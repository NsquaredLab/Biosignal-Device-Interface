"""
Base Device class for real-time interfaces to hardware devices.
Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2024-06-05
"""

# Python Libraries
from __future__ import annotations
from typing import TYPE_CHECKING, Union, Dict, Tuple

from abc import abstractmethod
import socket
import psutil
from PySide6.QtCore import QObject, Signal, QTimer
import numpy as np
import re

# Local Libraries
from biosignal_device_interface.constants.devices.core.base_device_constants import (
    DeviceType,
    DEVICE_NAME_DICT,
)

# Type Checking
if TYPE_CHECKING:
    # Python Libraries
    from PySide6.QtWidgets import QMainWindow, QWidget
    from PySide6.QtNetwork import QTcpSocket, QUdpSocket, QTcpServer
    from PySide6.QtSerialPort import QSerialPort
    from aenum import Enum

import warnings

# Set to keep track of seen error messages
_seen_error_messages = set()


def warn_once(e):
    """
    Issue a warning for the given error, but only once per unique message.

    Args:
        e: Exception instance whose message will be used to track uniqueness.
    """
    error_message = str(e)
    if error_message not in _seen_error_messages:
        warnings.warn(f"An error occurred: {error_message}", UserWarning)
        _seen_error_messages.add(error_message)

