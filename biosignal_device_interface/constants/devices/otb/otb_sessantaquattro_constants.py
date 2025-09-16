"""
Constants for the Sessantaquattro device.

Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2025-09-16
"""

from aenum import Enum, auto

from biosignal_device_interface.constants.devices.core.base_device_constants import (
    DeviceType,
    DeviceChannelTypes,
)


class SessantaquattroActionMode(Enum):
    """
    Enum class for the action mode of the Sessantaquattro device.
    """

    _init_ = "value __doc__"

    NONE = 0, "No action mode set."
    SET = auto(), "Set the parameters of the device."
    GET = auto(), "Get the parameters of the device."


class SessantaquattroSamplingFrequencyMode(Enum):
    """Enum class for the sampling frequency of the Sessantaquattro device."""

    _init_ = "value __doc__"

    NONE = 0, "No sampling frequency set."
    LOW = auto(), "Low Sampling Frequency"
    MEDIUM = auto(), "Medium Sampling Frequency"
    HIGH = auto(), "High Sampling Frequency"
    ULTRA = auto(), "Ultra Sampling Frequency"


class SessantaquattroDetectionMode(Enum):
    """
    Enum class for the working mode of the Sessantaquattro device.
    """

    _init_ = "value __doc__"

    NONE = 0, "No working mode set."
    MONOPOLAR = auto(), ("Monopolar Mode")
    BIPOLAR = auto(), ("Bipolar Mode")
    DIFFERENTIAL = auto(), ("Differential Mode")
    ACCELEROMETER = auto(), ("Accelerometer Mode")
    UNDEFINED = auto(), ("Undefined Mode")
    IMPEDANCE_ADVANCED = auto(), ("Impedance Check Advanced")
    IMPEDANCE = auto(), ("Impedance Check")
    TEST = auto(), ("Test Mode")


class SessantaquattroChannelMode(Enum):
    """
    Enum class for the channel mode of the Sessantaquattro device.
    """

    _init_ = "value __doc__"

    NONE = 0, "No channel mode set."
    LOW = auto(), ("Low Channel Mode")
    MEDIUM = auto(), ("Medium Channel Mode")
    HIGH = auto(), ("High Channel Mode")
    ULTRA = auto(), ("Ultra Channel Mode")


class SessantaquattroResolutionMode(Enum):
    """
    Enum class for the resolution mode of the Sessantaquattro device.
    """

    _init_ = "value __doc__"

    NONE = 0, "No resolution mode set."
    LOW = auto(), ("16 Bits Resolution")
    HIGH = auto(), ("24 Bits Resolution")


class SessantaquattroFilterMode(Enum):
    """
    Enum class for the filter mode of the Sessantaquattro device.
    """

    _init_ = "value __doc__"

    NONE = 0, "No filter mode set."
    OFF = auto(), ("High Pass Filter Off")
    ON = auto(), ("High Pass Filter On")


class SessantaquattroGainMode(Enum):
    """
    Enum class for the gain mode of the Sessantaquattro device.
    """

    _init_ = "value __doc__"

    NONE = 0, "No gain mode set."
    DEFAULT = auto(), (
        "Gain x2 (for 24 bits resolution) / Gain x8 (for 16 bits resolution)"
    )
    LOW = auto(), ("Gain x4")
    MEDIUM = auto(), ("Gain x6")
    HIGH = auto(), ("Gain x8")


class SessantaquattroTriggerMode(Enum):
    """
    Enum class for the trigger mode of the Sessantaquattro device.
    """

    _init_ = "value __doc__"

    NONE = 0, "No trigger mode set."
    DEFAULT = auto(), (
        "The data transfer is controlled from GO/STOP bit, REC has no effect."
    )
    INTERNAL = auto(), (
        "The data transfer ist triggered by the internal signal (phototransistor)"
    )
    EXTERNAL = auto(), (
        "The data transfer is triggered by the external signal (from the adapter)"
    )
    SDCARD = auto(), (
        "SDCARD: SD card acquisition starts/stops with the hardware button or with the REC bit."
    )


class SessantaquattroRecordingMode(Enum):
    """
    Enum class for the recording mode of the Sessantaquattro device.
    """

    _init_ = "value __doc__"

    NONE = 0, "No recording mode set."
    STOP = auto(), ("Stop the recording. Works only if TRIG = 3 (SDCARD).")
    START = auto(), ("Start the recording. Works only if TRIG = 3 (SDCARD).")


class SessantoquattroTransmissionMode(Enum):
    """
    Enum class for the transmission mode of the Sessantaquattro device.
    """

    _init_ = "value __doc__"

    NONE = 0, "No transmission mode set."
    OFF = auto(), ("No data transmission.")
    ON = auto(), ("Data transmission active.")


SESSANTAQUATTRO_DETECTION_MODE_CHARACTERISTICS_DICT: dict[
    SessantaquattroDetectionMode, dict[SessantaquattroSamplingFrequencyMode, int]
] = {
    SessantaquattroDetectionMode.MONOPOLAR: {
        SessantaquattroSamplingFrequencyMode.LOW: 500
    },
    SessantaquattroDetectionMode.BIPOLAR: {
        SessantaquattroSamplingFrequencyMode.LOW: 500
    },
    SessantaquattroDetectionMode.DIFFERENTIAL: {
        SessantaquattroSamplingFrequencyMode.LOW: 500
    },
    SessantaquattroDetectionMode.ACCELEROMETER: {
        SessantaquattroSamplingFrequencyMode.LOW: 2000
    },
    SessantaquattroDetectionMode.UNDEFINED: {
        SessantaquattroSamplingFrequencyMode.LOW: 500
    },
    SessantaquattroDetectionMode.IMPEDANCE_ADVANCED: {
        SessantaquattroSamplingFrequencyMode.LOW: 500
    },
    SessantaquattroDetectionMode.IMPEDANCE: {
        SessantaquattroSamplingFrequencyMode.LOW: 500
    },
    SessantaquattroDetectionMode.TEST: {SessantaquattroSamplingFrequencyMode.LOW: 500},
}
