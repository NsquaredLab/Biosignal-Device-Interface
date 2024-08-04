# Import OTB Devices to be used from biosignal_device_interface.devices
# import Muovi, Quattrocento, QuattrocentoLight, ...

# OTB Devices
from biosignal_device_interface.devices.otb_quattrocento import (
    OTBQuattrocento as Quattrocento,
    OTBQuattrocentoLight as QuattrocentoLight,
)
from biosignal_device_interface.devices.otb_muovi import OTBMuovi as Muovi
