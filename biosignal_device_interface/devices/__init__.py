# Import Devices to be used from biosignal_device_interface.devices
# import Muovi, MindRoveBracelet, Quattrocento, QuattrocentoLight, ...

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

from biosignal_device_interface.gui.device_template_widgets.all_devices_widget import (
    AllDevicesWidget,
)
