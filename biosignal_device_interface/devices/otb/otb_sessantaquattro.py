"""
Device class for real-time interfacing the Sessantaquattro device.
Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2025-09-16
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Union, Dict
from PySide6.QtNetwork import QTcpSocket, QTcpServer, QHostAddress
import numpy as np

# Local Libraries
from biosignal_device_interface.devices.core.base_device import BaseDevice
from biosignal_device_interface.constants.devices.core.base_device_constants import (
    DeviceType,
    DeviceChannelTypes,
)

# Constants
from biosignal_device_interface.constants.devices.otb.otb_sessantaquattro_constants import (
    SESSANTAQUATTRO_AUXILIARY_LSB_DICT,
    SESSANTAQUATTRO_CHANNEL_MODE_CHARACTERISTICS_DICT,
    SESSANTAQUATTRO_DETECTION_MODE_CHARACTERISTICS_DICT,
    SESSANTAQUATTRO_GAIN_MODE_CHARACTERISTICS_DICT,
    SESSANTAQUATTRO_BIOSIGNAL_LSB,
    SESSANTAQUATTRO_SAMPLES_PER_FRAME_DICT,
    SessantaquattroChannelMode,
    SessantaquattroDetectionMode,
    SessantaquattroGainMode,
    SessantaquattroRecordingMode,
    SessantaquattroResolutionMode,
    SessantaquattroSamplingFrequencyMode,
    SessantaquattroTriggerMode,
)

if TYPE_CHECKING:
    from PySide6.QtWidgets import QMainWindow, QWidget
    from aenum import Enum


class OTBSessantaquattro(BaseDevice):
    """
    Device class for real-time interfacing the Sessantaquattro device.

    parent (Union[QMainWindow, QWidget], optional):
            Parent widget to which the device is assigned to.
            Defaults to None.

    The Sessantaquattro class is using a TCP/IP protocol to communicate with the device.
    """

    def __init__(
        self,
        parent: Union[QMainWindow, QWidget],
    ) -> None:
        """Initialize the OTBSessantaquattro device.

        Args:
            parent (Union[QMainWindow, QWidget]): Parent widget to which the device is assigned to.
        """
        super().__init__(parent=parent)

        # Device Parameters
        self._device_type: DeviceType = DeviceType.OTB_SESSANTAQUATTRO

        # Connection Parameters
        self._interface: QTcpServer = None
        self._client_socket: QTcpSocket = None

        # Configuration Parameters
        ## Control Byte 0
        self._sampling_frequency_mode: SessantaquattroSamplingFrequencyMode = (
            SessantaquattroSamplingFrequencyMode.NONE
        )
        self._channel_mode: SessantaquattroChannelMode = SessantaquattroChannelMode.NONE
        self._detection_mode: SessantaquattroDetectionMode = (
            SessantaquattroDetectionMode.NONE
        )

        ## Control  Byte 1
        self._resolution_mode: SessantaquattroResolutionMode = (
            SessantaquattroResolutionMode.NONE
        )
        self._gain_mode: SessantaquattroGainMode = SessantaquattroGainMode.NONE
        self._trigger_mode: SessantaquattroTriggerMode = SessantaquattroTriggerMode.NONE
        self._recording_mode: SessantaquattroRecordingMode = (
            SessantaquattroRecordingMode.NONE
        )

    def _connect_to_device(self):
        super()._connect_to_device()

        self._interface = QTcpServer(self)
        self._received_bytes: bytearray = bytearray()

        if not self._interface.listen(
            QHostAddress(self._connection_settings[0]), self._connection_settings[1]
        ):
            return False

        self._interface.newConnection.connect(self._make_request)

        self._connection_timeout_timer.start()

        return True

    def _make_request(self) -> bool:
        super()._make_request()
        self._client_socket = self._interface.nextPendingConnection()

        if self._client_socket:

            self._client_socket.readyRead.connect(self._read_data)

            if not self.is_connected:
                self.is_connected = True
                self.connect_toggled.emit(self.is_connected)
                self._connection_timeout_timer.stop()
                return True

            elif not self._is_configured:
                self._is_configured = True
                self.configure_toggled.emit(self._is_configured)
                return True

    def _disconnect_from_device(self) -> bool:
        super()._disconnect_from_device()

        if self._client_socket is not None:
            self._client_socket.readyRead.disconnect(self._read_data)
            self._client_socket.disconnectFromHost()
            self._client_socket.close()

        if self._interface is not None:
            self._interface.close()

        return True

    def configure_device(
        self, params: Dict[str, Union[Enum, Dict[str, Enum]]]  # type: ignore
    ) -> None:
        super().configure_device(params)

        if not self.is_connected or self._client_socket is None:
            return

        # Set Configuration Parameters
        self._sampling_frequency = SESSANTAQUATTRO_DETECTION_MODE_CHARACTERISTICS_DICT[
            self._detection_mode
        ][self._sampling_frequency_mode]

        channels = SESSANTAQUATTRO_CHANNEL_MODE_CHARACTERISTICS_DICT[
            self._sampling_frequency_mode
        ][self._detection_mode]

        self._number_of_biosignal_channels = channels[DeviceChannelTypes.BIOSIGNAL]
        self._biosignal_channel_indices = np.arange(
            0, self._number_of_biosignal_channels
        )
        self._number_of_auxiliary_channels = channels[DeviceChannelTypes.AUXILIARY]
        self._auxiliary_channel_indices = np.arange(
            self._number_of_biosignal_channels,
            self._number_of_biosignal_channels + self._number_of_auxiliary_channels,
        )

        self._number_of_channels = (
            self._number_of_biosignal_channels + self._number_of_auxiliary_channels
        )

        self._bytes_per_sample = (
            2 if self._resolution_mode == SessantaquattroResolutionMode.LOW else 3
        )

        self._conversion_factor_biosignal = SESSANTAQUATTRO_BIOSIGNAL_LSB * (
            SESSANTAQUATTRO_GAIN_MODE_CHARACTERISTICS_DICT[self._resolution_mode][
                self._gain_mode
            ]
        )

        self._conversion_factor_auxiliary = SESSANTAQUATTRO_AUXILIARY_LSB_DICT[
            self._resolution_mode
        ]

        self._samples_per_frame = SESSANTAQUATTRO_SAMPLES_PER_FRAME_DICT[
            self._channel_mode
        ]

        # Prepare streaming
        self._buffer_size = (
            self._number_of_channels * self._samples_per_frame * self._bytes_per_sample
        )

        self._received_bytes = bytearray()

        self._configure_command()
        self._send_configuration_to_device()

    def _send_configuration_to_device(self) -> None:
        configuration_bytes = int(self._configuration_command).to_bytes(
            1, byteorder="big"
        )

        success = self._client_socket.write(configuration_bytes)

        if success == -1:
            self._disconnect_from_device()

    def _configure_command(self) -> None:
        self._configuration_command = 0

        # Control Byte 0
        # Bit 0 - Transmission Mode | Handled by Start / Stop Streaming
        # Bit 1
        if self._recording_mode == SessantaquattroRecordingMode.NONE:
            self._recording_mode = SessantaquattroRecordingMode.STOP
        self._configuration_command += (self._recording_mode.value - 1) << 1

        # Bit 3-2
        if self._trigger_mode == SessantaquattroTriggerMode.NONE:
            self._trigger_mode = SessantaquattroTriggerMode.DEFAULT
        self._configuration_command += (self._trigger_mode.value - 1) << 2

        # Bit 5-4
        if self._gain_mode == SessantaquattroGainMode.NONE:
            self._gain_mode = SessantaquattroGainMode.DEFAULT
        self._configuration_command += (self._gain_mode.value - 1) << 4

        # Bit 6 - Filter mode: disable high pass filter
        self._configuration_command += 0 << 6

        # Bit 7 - Resolution mode
        if self._resolution_mode == SessantaquattroResolutionMode.NONE:
            self._resolution_mode = SessantaquattroResolutionMode.LOW
        self._configuration_command += (self._resolution_mode.value - 1) << 7

        # Control Byte 1
        # Bit 2-0 - Detection Mode
        if self._detection_mode == SessantaquattroDetectionMode.NONE:
            self._detection_mode = SessantaquattroDetectionMode.MONOPOLAR
        self._configuration_command += (self._detection_mode.value - 1) << 8

        # Bit 4-3 - Channel Mode
        if self._channel_mode == SessantaquattroChannelMode.NONE:
            self._channel_mode = SessantaquattroChannelMode.LOW
        self._configuration_command += (self._channel_mode.value - 1) << 11

        # Bit 6-5 - Sampling Frequency Mode
        if self._sampling_frequency_mode == SessantaquattroSamplingFrequencyMode.NONE:
            self._sampling_frequency_mode = SessantaquattroSamplingFrequencyMode.HIGH
        self._configuration_command += (self._sampling_frequency_mode.value - 1) << 13

        # Bit 7 - GETSET - always 0 for setting the configuration
        self._configuration_command += 0 << 15

    def _start_streaming(self) -> None:
        super()._start_streaming()

        if self._configuration_command is None:
            return

        self._configuration_command += 1
        self._send_configuration_to_device()

    def _stop_streaming(self) -> None:
        super()._stop_streaming()

        if self._configuration_command is None:
            return

        self._configuration_command -= 1
        self._send_configuration_to_device()

    def clear_socket(self) -> None:
        if self._client_socket is not None:
            self._client_socket.readAll()
            self._received_bytes = bytearray()

    def _read_data(self) -> None:
        super()._read_data()

        if self._client_socket is None:
            return

        if not self._is_streaming:
            buffer_size: int = 13
            config_bytes = self._client_socket.read(
                buffer_size
            )  # TODO: Catches configuration settings, has to be checked

            self._process_configuration_data(config_bytes)
            return

        while self._client_socket.bytesAvailable() > self._buffer_size:
            packet = self._client_socket.read(self._buffer_size)
            if not packet:
                continue

            self._received_bytes.extend(packet)

            while len(self._received_bytes) >= self._buffer_size:
                data_to_process = self._received_bytes[: self._buffer_size]
                self._process_data(data_to_process)
                self._received_bytes = self._received_bytes[self._buffer_size :]

    def _process_configuration_data(self, input: bytearray) -> None:
        # TODO: Implement configuration data processing
        ...

    def _process_data(self, input: bytearray) -> None:
        super()._process_data(input)

        decoded_data = self._bytes_to_integers(input)

        processed_data = decoded_data.reshape(
            self._number_of_channels, -1, order="F"
        ).astype(np.float32)

        self.data_available.emit(processed_data)
        self.biosignal_data_available.emit(self._extract_biosignal_data(processed_data))
        self.auxiliary_data_available.emit(self._extract_auxiliary_data(processed_data))

    # Convert integer to bytes
    def _integer_to_bytes(self, command: int) -> bytes:
        return command.to_bytes(2, byteorder="big")

    # Convert channels from bytes to integers
    def _bytes_to_integers(
        self,
        data: bytearray,
    ) -> np.ndarray:
        channel_values = []
        # Separate channels from byte-string. One channel has
        # "bytes_in_sample" many bytes in it.
        for channel_index in range(len(data) // 2):
            channel_start = channel_index * self._bytes_per_sample
            channel_end = (channel_index + 1) * self._bytes_per_sample
            channel = data[channel_start:channel_end]

            # Convert channel's byte value to integer
            if self._resolution_mode == SessantaquattroResolutionMode.LOW:
                value = self._decode_int16(channel)
            else:
                value = self._decode_int24(channel)
            channel_values.append(value)

        return np.array(channel_values)

    def _decode_int16(self, bytes_value: bytearray) -> int:
        value = None
        # Combine 2 bytes to a 16 bit integer value
        value = bytes_value[0] * 256 + bytes_value[1]
        # See if the value is negative and make the two's complement
        if value >= 32768:
            value -= 65536
        return value

    # Convert byte-array value to an integer value and apply two's complement
    def _decode_int24(self, bytes_value: bytearray) -> int:
        value = None
        # Combine 3 bytes to a 24 bit integer value
        value = bytes_value[0] * 65536 + bytes_value[1] * 256 + bytes_value[2]
        # See if the value is negative and make the two's complement
        if value >= 8388608:
            value -= 16777216
        return value
