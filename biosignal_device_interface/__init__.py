"""
Biosignal Device Interface
==========================

A Python communication interface for biosignal devices manufactured by several companies,
designed for easy integration in custom PySide6 applications.

This package provides:
- Real-time communication with biosignal acquisition devices
- PySide6-based GUI widgets for device control
- Standardized interface for multiple device types
- Signal processing and data streaming capabilities

Supported Devices
-----------------
- OT Bioelettronica Muovi (32 channels)
- OT Bioelettronica Muovi Plus (64 channels)
- OT Bioelettronica Quattrocento (up to 408 channels)
- OT Bioelettronica Quattrocento Light (up to 64 channels)
- OT Bioelettronica SyncStation

Examples
--------
Basic usage with a single device:

>>> from biosignal_device_interface.devices import OTBMuoviWidget
>>> from PySide6.QtWidgets import QApplication, QMainWindow
>>> 
>>> app = QApplication([])
>>> window = QMainWindow()
>>> device_widget = OTBMuoviWidget(window)
>>> window.setCentralWidget(device_widget)
>>> window.show()
>>> app.exec()

Notes
-----
Authors: Dominik I. Braun <dome.braun@fau.de>, Raul C. Sîmpetru <raul.simpetru@fau.de>
License: CC BY-SA 4.0
Version: 0.3.0a
"""

__version__ = "0.3.0a"
__author__ = "Dominik I. Braun, Raul C. Sîmpetru"
__email__ = "dome.braun@fau.de"
__license__ = "CC BY-SA 4.0"

# Main exports
from biosignal_device_interface.devices import (
    # Device classes
    OTBMuovi,
    OTBQuattrocento,
    OTBQuattrocentoLight,
    
    # Widget classes
    OTBMuoviWidget,
    OTBMuoviPlusWidget,
    OTBQuattrocentoLightWidget,
    OTBSyncStationWidget,
    OTBDevicesWidget,
    AllDevicesWidget,
)

__all__ = [
    # Device classes
    "OTBMuovi",
    "OTBQuattrocento", 
    "OTBQuattrocentoLight",
    
    # Widget classes
    "OTBMuoviWidget",
    "OTBMuoviPlusWidget",
    "OTBQuattrocentoLightWidget",
    "OTBSyncStationWidget",
    "OTBDevicesWidget",
    "AllDevicesWidget",
]
