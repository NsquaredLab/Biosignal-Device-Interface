from aenum import Enum, auto

from biosignal_device_interface.constants.devices.core.base_device_constants import (
    DeviceType,
    DeviceChannelTypes,
)


class MuoviWorkingMode(Enum):
    """
    Enum class for the working mode of the Muovi device.

    Note:
        High pass filter implemented by firmware subtracting the exponential moving average, obtained by:
        Average_ChX[t] = (1-alpha) Average_ChX[t-1] + alpha ChX[t]
        Where alpha is equal to 1/25 for MODE = 0, 1 or 2. It is equal to 1/2 in case of Impedance check.
        For the standard modes, this result in a high pass filter with a cut-off frequency of 10.5 Hz, when sampling
        the signals at 2000 Hz. More in general the cut-off frequency is Fsamp/190

    """

    _init_ = "value __doc__"

    NONE = 0, "No working mode set."
    EEG = auto(), "EEG Mode: FSAMP 500 Hz, DC coupled, 24 bit resolution"
    EMG = (
        auto(),
        "EMG Mode: FSAMP 2000 Hz, DC coupled, 16 bit resolution, High pass filtered at 10 Hz",
    )


class MuoviDetectionMode(Enum):
    """
    Enum class for the detection mode of the Muovi device.

    Note:
        Preamp gain of 4 has a double input range and a slightly larger noise w.r.t. preamp gain of 8. It can be
        used when DC component of EMG signals is higher and generates saturation before the high pass filter
        resulting in flat signals. The input range before the high pass filter is +/-600mV when the preamp is set to
        4 and +/-300mV when the preamp is set to 8.
    """

    _init_ = "value __doc__"

    NONE = 0, "No detection mode set."
    MONOPOLAR_GAIN_8 = auto(), (
        "Monopolar Mode.preamp gain 8. 32 monopolar bioelectrical signals + 6 accessory signals. "
        "Resolution is 286.1 nV and range +/-9.375 mV."
    )
    MONOPOLAR_GAIN_4 = auto(), (
        "Monopolar Mode (Only EMG -> EEG=>Mode 0). preamp gain 4. "
        "32 bioelectrical signals + 6 accessory signals. "
        "Resolution is 572.2nV and range +/-18.75 mV."
    )
    IMPEDANCE_CHECK = auto(), "Impedance Check on all 32 + 6 channels."
    TEST = auto(), "Ramps on all 32 + 6 channels."


MUOVI_WORKING_MODE_CHARACTERISTICS_DICT: dict[MuoviWorkingMode, dict[str, int]] = {
    MuoviWorkingMode.EEG: {
        "sampling_frequency": 500,
        "bytes_per_sample": 3,
    },
    MuoviWorkingMode.EMG: {
        "sampling_frequency": 2000,
        "bytes_per_sample": 2,
    },
}
"""
Dictionary to get characteristics of the Muovi working mode.

The keys are the working modes of the Muovi device.

The values are dictionaries with the following keys:
    - "sampling_frequency": The sampling frequency of the working mode in Hz.
    - "bytes_per_sample": The number of bytes per sample.
"""


MUOVI_SAMPLES_PER_FRAME_DICT: dict[DeviceType, dict[MuoviWorkingMode, int]] = {
    DeviceType.OTB_MUOVI: {
        MuoviWorkingMode.EEG: 12,
        MuoviWorkingMode.EMG: 18,
    },
    DeviceType.OTB_MUOVI_PLUS: {
        MuoviWorkingMode.EEG: 6,
        MuoviWorkingMode.EMG: 10,
    },
}
"""
Dictionary to get the frame length of the Muovi.

The keys are the device type of a Muovi (Normal or Plus).

The values are dictionaries with the following keys:
    - MuoviWorkingMode.EEG: The frame length of the EEG working mode
    - MuoviWorkingMode.EMG: The frame length of the EMG working mode.
"""

MUOVI_AVAILABLE_CHANNELS_DICT: dict[DeviceType, dict[DeviceChannelTypes, int]] = {
    DeviceType.OTB_MUOVI: {
        DeviceChannelTypes.ALL: 38,
        DeviceChannelTypes.BIOSIGNAL: 32,
        DeviceChannelTypes.AUXILIARY: 6,
    },
    DeviceType.OTB_MUOVI_PLUS: {
        DeviceChannelTypes.ALL: 70,
        DeviceChannelTypes.BIOSIGNAL: 64,
        DeviceChannelTypes.AUXILIARY: 6,
    },
}

"""

"""

MUOVI_CONVERSION_FACTOR_DICT: dict[MuoviDetectionMode, int] = {
    MuoviDetectionMode.MONOPOLAR_GAIN_8: 572.2e-6,
    MuoviDetectionMode.MONOPOLAR_GAIN_4: 286.1e-6,
}
"""
Dictionary to get the gain of the Muovi detection mode. \\
The keys are the detection modes of the Muovi device. \\
The values are the gain of the detection mode in V.
"""


MUOVI_NETWORK_PORT: int = 54321
"""The default network port of the Muovi device."""
