"""
Constants for the Sessantaquattro device.

Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2025-09-16
"""

from typing import Dict
from aenum import Enum, auto

from biosignal_device_interface.constants.devices.core.base_device_constants import (
    DeviceChannelTypes,
)


class SessantaquattroSamplingFrequencyMode(Enum):
    """Enum class for the sampling frequency of the Sessantaquattro device."""

    _init_ = "value __doc__"

    NONE = 0, "No sampling frequency set."
    LOW = auto(), "500 Hz (2000 Hz - Accelerometer)"
    MEDIUM = auto(), "1000 Hz (4000 Hz - Accelerometer)"
    HIGH = auto(), "2000 Hz (8000 Hz - Accelerometer)"
    ULTRA = auto(), "4000 Hz (16000 Hz - Accelerometer)"


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
    LOW = auto(), (
        "8 bioelec. + 2 AUX + 2 accessory (if MODE=001: 4 bio + 2 AUX + 2 acc)"
    )
    MEDIUM = auto(), (
        "16 bioelec. + 2 AUX + 2 accessory (if MODE=001: 8 bio + 2 AUX + 2 acc)"
    )
    HIGH = auto(), (
        "32 bioelec. + 2 AUX + 2 accessory (if MODE=001: 16 bio + 2 AUX + 2 acc)"
    )
    ULTRA = auto(), (
        "64 bioelec. + 2 AUX + 2 accessory (if MODE=001: 32 bio + 2 AUX + 2 acc)"
    )


class SessantaquattroResolutionMode(Enum):
    """
    Enum class for the resolution mode of the Sessantaquattro device.
    """

    _init_ = "value __doc__"

    NONE = 0, "No resolution mode set."
    LOW = auto(), ("16 Bits Resolution")
    HIGH = auto(), ("24 Bits Resolution")


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


def _get_sampling_frequency(
    detection_mode: SessantaquattroDetectionMode,
    sampling_freq_mode: SessantaquattroSamplingFrequencyMode,
) -> int:
    """Get sampling frequency for given detection and sampling frequency modes."""
    if detection_mode == SessantaquattroDetectionMode.ACCELEROMETER:
        base_freq = 2000
    else:
        base_freq = 500

    multiplier = 2 ** (sampling_freq_mode.value - 1)
    return base_freq * multiplier


def _get_biosignal_channel_count(
    sampling_freq_mode: SessantaquattroSamplingFrequencyMode,
    detection_mode: SessantaquattroDetectionMode,
) -> int:
    """Get biosignal channel count for given modes."""
    base_channels = 8 * (2 ** (sampling_freq_mode.value - 1))

    # Bipolar mode has half the channels
    if detection_mode == SessantaquattroDetectionMode.BIPOLAR:
        return base_channels // 2

    return base_channels


# Generate dictionaries using functions
SESSANTAQUATTRO_DETECTION_MODE_CHARACTERISTICS_DICT: Dict[
    SessantaquattroDetectionMode, Dict[SessantaquattroSamplingFrequencyMode, int]
] = {
    detection_mode: {
        sampling_freq: _get_sampling_frequency(detection_mode, sampling_freq)
        for sampling_freq in SessantaquattroSamplingFrequencyMode
        if sampling_freq != SessantaquattroSamplingFrequencyMode.NONE
    }
    for detection_mode in SessantaquattroDetectionMode
    if detection_mode != SessantaquattroDetectionMode.NONE
}

SESSANTAQUATTRO_CHANNEL_MODE_CHARACTERISTICS_DICT: Dict[
    SessantaquattroSamplingFrequencyMode,
    Dict[SessantaquattroDetectionMode, Dict[DeviceChannelTypes, int]],
] = {
    sampling_freq: {
        detection_mode: {
            DeviceChannelTypes.BIOSIGNAL: _get_biosignal_channel_count(
                sampling_freq, detection_mode
            ),
            DeviceChannelTypes.AUXILIARY: 4,
        }
        for detection_mode in SessantaquattroDetectionMode
        if detection_mode != SessantaquattroDetectionMode.NONE
    }
    for sampling_freq in SessantaquattroSamplingFrequencyMode
    if sampling_freq != SessantaquattroSamplingFrequencyMode.NONE
}

SESSANTAQUATTRO_GAIN_MODE_CHARACTERISTICS_DICT: Dict[
    SessantaquattroResolutionMode, Dict[SessantaquattroGainMode, float]
] = {
    SessantaquattroResolutionMode.LOW: {
        SessantaquattroGainMode.DEFAULT: 286.1e-6,  # Gain8, 16-bit (in mV, originally 286.1 nV)
        SessantaquattroGainMode.LOW: 572.2e-6,  # Gain4, 16-bit (in mV, originally 572.2 nV)
        SessantaquattroGainMode.MEDIUM: 381.5e-6,  # Gain6, 16-bit (in mV, originally 381.5 nV)
        SessantaquattroGainMode.HIGH: 286.1e-6,  # Gain8, 16-bit (in mV, originally 286.1 nV)
    },
    SessantaquattroResolutionMode.HIGH: {
        SessantaquattroGainMode.DEFAULT: 71.5e-6,  # Gain8, 24-bit (in mV, originally 71.5 nV)
        SessantaquattroGainMode.LOW: 143.0e-6,  # Gain4, 24-bit (in mV, originally 143.0 nV)
        SessantaquattroGainMode.MEDIUM: 95.4e-6,  # Gain6, 24-bit (in mV, originally 95.4 nV)
        SessantaquattroGainMode.HIGH: 71.5e-6,  # Gain8, 24-bit (in mV, originally 71.5 nV)
    },
}

SESSANTAQUATTRO_AUXILIARY_LSB_DICT: Dict[SessantaquattroResolutionMode, float] = {
    SessantaquattroResolutionMode.LOW: 146.48e-6,  # in mV (originally 146.48 nV)
    SessantaquattroResolutionMode.HIGH: 572.2e-6,  # in mV (originally 572.2 nV)
}

SESSANTAQUATTRO_SAMPLES_PER_FRAME_DICT: Dict[SessantaquattroChannelMode, int] = {
    SessantaquattroChannelMode.LOW: 48,
    SessantaquattroChannelMode.MEDIUM: 28,
    SessantaquattroChannelMode.HIGH: 16,
    SessantaquattroChannelMode.ULTRA: 8,
}

if __name__ == "__main__":
    # Print the generated dictionaries for verification
    import pprint

    print("Sessantaquattro Detection Mode Characteristics Dictionary:")
    pprint.pprint(SESSANTAQUATTRO_DETECTION_MODE_CHARACTERISTICS_DICT)

    print("\nSessantaquattro Channel Mode Characteristics Dictionary:")
    pprint.pprint(SESSANTAQUATTRO_CHANNEL_MODE_CHARACTERISTICS_DICT)
