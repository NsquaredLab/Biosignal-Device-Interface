"""
Base Device class for real-time interfaces to hardware devices.
Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2024-06-05
"""

from enum import Enum, auto


############# ENUMS #############
class DeviceType(Enum):
    OTB_QUATTROCENTO = auto()
    OTB_QUATTROCENTO_LIGHT = auto()
    OTB_SESSANTAQUATTRO = auto()
    OTB_SESSANTAQUATTRO_PLUS = auto()
    OTB_SYNCSTATION = auto()
    OTB_MUOVI = auto()
    OTB_MUOVI_PLUS = auto()
    INTAN_RHD_CONTROLLER = auto()
    MINDROVE_BRACELET = auto()
    DEFAULT = auto()


class OTBDeviceType(Enum):
    QUATTROCENTO = auto()
    QUATTROCENTO_LIGHT = auto()
    SESSANTAQUATTRO = auto()
    SESSANTAQUATTRO_PLUS = auto()
    SYNCSTATION = auto()
    MUOVI = auto()
    MUOVI_PLUS = auto()


############# CONSTANTS #############
DEVICE_NAME_DICT: dict[DeviceType | OTBDeviceType, str] = {
    DeviceType.OTB_QUATTROCENTO: "Quattrocento",
    OTBDeviceType.QUATTROCENTO: "Quattrocento",
    DeviceType.OTB_QUATTROCENTO_LIGHT: "Quattrocento Light",
    OTBDeviceType.QUATTROCENTO_LIGHT: "Quattrocento Light",
    DeviceType.OTB_SESSANTAQUATTRO: "Sessantaquattro",
    OTBDeviceType.SESSANTAQUATTRO: "Sessantaquattro",
    DeviceType.OTB_SESSANTAQUATTRO_PLUS: "Sessantaquattro Plus",
    OTBDeviceType.SESSANTAQUATTRO_PLUS: "Sessantaquattro Plus",
    DeviceType.OTB_SYNCSTATION: "SyncStation",
    OTBDeviceType.SYNCSTATION: "SyncStation",
    DeviceType.OTB_MUOVI: "Muovi",
    OTBDeviceType.MUOVI: "Muovi",
    DeviceType.OTB_MUOVI_PLUS: "Muovi Plus",
    OTBDeviceType.MUOVI_PLUS: "Muovi Plus",
    DeviceType.INTAN_RHD_CONTROLLER: "Intan RHD Controller",
    DeviceType.MINDROVE_BRACELET: "MindRove Bracelet",
    DeviceType.DEFAULT: "Default Device",
}
