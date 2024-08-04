"""
Device class for real-time interfacing the Sessantaquattro (+) device.
Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2023-06-06
"""

# Python Libraries
from __future__ import annotations
from typing import TYPE_CHECKING, Union, Dict, Tuple
from PySide6.QtNetwork import QTcpSocket, QHostAddress
from PySide6.QtCore import QIODevice, QByteArray
from PySide6.QtWidgets import QMainWindow, QWidget
import numpy as np


from biosignal_device_interface.devices.core.base_device import BaseDevice
from biosignal_device_interface.constants.devices.base_device_constants import (
    DeviceType,
)


if TYPE_CHECKING:
    # Python Libraries
    from PySide6.QtWidgets import QMainWindow, QWidget
    from enum import Enum


class OTBSessantaquattro(BaseDevice):
    """
    Sessantaquattro device class derived from BaseDevice class.

    The Sessantaquattro class is using a TCP/IP protocol to communicate with the device.
    """

    def __init__(
        self, parent: QMainWindow | QWidget = None, is_plus: bool = False
    ) -> None:
        super().__init__(parent)

        # Device Parameters
        self.is_plus: bool = is_plus
        self._device_type: DeviceType = (
            DeviceType.OTB_SESSANTAQUATTRO
            if not self.is_plus
            else DeviceType.OTB_SESSANTAQUATTRO_PLUS
        )

        # Device Information
        self._number_of_auxiliary_channels: int = 6  # Fix

        self._conversion_factor_biosignal: float = (
            0.0002861  # in uV #TODO cannot set fixed! Depending on Gain
        )

        # Connection Parameters
        self._interface: QTcpSocket = QTcpSocket()