class BaseDevice(QObject):
    # Signals
    connect_toggled: Signal = Signal(bool)
    configure_toggled: Signal = Signal(bool)
    stream_toggled: Signal = Signal(bool)
    data_available: Signal = Signal(np.ndarray)
    biosignal_data_available: Signal = Signal(np.ndarray)
    auxiliary_data_available: Signal = Signal(np.ndarray)

    def __init__(self, parent: Union[QMainWindow, QWidget] = None, **kwargs) -> None:
        super().__init__(parent)

        # Device Parameters
        self._device_type: DeviceType = None

        # Device Information
        self._sampling_frequency: int | None = None
        self._number_of_channels: int | None = None
        self._number_of_biosignal_channels: int | None = None
        self._biosignal_channel_indices: list[int] | None = None
        self._number_of_auxiliary_channels: int | None = None
        self._auxiliary_channel_indices: list[int] | None = None
        self._samples_per_frame: int | None = None
        self._bytes_per_sample: int | None = None

        self._conversion_factor_biosignal: float = None  # Returns mV
        self._conversion_factor_auxiliary: float = None  # Returns mV

        # Connection Parameters
        self._interface: QTcpServer | QTcpSocket | QUdpSocket | QSerialPort | None = (
            None
        )
        self._connection_settings: Tuple[str, int] | None = None
        self._buffer_size: int | None = None
        self._received_bytes: bytearray | None = None

        self._connection_timeout_timer: QTimer = QTimer()
        self._connection_timeout_timer.setSingleShot(True)
        self._connection_timeout_timer.timeout.connect(self._disconnect_from_device)
        self._connection_timeout_timer.setInterval(1000)

        # Device Status
        self.is_connected: bool = False
        self._is_configured: bool = False
        self._is_streaming: bool = False

    @abstractmethod
    def _connect_to_device(self) -> bool:
        """
        Function to attempt a connection to the devices.

        Returns:
            bool:
                Success of the connection attempt.
        """
        pass

    @abstractmethod
    def _make_request(self) -> bool:
        """
        Requests a connection or checks if someone connected to the server.
        After connection is successful, the Signal connected_signal emits True
        and sets the current state is_connected to True.

        Returns:
            bool:
                Returns True if request was successfully. False if not.
        """
        pass

    @abstractmethod
    def _disconnect_from_device(self) -> bool:
        """
        Closes the connection to the device.

        self.interface closes and is set to None.
        Device state is_connected is set to False.
        Signal connected_signal emits False.

        Returns:
            bool:
                Success of the disconnection attempt.
        """
        self.is_connected = False
        self.connect_toggled.emit(False)
        self._is_configured = False
        self.configure_toggled.emit(False)

    @abstractmethod
    def configure_device(self, params: Dict[str, Union[Enum, Dict[str, Enum]]]) -> None:  # type: ignore
        """
        Sends a configuration byte sequence based on selected params to the device.
        An overview of possible configurations can be seen in
        biosignal_device_interface/constants/{device}.py.

        E.g., enums/sessantaquattro.py


        Args:
            params (Dict[str, Union[Enum, Dict[str, Enum]]]):
                Dictionary that holds the configuration settings
                to which the device should be configured to.

                The first one should be the attributes (configuration mode) name,
                and the second its respective value. Orient yourself on the
                enums of the device to choose the correct configuration settings.
        """
        self._update_configuration_parameters(params)

    @abstractmethod
    def _start_streaming(self) -> None:
        """
        Sends the command to start the streaming to the device.

        if successful:
            Device state is_streaming is set to True.
            Signal streaming_signal emits True.
        """
        self._is_streaming = True
        self.stream_toggled.emit(True)

    @abstractmethod
    def _stop_streaming(self) -> None:
        """
        Sends the command to stop the streaing to the device

        if successful:
            Device state is_streaming is set to False.
            Signal streaming_signal emits False.
        """
        self._is_streaming = False
        self.stream_toggled.emit(False)

    @abstractmethod
    def clear_socket(self) -> None:
        """Reads all the bytes from the buffer."""
        pass

    @abstractmethod
    def _read_data(self) -> None:
        """
        This function is called when bytes are ready to be read in the buffer.
        After reading the bytes from the buffer, _process_data is called to
        decode and process the raw data.
        """
        pass

    @abstractmethod
    def _process_data(self, input: bytearray) -> None:
        """
        Decodes the transmitted bytes and convert them to respective
        output format (e.g., mV).

        Emits the processed data through the Signal data_available_signal
        which can be connected to a function using:
        {self.device}.data_available_signal.connect(your_custom_function).

        This works perfectly fine outside of this class.

        Your custom function your_custom_function needs to have a parameter
        "data" which is of type np.ndarray.


        In case that the current configuration of the device was requested,
        the configuration is provided through the Signal
        configuration_available_signal that emits the current parameters
        in a dictionary.

        Args:
            input (bytearray):
                Bytearray of the transmitted raw data.
        """
        pass

    def _update_configuration_parameters(
        self, params: Dict[str, Union[Enum, Dict[str, Enum]]]
    ) -> None:
        """
        Updates the device attributes with the new configuration parameters.

        Args:
            params (Dict[str, Union[Enum, Dict[str, Enum]]]):
                Dictionary that holds the configuration settings
                to which the device should be configured to.

                The first one should be the attributes (configuration mode) name,
                and the second its respective value. Orient yourself on the
                enums of the device to choose the correct configuration settings.
        """
        for key, value in params.items():
            key = "_" + key
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                print(
                    f"Attribute '{key}' not found in the class of {self._device_type.name}",
                )

    def _extract_biosignal_data(
        self, data: np.ndarray, milli_volts: bool = True
    ) -> np.ndarray:
        """
        Extracts the biosignals from the transmitted data.

        Args:
            data (np.ndarray):
                Raw data that got transmitted.

            milli_volts (bool, optional):
                If True, the biosignal data is converted to milli volts.
                Defaults to True.

        Returns:
            np.ndarray:
                Extracted biosignal channels.
        """
        biosignal_data = data[self._biosignal_channel_indices]
        if milli_volts:
            return biosignal_data * self._conversion_factor_biosignal
        return biosignal_data

    def _extract_auxiliary_data(
        self, data: np.ndarray, milli_volts: bool = True
    ) -> np.ndarray:
        """
        Extract auxiliary channels from the transmitted data.

        Args:
            data (np.ndarray):
                Raw data that got transmitted.
            milli_volts (bool, optional):
                If True, the auxiliary data is converted to milli volts.
                Defaults to True.

        Returns:
            np.ndarray:
                Extracted auxiliary channel data.
        """

        if milli_volts:
            return (
                data[self._auxiliary_channel_indices]
                * self._conversion_factor_auxiliary
            )
        return data[self._auxiliary_channel_indices]

    def toggle_connection(self, settings: Tuple[str, int] = None) -> bool:
        """
        Toggles the connection to the device.

        Args:
            settings (Tuple[str, int], optional):
                If CommunicationProtocol.TCPIP:
                Tuple[0] = IP -> string
                Tuple[1] = Port -> int

                If CommunicationProtocol.SERIAL pr CommunicationProtocol.USB:
                Tuple[0] = COM Port -> string
                Tuple[1] = Baudrate -> int

                Defaults to None.

        Returns:
            bool:
                True if connection attempt was successfully. False if not.
        """
        self._connection_settings = settings

        if self.is_connected:
            if self._is_streaming:
                self.toggle_streaming()

            success: bool = self._disconnect_from_device()
        else:
            success: bool = self._connect_to_device()

        return success

    def toggle_streaming(self) -> None:
        """
        Toggles the current state of the streaming.
        If device is streaming, the streaming is stopped and vice versa.
        """
        if self._is_streaming:
            self._stop_streaming()
            self.clear_socket()
        else:
            self._start_streaming()

        self.clear_socket()

    def get_device_information(self) -> Dict[str, Enum | int | float | str]:
        """
        Gets the current configuration of the device.

        Returns:
            Dict[str, Enum | int | float | str]:
                Dictionary that holds information about the
                current device configuration and status.
        """
        return {
            "name": DEVICE_NAME_DICT[self._device_type],
            "sampling_frequency": self._sampling_frequency,
            "number_of_channels": self._number_of_channels,
            "number_of_biosignal_channels": self._number_of_biosignal_channels,
            "number_of_auxiliary_channels": self._number_of_auxiliary_channels,
            "samples_per_frame": self._samples_per_frame,
            "conversion_factor_biosignal": self._conversion_factor_biosignal,
            "conversion_factor_auxiliary": self._conversion_factor_auxiliary,
        }

    def check_valid_ip(self, ip_address: str) -> bool:
        """
        Checks if the provided IP is valid.

        Args:
            ip (str): IP to be checked.

        Returns:
            bool: True if IP is valid. False if not.
        """
        ip_pattern = re.compile(
            r"^([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\."
            r"([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\."
            r"([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\."
            r"([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
        )

        return bool(ip_pattern.match(ip_address))

    def check_valid_port(self, port: str) -> bool:
        """
        Checks if the provided port is valid.

        Args:
            port (str): Port to be checked.

        Returns:
            bool: True if port is valid. False if not.
        """
        try:
            port_num = int(port)
            return 0 <= port_num <= 65535
        except ValueError:
            return False

    def get_server_wifi_ip_address(self) -> list[str]:
        """
        Returns the IP address of the host server.
        """
        try:
            # Get all network interfaces
            interfaces = psutil.net_if_addrs()

            addresses_return = []

            # Iterate through interfaces to find the one associated with WiFi
            for interface, addresses in interfaces.items():
                if (
                    any(keyword in interface.lower() for keyword in ["wlan", "wi-fi", "wifi", "wireless", "en0", "wlp", "wln", "wl"])
                ):
                    for address in addresses:
                        # Check if the address is an IPv4 address and not a loopback or virtual address
                        if (
                            address.family == socket.AF_INET
                            and not address.address.startswith("127.")
                        ):
                            addresses_return.append(address.address)

            return addresses_return[::-1] if addresses_return else [""]

        except Exception as e:
            warn_once("Error occurred while getting server IP address: " + str(e))
            return [""]
