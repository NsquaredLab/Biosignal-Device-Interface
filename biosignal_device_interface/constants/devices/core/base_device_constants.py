"""
Base Device Constants and Enumerations
======================================

This module defines the core constants, enumerations, and type definitions
used throughout the biosignal device interface package. It provides standardized
device types, channel types, and naming conventions.

The constants defined here ensure consistency across all device implementations
and provide a centralized location for device-related configuration.

Enums:
    DeviceType: Enumeration of all supported device types
    OTBDeviceType: Enumeration of OT Bioelettronica device types
    DeviceChannelTypes: Enumeration of channel types (biosignal, auxiliary, all)

Constants:
    DEVICE_NAME_DICT: Mapping of device types to human-readable names

Author: Dominik I. Braun <dome.braun@fau.de>
Last Update: 2024-06-05
"""

from aenum import Enum, auto


############# ENUMS #############
class DeviceType(Enum):
    """
    Enumeration of all supported biosignal device types.
    
    This enum provides a standardized way to identify different device types
    throughout the package. Each device type includes both a unique identifier
    and a human-readable description.
    
    When adding support for new devices, add the corresponding entry here
    following the naming convention: MANUFACTURER_DEVICENAME.
    
    Attributes:
        OTB_QUATTROCENTO: OT Bioelettronica Quattrocento (up to 408 channels)
        OTB_QUATTROCENTO_LIGHT: OT Bioelettronica Quattrocento Light (up to 64 channels)
        OTB_MUOVI: OT Bioelettronica Muovi (32 channels)
        OTB_MUOVI_PLUS: OT Bioelettronica Muovi Plus (64 channels)
        OTB_SYNCSTATION: OT Bioelettronica SyncStation (synchronization device)
    """

    _init_ = "value __doc__"
    OTB_QUATTROCENTO = auto(), "OT Bioelettronica Quattrocento"
    OTB_QUATTROCENTO_LIGHT = auto(), "OT Bioelettronica Quattrocento Light"
    OTB_MUOVI = auto(), "OT Bioelettronica Muovi"
    OTB_MUOVI_PLUS = auto(), "OT Bioelettronica Muovi Plus"
    OTB_SYNCSTATION = auto(), "OT Bioelettronica SyncStation"


class OTBDeviceType(Enum):
    """
    Enumeration of OT Bioelettronica device types.
    
    This enum specifically covers devices manufactured by OT Bioelettronica,
    providing a more specific categorization for OTB devices.
    
    Attributes:
        QUATTROCENTO: Quattrocento high-density EMG system
        QUATTROCENTO_LIGHT: Quattrocento Light compact EMG system  
        MUOVI: Muovi wireless EMG system (32 channels)
        MUOVI_PLUS: Muovi Plus wireless EMG system (64 channels)
        SYNCSTATION: SyncStation synchronization device
    """

    _init_ = "value __doc__"

    QUATTROCENTO = auto(), "Quattrocento"
    QUATTROCENTO_LIGHT = auto(), "Quattrocento Light"
    MUOVI = auto(), "Muovi"
    MUOVI_PLUS = auto(), "Muovi Plus"
    SYNCSTATION = auto(), "SyncStation"


class DeviceChannelTypes(Enum):
    """
    Enumeration of device channel types.
    
    This enum categorizes the different types of channels available on 
    biosignal devices for data filtering and processing.
    
    Attributes
    ----------
    ALL : auto()
        All channels (biosignal + auxiliary)
    AUXILIARY : auto()
        Auxiliary channels (accelerometer, gyroscope, etc.)
    BIOSIGNAL : auto()
        Biosignal channels (EMG, EEG, etc.)
    """
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
