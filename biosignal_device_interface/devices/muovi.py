# Python Libraries
"""
Device class for real-time interfacing the Muovi device.
Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2024-06-05
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Union, Dict, Tuple
from PySide6.QtNetwork import QTcpSocket, QTcpServer, QHostAddress
from PySide6.QtCore import QByteArray, QTimer
import numpy as np

# Local Libraries
from biosignal_device_interface.devices.core.base_device import BaseDevice
from biosignal_device_interface.constants.base_device_constants import DeviceType

if TYPE_CHECKING:
    from PySide6.QtWidgets import QMainWindow, QWidget


class Muovi(BaseDevice):
    """
    Muovi device class derived from BaseDevice class.

    Args:
        is_muovi_plus (bool):
            True if the device is a Muovi Plus, False if not.

        parent (Union[QMainWindow, QWidget], optional):
            Parent widget to which the device is assigned to.
            Defaults to None.

    The Muovi class is using a TCP/IP protocol to communicate with the device.
    """

    def __init__(
        self,
        parent: Union[QMainWindow, QWidget] = None,
        is_muovi_plus: bool = False,
    ) -> None:
        """
        Initialize the Muovi device.

        Args:
            parent (Union[QMainWindow, QWidget], optional): Parent widget. Defaults to None.
            is_muovi_plus (bool, optional): Boolean to initialize the Muovi device as Muovi+ (64 biosignal channels) or Muovi (32 biosignal channels). Defaults to False (Muovi).
        """
        super().__init__(parent)

        # Device Parameters
        self._device_type: DeviceType = (
            DeviceType.OTB_MUOVI_PLUS if is_muovi_plus else DeviceType.OTB_MUOVI
        )

        # Device Information
        self._conversion_factor_biosignal: float = (
            0.000286  # TODO: Confirm with OT Bioelettronica (found in communication.py / matlab code) -> Should be flexible depending on the GAIN
        )

        # Connection Parameters
        self._interface: QTcpServer = QTcpServer()
        self._client_socket: QTcpSocket | None = None
