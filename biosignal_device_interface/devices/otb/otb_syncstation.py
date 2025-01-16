"""
Device class for real-time interfacing the OTB Syncstation device.
Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2025-01-09
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Union, Dict
from PySide6.QtNetwork import QTcpSocket, QHostAddress
from PySide6.QtCore import QIODevice
import numpy as np

# Local Libraries
from biosignal_device_interface.constants.devices.otb.otb_syncstation_constants import (
    PROBE_CHARACTERISTICS_DICT,
    SYNCSTATION_CHARACTERISTICS_DICT,
    SYNCSTATION_CONVERSION_FACTOR_DICT,
    SyncStationDetectionMode,
    SyncStationProbeConfigMode,
    SyncStationRecOnMode,
    SyncStationWorkingMode,
)
from biosignal_device_interface.devices.core.base_device import BaseDevice
from biosignal_device_interface.constants.devices.core.base_device_constants import (
    DeviceType,
    DeviceChannelTypes,
)


if TYPE_CHECKING:
    from PySide6.QtWidgets import QMainWindow, QWidget
    from aenum import Enum


class OTBSyncStation(BaseDevice):
    """
    Device class for real-time interfacing the OTB Syncstation device.
    The SyncStation class is using a TCP/IP protocol to communicate with the device.
    """

    def __init__(self, parent: Union[QMainWindow, QWidget] = None) -> None:
        """
        Constructor of the OTBSyncStation class.

        Args:
            parent (Union[QMainWindow, QWidget]): The parent object of the device. Defaults to None.
        """
        super().__init__(parent)

        # Device Parameters
        self._device_type = DeviceType.OTB_SYNCSTATION

        # Connection Parameters
        self._interface: QTcpSocket = QTcpSocket()

        # Configuration Parameters
        self._configuration_command_A: bytearray = None
        self._configuration_command_B: bytearray = None

        # Configuration Parameters A
        self._rec_on_mode: SyncStationRecOnMode = None
        self._working_mode: SyncStationWorkingMode = None
        self._number_of_probes: int = None
        self._bytes_configuration_A: Dict[
            SyncStationProbeConfigMode, Dict[str, SyncStationDetectionMode | bool]
        ] = None

        # Configuration Parameters B
        self._bytes_configuration_B: Dict[str, int] = None

    def _connect_to_device(self) -> bool:
        super()._connect_to_device()

        self._received_bytes: bytearray = bytearray()
        self._make_request()

    def _make_request(self) -> bool:
        super()._make_request()

        self._interface.connectToHost(
            QHostAddress(self._connection_settings[0]),
            self._connection_settings[1],
            QIODevice.ReadWrite,
        )

        if not self._interface.waitForConnected(1000):
            self._disconnect_from_device()
            return False

        self.is_connected = True
        self.connect_toggled.emit(True)

        self._interface.readyRead.connect(self._read_data)
        return True

    def _disconnect_from_device(self) -> None:
        super()._disconnect_from_device()

        self._interface.disconnectFromHost()
        self._interface.readyRead.disconnect(self._read_data)
        self._interface.close()

        self.is_connected = False
        self.connect_toggled.emit(False)

    def configure_device(self, params) -> None:
        super().configure_device(params)

        success = self._configure_byte_sequence_A()

        if not success:
            print("Unable to configure device.")
            return

        self._send_configuration_to_device()

        self._is_configured = True
        self.configure_toggled.emit(True)

    def _configure_byte_sequence_A(self) -> None:
        start_byte = 0
        start_byte += (self._rec_on_mode.value - 1) << 6

        self._sampling_frequency = SYNCSTATION_CHARACTERISTICS_DICT[
            "channel_information"
        ][self._working_mode]["sampling_frequency"]
        self._bytes_per_sample = SYNCSTATION_CHARACTERISTICS_DICT[
            "channel_information"
        ][self._working_mode]["bytes_per_sample"]

        self._configuration_command_A = bytearray()
        self._number_of_channels = 0
        self._number_of_bytes = 0

        self._number_of_biosignal_channels = 0
        self._number_of_auxiliary_channels = 0
        self._biosignal_channel_indices = []
        self._auxiliary_channel_indices = []

        for key, value in self._bytes_configuration_A.items():
            probe_command = 0
            probe_command += (key.value - 1) << 4
            probe_command += (self._working_mode.value - 1) << 3
            probe_command += (value["detection_mode"].value - 1) << 1
            probe_command += int(value["probe_status"])

            if value["probe_status"]:
                self._configuration_command_A.append(probe_command)
                channels = PROBE_CHARACTERISTICS_DICT[key][DeviceChannelTypes.ALL]
                biosignal_channels = PROBE_CHARACTERISTICS_DICT[key][
                    DeviceChannelTypes.BIOSIGNAL
                ]
                auxiliary_channels = PROBE_CHARACTERISTICS_DICT[key][
                    DeviceChannelTypes.AUXILIARY
                ]

                self._biosignal_channel_indices.append(
                    np.arange(
                        self._number_of_channels,
                        self._number_of_channels + biosignal_channels,
                    )
                )

                self._auxiliary_channel_indices.append(
                    np.arange(
                        self._number_of_channels + biosignal_channels,
                        self._number_of_channels + channels,
                    )
                )

                self._number_of_channels += channels
                self._number_of_biosignal_channels += biosignal_channels
                self._number_of_auxiliary_channels += auxiliary_channels

        self._conversion_factor_biosignal = SYNCSTATION_CONVERSION_FACTOR_DICT[
            value["detection_mode"]
        ]
        self._conversion_factor_auxiliary = self._conversion_factor_biosignal

        self._biosignal_channel_indices = np.hstack(self._biosignal_channel_indices)
        self._auxiliary_channel_indices = np.hstack(self._auxiliary_channel_indices)
        self._number_of_bytes = self._number_of_channels * self._bytes_per_sample

        # Add SyncStation Channels
        self._number_of_channels += SYNCSTATION_CHARACTERISTICS_DICT[
            DeviceChannelTypes.ALL
        ]
        self._number_of_auxiliary_channels += SYNCSTATION_CHARACTERISTICS_DICT[
            DeviceChannelTypes.ALL
        ]

        self._number_of_bytes += (
            SYNCSTATION_CHARACTERISTICS_DICT[DeviceChannelTypes.ALL]
            * SYNCSTATION_CHARACTERISTICS_DICT["bytes_per_sample"]
        )

        self._samples_per_frame = int(
            (1 / SYNCSTATION_CHARACTERISTICS_DICT["FPS"]) * self._sampling_frequency
        )

        self._buffer_size = int(self._number_of_bytes * self._samples_per_frame)

        num_probes = len(self._configuration_command_A)
        start_byte += num_probes << 1
        self._configuration_command_A.insert(0, start_byte)
        start_byte_ckc8 = self._crc_check(
            self._configuration_command_A, len(self._configuration_command_A)
        )
        self._configuration_command_A.append(start_byte_ckc8)

        return True

    def _crc_check(self, command_bytes: bytearray, command_length: int) -> bytes:
        """
        Performs the Cyclic Redundancy Check (CRC) of the transmitted bytes.

        Translated function from example code provided by OT Bioelettronica.

        Args:
            command_bytes (bytearray):
                Bytearray of the transmitted bytes.

            command_length (int):
                Length of the transmitted bytes.

        Returns:
            bytes:
                CRC of the transmitted bytes.
        """

        crc = 0
        j = 0

        while command_length > 0:
            extracted_byte = command_bytes[j]
            for i in range(8, 0, -1):
                sum = crc % 2 ^ extracted_byte % 2
                crc = crc // 2

                if sum > 0:
                    crc_bin = format(crc, "08b")
                    a_bin = format(140, "08b")

                    str_list = []

                    for k in range(8):
                        str_list.append("0" if crc_bin[k] == a_bin[k] else "1")

                    crc = int("".join(str_list), 2)

                extracted_byte = extracted_byte // 2

            command_length -= 1
            j += 1

        return crc

    def _configure_byte_sequence_B(self) -> None:
        # TODO: Implement this method
        ...

    def _send_configuration_to_device(self) -> None:
        print(
            f"Device configuration sent: {[int.from_bytes(self._configuration_command_A[i : i + 1], 'big') for i in range(len(self._configuration_command_A))]}"
        )
        self._interface.write(self._configuration_command_A)

    def _stop_streaming(self):
        self._configuration_command_A[0] -= 1
        self._configuration_command_A[-1] = self._crc_check(
            self._configuration_command_A, len(self._configuration_command_A) - 1
        )

        self._send_configuration_to_device()

        self._is_streaming = False
        self.stream_toggled.emit(False)

    def _start_streaming(self):
        self._configuration_command_A[0] += 1
        self._configuration_command_A[-1] = self._crc_check(
            self._configuration_command_A, len(self._configuration_command_A) - 1
        )

        self._send_configuration_to_device()

        self._is_streaming = True
        self.stream_toggled.emit(True)

    def _clear_socket(self) -> None:
        """
        Clears the socket from any remaining data.
        """
        self._interface.readAll()
        self._received_bytes = bytearray()

    def _read_data(self) -> None:
        if not self._is_streaming:
            packet = self._interface.readAll()

        else:
            if self._interface.bytesAvailable() > 0:

                packet = self._interface.readAll()
                packet_bytearray = bytearray(packet.data())

                if not packet_bytearray:
                    return

                self._received_bytes.extend(packet_bytearray)

                while len(self._received_bytes) >= self._buffer_size:
                    self._process_data(
                        bytearray(self._received_bytes)[: self._buffer_size]
                    )
                    self._received_bytes = bytearray(self._received_bytes)[
                        self._buffer_size :
                    ]

    def _process_data(self, input: bytearray) -> None:
        data: np.ndarray = np.frombuffer(input, dtype=np.uint8).astype(np.float32)

        samples = self._samples_per_frame
        data = np.reshape(data, (samples, self._number_of_bytes)).T
        processed_data = self._bytes_to_integers(data)

        # Emit the data
        self.data_available.emit(processed_data)
        self.biosignal_data_available.emit(self._extract_biosignal_data(processed_data))
        self.auxiliary_data_available.emit(self._extract_auxiliary_data(processed_data))

    def _integer_to_bytes(self, command: int) -> bytes:
        return int(command).to_bytes(1, byteorder="big")

    # Convert channels from bytes to integers
    def _bytes_to_integers(
        self,
        data: np.ndarray,
    ) -> np.ndarray:
        samples = self._samples_per_frame
        frame_data = np.zeros((self._number_of_channels, samples), dtype=np.float32)
        channels_to_read = 0
        for device in list(SyncStationProbeConfigMode)[1:]:
            if self._bytes_configuration_A[device]["probe_status"]:
                channel_number = PROBE_CHARACTERISTICS_DICT[device][
                    DeviceChannelTypes.ALL
                ]
                # Convert channel's byte value to integer
                if self._working_mode == SyncStationWorkingMode.EMG:
                    channel_indices = (
                        np.arange(0, channel_number * 2, 2) + channels_to_read * 2
                    )
                    data_sub_matrix = self._decode_int16(data, channel_indices)
                    frame_data[
                        channels_to_read : channels_to_read + channel_number, :
                    ] = data_sub_matrix

                elif self._working_mode == SyncStationWorkingMode.EEG:
                    channel_indices = (
                        np.arange(0, channel_number * 3, 3) + channels_to_read * 2
                    )
                    data_sub_matrix = self._decode_int24(data, channel_indices)
                    frame_data[
                        channels_to_read : channels_to_read + channel_number, :
                    ] = data_sub_matrix

                channels_to_read += channel_number
                del data_sub_matrix
                del channel_indices

        syncstation_aux_bytes_number = (
            SYNCSTATION_CHARACTERISTICS_DICT[DeviceChannelTypes.ALL]
            * SYNCSTATION_CHARACTERISTICS_DICT["bytes_per_sample"]
        )
        syncstation_aux_starting_byte = (
            self._number_of_bytes - syncstation_aux_bytes_number
        )
        channel_indices = np.arange(
            syncstation_aux_starting_byte,
            syncstation_aux_starting_byte + syncstation_aux_bytes_number,
            2,
        )
        data_sub_matrix = self._decode_int16(data, channel_indices)
        frame_data[channels_to_read : channels_to_read + 6, :] = data_sub_matrix
        return np.array(frame_data)

    def _decode_int24(
        self, data: np.ndarray, channel_indices: np.ndarray
    ) -> np.ndarray:
        data_sub_matrix = (
            data[channel_indices, :] * 2**16
            + data[channel_indices + 1, :] * 2**8
            + data[channel_indices + 2, :]
        )
        negative_indices = np.where(data_sub_matrix >= 2**23)
        data_sub_matrix[negative_indices] -= 2**24

        return data_sub_matrix

    def _decode_int16(
        self, data: np.ndarray, channel_indices: np.ndarray
    ) -> np.ndarray:
        data_sub_matrix = data[channel_indices, :] * 2**8 + data[channel_indices + 1, :]
        negative_indices = np.where(data_sub_matrix >= 2**15)
        data_sub_matrix[negative_indices] -= 2**16
        return data_sub_matrix
