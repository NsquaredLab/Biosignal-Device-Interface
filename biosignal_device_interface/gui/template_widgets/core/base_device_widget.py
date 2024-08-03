"""
Base Device class for real-time interfaces to hardware devices.
Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2024-06-05
"""

# Python Libraries
from __future__ import annotations
from typing import TYPE_CHECKING, Union, Dict
from abc import abstractmethod
from PySide6.QtWidgets import QWidget, QMainWindow

# Import Devices
from biosignal_device_interface.devices.core.base_device import BaseDevice

if TYPE_CHECKING:
    from PySide6.QtCore import Signal
    import numpy as np
    from enum import Enum


class BaseDeviceWidget(QWidget):
    # Signals
    data_arrived: Signal = Signal(np.ndarray)
    biosignal_data_arrived: Signal = Signal(np.ndarray)
    auxiliary_data_arrived: Signal = Signal(np.ndarray)
    connect_toggled: Signal = Signal(bool)
    configure_toggled: Signal = Signal(bool)
    stream_toggled: Signal = Signal(bool)

    def __init__(self, parent: QWidget | QMainWindow | None = None):
        super().__init__(parent)

        self.parent_widget: QWidget | QMainWindow | None = parent

        # Device Setup
        self.device: BaseDevice = BaseDevice()
        self.device_params: Dict[str, Union[str, int, float]] = {}
        self._initialize_device_params()

        self.device.data_available.connect(self.data_arrived.emit)
        self.device.biosignal_data_available.connect(self.biosignal_data_arrived.emit)
        self.device.auxiliary_data_available.connect(self.auxiliary_data_arrived.emit)

    @abstractmethod
    def _toggle_connection(self) -> None:
        """ """
        pass

    @abstractmethod
    def _connection_toggled(self, is_connected: bool) -> None:
        """ """
        self.connect_toggled.emit(is_connected)

    @abstractmethod
    def _toggle_configuration(self) -> None:
        """ """
        pass

    @abstractmethod
    def _configuration_toggled(self, is_configured: bool) -> None:
        """ """
        self.configure_toggled.emit(is_configured)

    @abstractmethod
    def _toggle_stream(self) -> None:
        """ """
        pass

    @abstractmethod
    def _stream_toggled(self, is_streaming: bool) -> None:
        """ """
        self.stream_toggled.emit(is_streaming)

    def get_device_information(self) -> Dict[str, Enum | int | float | str]:
        """
        Gets the current configuration of the device.

        Returns:
            Dict[str, Enum | int | float | str]:
                Dictionary that holds information about the
                current device configuration and status.
        """
        return self.device.get_device_information()

    def _initialize_device_params(self) -> None:
        """ """
        pass
