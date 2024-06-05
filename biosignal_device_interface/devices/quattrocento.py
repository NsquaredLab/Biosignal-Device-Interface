"""
1)  Quattrocento Light class for real-time interface to 
    Quattrocento using OT Biolab Light.

2)  Quattrocento class for direct real-time interface to 
    Quattrocento without using OT Biolab Light.

Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2023-06-05
"""

# Python Libraries
from __future__ import annotations
from typing import TYPE_CHECKING, Union, Dict, Tuple
from PySide6.QtNetwork import QTcpSocket, QHostAddress
from PySide6.QtCore import QIODevice, QByteArray
import numpy as np


from biosignal_device_interface.devices.core.base_device import BaseDevice
from biosignal_device_interface.constants.base_device_constants import DeviceType


if TYPE_CHECKING:
    # Python Libraries
    from PySide6.QtWidgets import QMainWindow, QWidget
    from enum import Enum


class Quattrocento(BaseDevice):
    """
    Quattrocento device class derived from BaseDevice class.

    The Quattrocento class is using a TCP/IP protocol to communicate with the device.
    """

    def __init__(
        self,
        parent: Union[QMainWindow, QWidget] = None,
    ) -> None:
        super().__init__(parent)

        # Device Parameters
        self._device_type: DeviceType = DeviceType.OTB_QUATTROCENTO_LIGHT

        # Device Information
        self._number_of_channels: int = 408  # Fix
        self._number_of_auxiliary_channels: int = 16  # Fix
        self._conversion_factor_biosignal: float = 5 / (2**16) / 150 * 1000
        self._conversion_factor_auxiliary: float = 5 / (2**16) / 0.5

        # Connection Parameters
        self._interface: QTcpSocket = QTcpSocket()


class QuattrocentoLight(BaseDevice):
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
        self._device_type: DeviceType = DeviceType.OTB_QUATTROCENTO

        # Device Information
        self._conversion_factor_biosignal: float = 5 / (2**16) / 150 * 1000
        self._conversion_factor_auxiliary: float = 5 / (2**16) / 0.5

        # Connection Parameters
        self._interface: QTcpSocket = QTcpSocket()
