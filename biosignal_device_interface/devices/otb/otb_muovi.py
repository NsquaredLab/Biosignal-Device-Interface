"""
OT Bioelettronica Muovi Device Interface
========================================

This module provides real-time interface implementation for OT Bioelettronica Muovi
and Muovi Plus devices. The Muovi is a wireless EMG acquisition system that supports
up to 32 channels (Muovi) or 64 channels (Muovi Plus) of high-quality biosignal recording.

The implementation uses TCP/IP protocol for communication and supports various
working modes including EMG, EEG, and different detection modes with configurable
gain settings.

Key Features:
- Real-time data streaming over TCP/IP
- Support for both Muovi (32 ch) and Muovi Plus (64 ch)
- Multiple working modes (EMG, EEG, etc.)
- Configurable detection modes and gain settings
- Automatic data conversion to millivolts
- Frame-based data acquisition

Classes:
    OTBMuovi: Main device class for Muovi/Muovi Plus devices

Author: Dominik I. Braun <dome.braun@fau.de>
Last Update: 2024-06-05
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
from biosignal_device_interface.constants.devices.otb.otb_muovi_constants import (
    MUOVI_CONVERSION_FACTOR_DICT,
    MuoviWorkingMode,
    MuoviDetectionMode,
    MUOVI_WORKING_MODE_CHARACTERISTICS_DICT,
    MUOVI_SAMPLES_PER_FRAME_DICT,
    MUOVI_AVAILABLE_CHANNELS_DICT,
)

if TYPE_CHECKING:
    from PySide6.QtWidgets import QMainWindow, QWidget
    from aenum import Enum


class OTBMuovi(BaseDevice):
    """
    OT Bioelettronica Muovi/Muovi Plus device interface.
    
    This class provides real-time communication with Muovi and Muovi Plus devices
    using TCP/IP protocol. The device acts as a TCP server, waiting for connections
    from the Muovi hardware.
    
    The Muovi supports various working modes:
    - EMG: Electromyography recording
    - EEG: Electroencephalography recording  
    - Other specialized modes
    
    Detection modes with different gain settings:
    - MONOPOLAR_GAIN_1, MONOPOLAR_GAIN_2, MONOPOLAR_GAIN_4, MONOPOLAR_GAIN_8
    - DIFFERENTIAL modes
    - IMPEDANCE_CHECK mode
    
    Parameters
    ----------
    parent : Union[QMainWindow, QWidget], optional
        Parent widget for the device. Defaults to None.
    is_muovi_plus : bool, optional
        Set to True for Muovi Plus (64 channels), False for standard Muovi 
        (32 channels). Defaults to False.
            
    Attributes
    ----------
    _device_type : DeviceType
        Type of device (MUOVI or MUOVI_PLUS)
    _working_mode : MuoviWorkingMode
        Current working mode configuration
    _detection_mode : MuoviDetectionMode
        Current detection mode configuration
    _configuration_command : int
        Encoded configuration command for the device
        
    Notes
    -----
    The device uses TCP/IP protocol where this class acts as a server and the
    Muovi hardware connects as a client. Connection settings specify the IP
    address and port to listen on.
    """

    def __init__(
        self,
        parent: Union[QMainWindow, QWidget] = None,
        is_muovi_plus: bool = False,
    ) -> None:
        """
        Initialize the Muovi device.

        Parameters
        ----------
        parent : Union[QMainWindow, QWidget], optional
            Parent widget. Defaults to None.
        is_muovi_plus : bool, optional
            Boolean to initialize the Muovi device as Muovi+ (64 biosignal channels) 
            or Muovi (32 biosignal channels). Defaults to False (Muovi).
        """
        super().__init__(parent)

        # Device Parameters
        self._device_type: DeviceType = (
            DeviceType.OTB_MUOVI_PLUS if is_muovi_plus else DeviceType.OTB_MUOVI
        )

        # Connection Parameters
        self._interface: QTcpServer = None
        self._client_socket: QTcpSocket | None = None

        # Configuration Parameters
        self._working_mode: MuoviWorkingMode = MuoviWorkingMode.NONE
        self._detection_mode: MuoviDetectionMode = MuoviDetectionMode.NONE
        self._configuration_command: int | None = None

    def _connect_to_device(self) -> bool:
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

        # Check if detection mode is valid for working mode (Case EEG -> MONOPOLAR_GAIN_4 => MONOPOLAR_GAIN_8)
        if self._working_mode == MuoviWorkingMode.EEG:
            if self._detection_mode == MuoviDetectionMode.MONOPOLAR_GAIN_4:
                self._detection_mode = MuoviDetectionMode.MONOPOLAR_GAIN_8

        self._conversion_factor_biosignal = MUOVI_CONVERSION_FACTOR_DICT[
            self._detection_mode
        ]
        self._conversion_factor_auxiliary = self._conversion_factor_biosignal

        # Set configuration parameters for data transfer
        working_mode_characteristics = MUOVI_WORKING_MODE_CHARACTERISTICS_DICT[
            self._working_mode
        ]
        self._sampling_frequency = working_mode_characteristics["sampling_frequency"]
        self._bytes_per_sample = working_mode_characteristics["bytes_per_sample"]
        self._samples_per_frame = MUOVI_SAMPLES_PER_FRAME_DICT[self._device_type][
            self._working_mode
        ]

        self._number_of_channels = MUOVI_AVAILABLE_CHANNELS_DICT[self._device_type][
            DeviceChannelTypes.ALL
        ]
        self._number_of_biosignal_channels = MUOVI_AVAILABLE_CHANNELS_DICT[
            self._device_type
        ][DeviceChannelTypes.BIOSIGNAL]
        self._biosignal_channel_indices = np.arange(self._number_of_biosignal_channels)

        self._number_of_auxiliary_channels = MUOVI_AVAILABLE_CHANNELS_DICT[
            self._device_type
        ][DeviceChannelTypes.AUXILIARY]
        self._auxiliary_channel_indices = np.arange(
            self._number_of_biosignal_channels,
            self._number_of_biosignal_channels + self._number_of_auxiliary_channels,
        )

        self._buffer_size = (
            self._number_of_channels * self._samples_per_frame * self._bytes_per_sample
        )

        self._received_bytes = bytearray()

        self._configure_command()
        self._send_configuration_to_device()

    def _send_configuration_to_device(self) -> None:
        """
        Send the configuration command to the connected Muovi device.
        
        Converts the configuration command to bytes and sends it via TCP socket.
        If sending fails, disconnects from the device.
        """
        configuration_bytes = int(self._configuration_command).to_bytes(
            1, byteorder="big"
        )

        success = self._client_socket.write(configuration_bytes)

        if success == -1:
            self._disconnect_from_device()

    def _configure_command(self) -> None:
        """
        Encode the working mode and detection mode into a configuration command.
        
        The configuration command is a single byte where:
        - Bits 2-7: Working mode value (shifted left by 2)
        - Bits 0-1: Detection mode value
        """
        self._configuration_command = self._working_mode.value << 2
        self._configuration_command += self._detection_mode.value

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

    def _read_data(self) -> None:
        super()._read_data()

        if not self._is_streaming:
            self.clear_socket()
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

    def _process_data(self, input: bytearray) -> None:
        super()._process_data(input)

        decoded_data = self._bytes_to_integers(input)

        processed_data = decoded_data.reshape(
            self._number_of_channels, -1, order="F"
        ).astype(np.float32)

        # Emit the data
        self.data_available.emit(processed_data)
        self.biosignal_data_available.emit(self._extract_biosignal_data(processed_data))
        self.auxiliary_data_available.emit(self._extract_auxiliary_data(processed_data))

    def _bytes_to_integers(
        self,
        data: bytearray,
    ) -> np.ndarray:
        """
        Convert raw byte data to integer values.
        
        Separates channels from the byte stream and converts each channel's
        bytes to integer values based on the current working mode.
        
        Parameters
        ----------
        data : bytearray
            Raw byte data from the device
            
        Returns
        -------
        np.ndarray
            Array of integer values for each channel
        """
        channel_values = []
        # Separate channels from byte-string. One channel has
        # "bytes_in_sample" many bytes in it.
        for channel_index in range(len(data) // 2):
            channel_start = channel_index * self._bytes_per_sample
            channel_end = (channel_index + 1) * self._bytes_per_sample
            channel = data[channel_start:channel_end]

            # Convert channel's byte value to integer
            match self._working_mode:
                case MuoviWorkingMode.EMG:
                    value = self._decode_int16(channel)
                case MuoviWorkingMode.EEG:
                    value = self._decode_int24(channel)

            channel_values.append(value)

        return np.array(channel_values)

    def _decode_int16(self, bytes_value: bytearray) -> int:
        """
        Decode 2 bytes to a 16-bit signed integer using two's complement.
        
        Parameters
        ----------
        bytes_value : bytearray
            2-byte array to decode
            
        Returns
        -------
        int
            Decoded 16-bit signed integer value
        """
        value = None
        # Combine 2 bytes to a 16 bit integer value
        value = bytes_value[0] * 2**8 + bytes_value[1]
        # See if the value is negative and make the two's complement
        if value >= 2**15:
            value -= 2**16
        return value

    def _decode_int24(self, bytes_value: bytearray) -> int:
        """
        Decode 3 bytes to a 24-bit signed integer using two's complement.
        
        Parameters
        ----------
        bytes_value : bytearray
            3-byte array to decode
            
        Returns
        -------
        int
            Decoded 24-bit signed integer value
        """
        value = None
        # Combine 3 bytes to a 24 bit integer value
        value = bytes_value[0] * 2**16 + bytes_value[1] * 2**8 + bytes_value[2]
        # See if the value is negative and make the two's complement
        if value >= 2**23:
            value -= 2**24
        return value
