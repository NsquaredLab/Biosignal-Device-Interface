"""
Device class for real-time interfacing the Intan RHD Controller device.
Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2024-06-06
"""

# Python Libraries
from __future__ import annotations
from typing import TYPE_CHECKING, Union, Dict, Tuple
from PySide6.QtCore import QByteArray, QIODevice
from PySide6.QtNetwork import QTcpSocket, QHostAddress
import numpy as np
from enum import Enum

# Local Libraries
from biosignal_device_interface.devices.core.base_device import BaseDevice
from biosignal_device_interface.constants.base_device_constants import DeviceType

if TYPE_CHECKING:
    from PySide6.QtWidgets import QMainWindow, QWidget


class IntanRHDRecordingController(BaseDevice):
    """
    Intan RHD Recording Controller device class derived from BaseDevice class.
    The Intan RHD Recording Controller is using a TCP/IP protocol to communicate with the device.
    """

    def __init__(
        self,
        parent: Union[QMainWindow, QWidget] = None,
    ):
        super().__init__(parent)

        # Device Parameters
        self._device_type: DeviceType = DeviceType.INTAN_RHD_RECORDING_CONTROLLER

        # Device Information
        self._samples_per_frame: int = 128  # Fix
        self._conversion_factor_biosignal: float = (
            0.195  # in mV # TODO: Check this value
        )
        self._conversion_factor_auxiliary: float = (
            0.195  # in mV # TODO: Check this value
        )

        # Connection Parameters
        self._interface: QTcpSocket = QTcpSocket()
        self._waveform_interface: QTcpSocket = QTcpSocket()
        self._waveform_port: int = 5001

        self._spike_interface: QTcpSocket = QTcpSocket()
        self._spike_port: int = 5002
