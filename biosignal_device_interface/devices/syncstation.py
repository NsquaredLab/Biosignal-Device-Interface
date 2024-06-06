"""
This module provides a class to interface with the SyncStation device.
Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2023-06-06
"""

# Python Libraries
from __future__ import annotations
from typing import TYPE_CHECKING, Union, Dict, Tuple
from PySide6.QtNetwork import QTcpSocket, QHostAddress
from PySide6.QtCore import QIODevice, QByteArray
import numpy as np

# Local Libraries
from biosignal_device_interface.devices.core.base_device import BaseDevice
from biosignal_device_interface.constants.base_device_constants import DeviceType


if TYPE_CHECKING:
    # Python Libraries
    from PySide6.QtWidgets import QMainWindow, QWidget
    from enum import Enum


class OTBSyncStation(BaseDevice):
    """
    SyncStation device class derived from BaseDevice class.

    The SyncStation class is using a TCP/IP protocol to communicate with the device.
    """

    def __init__(
        self,
        parent: Union[QMainWindow, QWidget] = None,
    ) -> None:
        super().__init__(parent)

        # Device Parameters
        self._device_type: DeviceType = DeviceType.OTB_SYNCSTATION

        # Device Information
        self._number_of_channels: int = 64  # Fix
        self._conversion_factor_biosignal: float = 5 / (2**16) / 0.5
        self._conversion_factor_auxiliary: float = 5 / (2**16) / 0.5

        # Connection Parameters
        self._interface: QTcpSocket = QTcpSocket()
