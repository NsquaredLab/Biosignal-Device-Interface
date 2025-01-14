"""
Base Device class for real-time interfaces to hardware devices.
Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2024-06-05
"""

from aenum import Enum, auto


############# ENUMS #############
class DeviceType(Enum):
    """
    Enum class for the different available devices.
    Add new devices here.
    """

    _init_ = "value __doc__"
    OTB_QUATTROCENTO = auto(), "OT Bioelettronica Quattrocento"
    OTB_QUATTROCENTO_LIGHT = auto(), "OT Bioelettronica Quattrocento Light"
    OTB_MUOVI = auto(), "OT Bioelettronica Muovi"
    OTB_MUOVI_PLUS = auto(), "OT Bioelettronica Muovi Plus"
    OTB_SYNCSTATION = auto(), "OT Bioelettronica SyncStation"


class OTBDeviceType(Enum):
    """
    Enum class for the different available OT Bioelettronica devices.
    Add new devices here.
    """

    _init_ = "value __doc__"

    QUATTROCENTO = auto(), "Quattrocento"
    QUATTROCENTO_LIGHT = auto(), "Quattrocento Light"
    MUOVI = auto(), "Muovi"
    MUOVI_PLUS = auto(), "Muovi Plus"
    SYNCSTATION = auto(), "SyncStation"


class DeviceChannelTypes(Enum):
    _init_ = "value __doc__"

    ALL = auto(), "All"
    AUXILIARY = auto(), "Auxiliary"
    BIOSIGNAL = auto(), "Biosignal"


############# CONSTANTS #############
DEVICE_NAME_DICT: dict[DeviceType | OTBDeviceType, str] = {
    DeviceType.OTB_QUATTROCENTO: "Quattrocento",
    OTBDeviceType.QUATTROCENTO: "Quattrocento",
    DeviceType.OTB_QUATTROCENTO_LIGHT: "Quattrocento Light",
    OTBDeviceType.QUATTROCENTO_LIGHT: "Quattrocento Light",
    DeviceType.OTB_MUOVI: "Muovi",
    OTBDeviceType.MUOVI: "Muovi",
    DeviceType.OTB_MUOVI_PLUS: "Muovi Plus",
    OTBDeviceType.MUOVI_PLUS: "Muovi Plus",
    DeviceType.OTB_SYNCSTATION: "SyncStation",
    OTBDeviceType.SYNCSTATION: "SyncStation",
}
