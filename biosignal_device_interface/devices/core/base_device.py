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
from PySide6.QtCore import QObject, QByteArray, Signal, QTimer
import numpy as np
import re

# Local Libraries
from biosignal_device_interface.constants.base_device_constants import (
    DeviceType,
    DEVICE_NAME_DICT,
)

# Type Checking
if TYPE_CHECKING:
    # Python Libraries
    from PySide6.QtWidgets import QMainWindow, QWidget
    from PySide6.QtNetwork import QTcpSocket, QUdpSocket
    from PySide6.QtSerialPort import QSerialPort
    from enum import Enum


class BaseDevice(QObject):
    # Signals
    connect_toggled: Signal = Signal(bool)
    configure_toggled: Signal = Signal(bool)
    stream_toggled: Signal = Signal(bool)
    data_arrived: Signal = Signal(np.ndarray)

    def __init__(self, parent: Union[QMainWindow, QWidget] = None, **kwargs) -> None:
        super().__init__(parent)

        # Device Parameters
        self._device_type: DeviceType = DeviceType.DEFAULT

        # Device Information
        self._sampling_frequency: int | None = None
        self._number_of_channels: int | None = None
        self._number_of_biosignal_channels: int | None = None
        self._biosignal_channel_indices: list[int] | None = None
        self._number_of_auxiliary_channels: int | None = None
        self._auxiliary_channel_indices: list[int] | None = None
        self._samples_per_frame: int | None = None

        self._conversion_factor_biosignal: float = None  # Returns mV
        self._conversion_factor_auxiliary: float = None  # Returns mV

        # Connection Parameters
        self._interface: QTcpSocket | QUdpSocket | QSerialPort | None = None
        self._connection_settings: Tuple[str, int] | None = None
        self._buffer_size: int = None
        self._received_bytes: QByteArray = QByteArray()

        self._connection_timeout_timer: QTimer = QTimer()
        self._connection_timeout_timer.setSingleShot(True)
        self._connection_timeout_timer.timeout.connect(self._connection_timeout)
        self._connection_timeout_timer.setInterval(1000)

        # Device Status
        self.is_configured: bool = False
        self.is_connected: bool = False
        self.is_streaming: bool = False

    @abstractmethod
    def _reset_device_parameters(self) -> Dict[str, Union[Enum, Dict[str, Enum]]]:
        """
        Resets the device parameters to Default values.

        Returns:
            Dict[str, Union[Enum, Dict[str, Enum]]]:
                Default values of the device attributes.

                The first one are the attributes (configuration mode) name,
                and the second its respective value.
        """
        ...

    @abstractmethod
    def _connect_to_device(self) -> None:
        """
        Function to attempt a connection to the devices
        """
        ...

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
        ...

    @abstractmethod
    def _connection_timeout(self) -> None:
        """
        Function that is called when the connection timeout is reached.
        """
        ...

    @abstractmethod
    def _disconnect_from_device(self) -> None:
        """
        Closes the connection to the device.

        self.interface closes and is set to None.
        Device state is_connected is set to False.
        Signal connected_signal emits False.
        """
        ...

    @abstractmethod
    def configure_device(self, params: Dict[str, Union[Enum, Dict[str, Enum]]]) -> None:
        """
        Sends a configuration byte sequence based on selected params to the device.
        An overview of possible configurations can be seen in enums/{device}.

        E.g., enums/sessantaquattro.py


        Args:
            params (Dict[str, Union[Enum, Dict[str, Enum]]]):
                Dictionary that holds the configuration settings
                to which the device should be configured to.

                The first one should be the attributes (configuration mode) name,
                and the second its respective value. Orient yourself on the
                enums of the device to choose the correct configuration settings.
        """
        ...

    @abstractmethod
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
        ...

    @abstractmethod
    def get_configuration(self) -> None:
        """
        Sends the command to get the current configuration of the device.
        """
        ...

    @abstractmethod
    def _stop_streaming(self) -> None:
        """
        Sends the command to stop the streaing to the device

        if successful:
            Device state is_streaming is set to False.
            Signal streaming_signal emits False.
        """
        ...

    @abstractmethod
    def _start_streaming(self) -> None:
        """
        Sends the command to start the streaming to the device.

        if successful:
            Device state is_streaming is set to True.
            Signal streaming_signal emits True.
        """
        ...

    @abstractmethod
    def clear_socket(self) -> None:
        """Reads all the bytes from the buffer."""
        ...

    @abstractmethod
    def _read_data(self) -> None:
        """
        This function is called when bytes are ready to be read in the buffer.
        After reading the bytes from the buffer, _process_data is called to
        decode and process the raw data.
        """
        ...

    @abstractmethod
    def _process_data(self, input: QByteArray) -> None:
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
            input (QByteArray):
                Bytearray of the transmitted raw data.
        """
        ...

    def extract_biosignal_data(
        self, data: np.ndarray, milli_volts: bool = False
    ) -> np.ndarray:
        """
        Extracts the biosignals from the transmitted data.

        Args:
            data (np.ndarray):
                Raw data that got transmitted.

            milli_volts (bool, optional):
                If True, the biosignal data is converted to milli volts.
                Defaults to False.

        Returns:
            np.ndarray:
                Extracted biosignal channels.
        """

        if len(self._biosignal_channel_indices) > 0:
            if milli_volts:
                return (
                    data[self._biosignal_channel_indices]
                    * self._conversion_factor_biosignal
                )
            return data[self._biosignal_channel_indices]

    def extract_aux_data(
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
        if len(self._auxiliary_channel_indices) > 0:
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
        self.connection_settings = settings

        if self.is_connected:
            if self.is_streaming:
                self.toggle_streaming()

            success: bool = self._disconnect_from_device()
        else:
            success: bool = self._connect_to_device(settings)

        return success

    def toggle_streaming(self) -> None:
        """
        Toggles the current state of the streaming.
        If device is streaming, the streaming is stopped and vice versa.
        """
        if self.is_streaming:
            self._stop_streaming()
            self.clear_socket()
        else:
            self._start_streaming()

    def reset_configuration(self) -> Dict[str, Union[Enum, dict[str, Enum]]]:
        """
        Resets the current configuration of the device.

        Returns:
            Dict[str, Union[Enum, dict[str, Enum]]]:
                Dictionary that holds the configuration settings
                to which the device should be configured to.

                The first one should be the attributes (configuration mode) name,
                and the second its respective value. Orient yourself on the
                enums of the device to choose the correct configuration settings.
        """
        params = self._reset_device_parameters()
        self.configure_device(params)

        return params

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
                    "wlan" in interface.lower()
                    or "wi-fi" in interface.lower()
                    or "wifi" in interface.lower()
                    or "wireless" in interface.lower()
                    or "en0" in interface.lower()
                ):
                    for address in addresses:
                        # Check if the address is an IPv4 address and not a loopback or virtual address
                        if (
                            address.family == socket.AF_INET
                            and not address.address.startswith("127.")
                        ):
                            addresses_return.append(address.address)

            return addresses_return[::-1] if addresses_return else [""]

        except Exception:
            return [""]
