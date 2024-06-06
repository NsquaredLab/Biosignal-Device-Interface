# Import OTB Devices to be used from biosignal_device_interface.devices
# import Muovi, Quattrocento, QuattrocentoLight, ...

# OTB Devices
from biosignal_device_interface.devices.quattrocento import (
    OTBQuattrocento as Quattrocento,
    OTBQuattrocentoLight as QuattrocentoLight,
)
from biosignal_device_interface.devices.muovi import OTB_Muovi as Muovi
from biosignal_device_interface.devices.syncstation import (
    OTBSyncStation as SyncStation,
)
from biosignal_device_interface.devices.sessantaquattro import (
    OTBSessantaquattro as Sessantaquattro,
)
