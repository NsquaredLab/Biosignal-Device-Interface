"""
Quattrocento Light class for real-time interface to 
Quattrocento using OT Biolab Light.

Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2023-06-05
"""

# Python Libraries
from __future__ import annotations
from typing import TYPE_CHECKING, Union, Dict
from PySide6.QtNetwork import QTcpSocket, QHostAddress
from PySide6.QtCore import QIODevice
import numpy as np


from biosignal_device_interface.devices.core.base_device import BaseDevice
from biosignal_device_interface.constants.devices.core.base_device_constants import (
    DeviceType,
)
from biosignal_device_interface.constants.devices.otb.otb_quattrocento_light_constants import (
    COMMAND_START_STREAMING,
    COMMAND_STOP_STREAMING,
    CONNECTION_RESPONSE,
    QUATTROCENTO_LIGHT_STREAMING_FREQUENCY_DICT,
    QUATTROCENTO_SAMPLING_FREQUENCY_DICT,
    QuattrocentoLightSamplingFrequency,
    QuattrocentoLightStreamingFrequency,
)


if TYPE_CHECKING:
    # Python Libraries
    from PySide6.QtWidgets import QMainWindow, QWidget
    from aenum import Enum


class OTBQuattrocentoLight(BaseDevice):
    """
    QuattrocentoLight device class derived from BaseDevice class.
    The QuattrocentoLight is using a TCP/IP protocol to communicate with the device.

    This class directly interfaces with the OT Biolab Light software from
    OT Bioelettronica. The configured settings of the device have to
    match the settings from the OT Biolab Light software!
    """

    def __init__(
        self,
        parent: Union[QMainWindow, QWidget] = None,
    ) -> None:
        super().__init__(parent)

        # Device Parameters
        self._device_type: DeviceType = DeviceType.OTB_QUATTROCENTO_LIGHT

        # Device Information
        self._number_of_channels: int = 408  # Fix value
        self._auxiliary_channel_start_index: int = 384  # Fix value
        self._number_of_auxiliary_channels: int = 16  # Fix value
        self._conversion_factor_biosignal: float = 5 / (2**16) / 150 * 1000  # in mV
        self._conversion_factor_auxiliary: float = 5 / (2**16) / 0.5  # in mV
        self._bytes_per_sample: int = 2  # Fix value
        # Quattrocento unique parameters
        self._streaming_frequency: int | None = None

        # Connection Parameters
        self._interface: QTcpSocket = QTcpSocket()

        # Configuration Parameters
        self._grids: list[int] | None = None
        self._grid_size: int = 64  # TODO: This is only valid for the big electrodes
        self._streaming_frequency_mode: QuattrocentoLightStreamingFrequency | None = (
            None
        )
        self._sampling_frequency_mode: QuattrocentoLightSamplingFrequency | None = None

    def _connect_to_device(self) -> bool:
        super()._connect_to_device()

        self._received_bytes: bytearray = bytearray()
        return self._make_request()

    def _make_request(self) -> bool:
        super()._make_request()
        # Signal self.connect_toggled is emitted in _read_data
        self._interface.connectToHost(
            QHostAddress(self._connection_settings[0]),
            self._connection_settings[1],
            QIODevice.ReadWrite,
        )

        if not self._interface.waitForConnected(1000):
            self._disconnect_from_device()
            return False

        self._interface.readyRead.connect(self._read_data)

        return True

    def _disconnect_from_device(self) -> None:
        super()._disconnect_from_device()

        self._interface.disconnectFromHost()
        self._interface.readyRead.disconnect(self._read_data)
        self._interface.close()

    def configure_device(
        self, params: Dict[str, Union[Enum, Dict[str, Enum]]]  # type: ignore
    ) -> None:
        super().configure_device(params)

        # Configure the device
        self._number_of_biosignal_channels = len(self._grids) * self._grid_size
        self._biosignal_channel_indices = np.array(
            [
                i * self._grid_size + j
                for i in self._grids
                for j in range(self._grid_size)
            ]
        )

        self._auxiliary_channel_indices = np.array(
            [
                i + self._auxiliary_channel_start_index
                for i in range(self._number_of_auxiliary_channels)
            ]
        )

        self._streaming_frequency = QUATTROCENTO_LIGHT_STREAMING_FREQUENCY_DICT[
            self._streaming_frequency_mode
        ]
        self._sampling_frequency = QUATTROCENTO_SAMPLING_FREQUENCY_DICT[
            self._sampling_frequency_mode
        ]

        self._samples_per_frame = self._sampling_frequency // self._streaming_frequency

        self._buffer_size = (
            self._bytes_per_sample * self._number_of_channels * self._samples_per_frame
        )

        self._is_configured = True
        self.configure_toggled.emit(True)

    def _start_streaming(self) -> None:
        super()._start_streaming()

        self._interface.write(COMMAND_START_STREAMING)

    def _stop_streaming(self) -> None:
        super()._stop_streaming()

        self._interface.write(COMMAND_STOP_STREAMING)
        self._interface.waitForBytesWritten(1000)

    def clear_socket(self) -> None:
        super().clear_socket()

        self._interface.readAll()

    def _read_data(self) -> None:
        super()._read_data()

        # Wait for connection response
        if not self.is_connected and (
            self._interface.bytesAvailable() == len(CONNECTION_RESPONSE)
            and self._interface.readAll() == CONNECTION_RESPONSE
        ):
            self.is_connected = True
            self.connect_toggled.emit(True)
            return
        if not self._is_streaming:
            self.clear_socket()
            return

        while self._interface.bytesAvailable() > self._buffer_size:
            packet = self._interface.read(self._buffer_size)
            if not packet:
                continue

            self._received_bytes.extend(packet)

            while len(self._received_bytes) >= self._buffer_size:
                data_to_process = self._received_bytes[: self._buffer_size]
                self._process_data(data_to_process)
                self._received_bytes = self._received_bytes[self._buffer_size :]

    def _process_data(self, input: bytearray) -> None:
        super()._process_data(input)

        # Decode the data
        decoded_data = np.frombuffer(input, dtype=np.int16)

        # Reshape it to the correct format
        processed_data = decoded_data.reshape(
            self._number_of_channels, -1, order="F"
        ).astype(np.float32)

        # Emit the data
        self.data_available.emit(processed_data)

        biosignal_data = self._extract_biosignal_data(processed_data)
        self.biosignal_data_available.emit(biosignal_data)
        auxiliary_data = self._extract_auxiliary_data(processed_data)
        self.auxiliary_data_available.emit(auxiliary_data)

    def get_device_information(self) -> Dict[str, Enum | int | float | str]:  # type: ignore
        return super().get_device_information()
