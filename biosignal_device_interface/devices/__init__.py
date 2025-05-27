# Import Devices to be used from biosignal_device_interface.devices
# import Muovi, MindRoveBracelet, Quattrocento, QuattrocentoLight, ...

# Core device classes
from biosignal_device_interface.devices.core import BaseDevice

# OTB device classes and widgets
from biosignal_device_interface.devices.otb import (
    OTBMuoviWidget,
    OTBMuoviPlusWidget,
    OTBQuattrocentoLightWidget,
    OTBMuovi,
    OTBQuattrocento,
    OTBQuattrocentoLight,
    OTBSyncStationWidget,
    OTBDevicesWidget,
)

# GUI widgets
from biosignal_device_interface.gui.device_template_widgets.all_devices_widget import (
    AllDevicesWidget,
)

__all__ = [
    # Core classes
    "BaseDevice",
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
