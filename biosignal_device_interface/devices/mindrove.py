"""
Device class for real-time interfacing the MindRove device.
Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2024-06-05
"""

# Python Libraries
from __future__ import annotations
from enum import Enum
from typing import TYPE_CHECKING, Union, Dict, Tuple
import numpy as np
from PySide6.QtCore import QTimer

# MindRove libraries
from mindrove.board_shim import BoardShim, MindRoveInputParams, BoardIds
from mindrove.data_filter import DataFilter, FilterTypes, DetrendOperations

# Local libraries
from biosignal_device_interface.devices.core.base_device import BaseDevice
from biosignal_device_interface.constants.base_device_constants import DeviceType

if TYPE_CHECKING:
    from PySide6.QtWidgets import QMainWindow, QWidget


class MindRoveBracelet(BaseDevice):
    """
    MindRove Bracelet class derived from BaseDevice class.

    The MindRove Bracelet is a WiFi (TCP/IP) device for recording and stimulating.
    """

    def __init__(
        self,
        parent: Union[QMainWindow, QWidget] = None,
    ) -> None:
        super().__init__(parent)

        # Device Parameters
        self._device_type: DeviceType = DeviceType.MINDROVE_BRACELET

        # Device Information
