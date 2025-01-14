"""
Quattrocento class for real-time direct interface to 
Quattrocento.

Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2025-01-14
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
from biosignal_device_interface.constants.devices.otb.otb_quattrocento_constants import (
    QuattrocentoAcqSettByte,
    QuattrocentoINXConf2Byte,
    QuattrocentoRecordingMode,
    QuattrocentoSamplingFrequencyMode,
    QuattrocentoNumberOfChannelsMode,
    QuattrocentoLowPassFilterMode,
    QuattrocentoHighPassFilterMode,
    QuattrocentoDetectionMode,
)

if TYPE_CHECKING:
    # Python Libraries
    from PySide6.QtWidgets import QMainWindow, QWidget
    from aenum import Enum


class OTBQuattrocento(BaseDevice):
    """
    Quattrocento device class derived from BaseDevice class.
    The Quattrocento is using a TCP/IP protocol to communicate with the device.

    This class directly interfaces with the Quattrocento from
    OT Bioelettronica.
    """

    def __init__(self, parent: Union[QMainWindow, QWidget] = None):
        super().__init__(parent)

        # Device Paramters
        self._device_type: DeviceType = DeviceType.OTB_QUATTROCENTO

        # Device Information
        self._conversion_factor_biosignal: float = 5 / (2**16) / 150 * 1000  # in mV
        self._conversion_factor_auxiliary: float = 5 / (2**16) / 0.5  # in mV
        self._number_of_streamed_channels: int = None

        # Connection Parameters
        self._interface: QTcpSocket = QTcpSocket()

        # Configuration parameters
        self._acq_sett_configuration: QuattrocentoAcqSettByte = (
            QuattrocentoAcqSettByte()
        )
        self._input_top_left_configuration: QuattrocentoINXConf2Byte = (
            QuattrocentoINXConf2Byte()
        )
        self._input_top_right_configuration: QuattrocentoINXConf2Byte = (
            QuattrocentoINXConf2Byte()
        )
        self._multiple_input_one_configuration: QuattrocentoINXConf2Byte = (
            QuattrocentoINXConf2Byte()
        )
        self._multiple_input_two_configuration: QuattrocentoINXConf2Byte = (
            QuattrocentoINXConf2Byte()
        )
        self._multiple_input_three_configuration: QuattrocentoINXConf2Byte = (
            QuattrocentoINXConf2Byte()
        )
        self._multiple_input_four_configuration: QuattrocentoINXConf2Byte = (
            QuattrocentoINXConf2Byte()
        )

        self._configuration_command: bytearray = bytearray(40)

    def _connect_to_device(self) -> bool:
        super()._connect_to_device()

        self._received_bytes: bytearray = bytearray()
        return self._make_request()

    def _make_request(self) -> bool:
        super()._make_request()

        self._interface.connectToHost(
            QHostAddress(self._connection_settings[0]), self._connection_settings[1]
        )

        if not self._interface.waitForConnected(1000):
            self._disconnect_from_device()
            return False

        self._interface.readyRead.connect(self._read_data)

        self._is_connected = True
        self.connect_toggled.emit(self._is_connected)

        return True

    def _disconnect_from_device(self) -> None:
        super()._disconnect_from_device()

        self._interface.disconnectFromHost()
        self._interface.readyRead.disconnect(self._read_data)
        self._interface.close()

    def _update_configuration_parameters(
        self, params: Dict[str, Union[Enum, Dict[str, Enum]]]  # type: ignore
    ) -> None:
        """
        Overwrite the base class method to update the configuration parameters
        """
        for key, value in params.items():
            key = f"_{key}"
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                print(
                    f"Attribute '{key}' not found in the class of {self._device_type.name}",
                )

        # TODO: Update Config Byte classes depending on input

    def configure_device(
        self, params: Dict[str, Union[Enum, Dict[str, Enum]]]  # type: ignore
    ):
        super().configure_device(params)

        self._sampling_frequency = self._acq_sett_configuration.get_sampling_frequency()
        self._number_of_streamed_channels = (
            self._acq_sett_configuration.get_number_of_channels()
        )

        # Configure the device
        # Byte 1: ACQ_SETT
        self._configuration_command[0] = bytes(self._acq_sett_configuration)

        # Byte 2: Configure AN_OUT_IN_SEL
        self._configuration_command[1] = bytes(0)  # TODO:

        # Byte 3: Configure AN_OUT_CH_SEL
        self._configuration_command[2] = bytes(0)  # TODO:

        # Byte 4-15: Configure IN1-4 -> TODO: change that to individual configuration
        for i in range(4):
            self._configuration_command[3 + i * 3 : 3 + i * 3 + 3] = bytes(
                self._input_top_left_configuration
            )

        # Byte 16-27: Configure IN5-8 -> TODO: change that to individual configuration
        for i in range(4):
            self._configuration_command[15 + i * 3 : 15 + i * 3 + 3] = bytes(
                self._input_top_right_configuration
            )

        # Byte 28-30: Configure MULTIPLE IN 1
        self._configuration_command[27:30] = bytes(
            self._multiple_input_one_configuration
        )

        # Byte 31-33: Configure MULTIPLE IN 2
        self._configuration_command[30:33] = bytes(
            self._multiple_input_two_configuration
        )

        # Byte 34-36: Configure MULTIPLE IN 3
        self._configuration_command[33:36] = bytes(
            self._multiple_input_three_configuration
        )

        # Byte 37-39: Configure MULTIPLE IN 4
        self._configuration_command[36:39] = bytes(
            self._multiple_input_four_configuration
        )

        # Control Byte
        self._configuration_command[39] = self._crc_check(
            self._configuration_command, 39
        )

        self._send_configuration_to_device()

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

    def _send_configuration_to_device(self) -> None:
        success = self._interface.write(self._configuration_command)

        if success == -1:
            print("Error while sending configuration to device")

    def _stop_streaming(self) -> None:
        super()._stop_streaming()

        self._configuration_command[0] -= 1
        self._configuration_command[39] = self._crc_check(
            self._configuration_command, 39
        )
        self._send_configuration_to_device()

    def _start_streaming(self) -> None:
        super()._start_streaming()

        self._configuration_command[0] += 1
        self._configuration_command[39] = self._crc_check(
            self._configuration_command, 39
        )
        self._send_configuration_to_device()

        self._is_streaming = True
        self.stream_toggled.emit(self._is_streaming)

    def clear_socket(self) -> None:
        if self._interface is not None:
            self._interface.readAll()

    def _read_data(self) -> None:
        super()._read_data()

        if not self._is_streaming:
            self.clear_socket()
            return

        while self._interface.bytesAvailable() > self._buffer_size:
            packet = self._interface.readAll()
            if not packet:
                continue

            self._received_bytes.extend(packet)

            while len(self._received_bytes) >= self._buffer_size:
                data_to_process = self._received_bytes[: self._buffer_size]
                self._process_data(data_to_process)
                self._received_bytes = self._received_bytes[self._buffer_size :]

    def _process_data(self, input: bytearray) -> None:
        super()._process_data(input)

        data = np.frombuffer(input, dtype="<i2")
        reshaped_data = data.reshape((self._number_of_streamed_channels, -1), order="F")

        # TODO: Slice the data to get only selected channels
        processed_data = reshaped_data[self._number_of_channels, :].astype(np.float32)

        self.data_available.emit(processed_data)
        self.biosignal_data_available.emit(self._extract_biosignal_data(processed_data))
        self.auxiliary_data_available.emit(self._extract_auxiliary_data(processed_data))
