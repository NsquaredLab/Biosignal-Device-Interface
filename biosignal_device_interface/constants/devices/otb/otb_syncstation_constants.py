"""
Device class for real-time interfacing the OTB Syncstation device.
Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2025-01-09
"""

from typing import Dict, Union
from aenum import Enum, auto
from biosignal_device_interface.constants.devices.core.base_device_constants import (
    DeviceType,
    DeviceChannelTypes,
)
from biosignal_device_interface.constants.devices.otb.otb_muovi_constants import (
    MUOVI_AVAILABLE_CHANNELS_DICT,
)


class SyncStationRecOnMode(Enum):
    """
    Enum class for the recording on mode of the SyncStation device.
    """

    _init_ = "value __doc__"

    OFF = auto(), (
        "The PC is not recording the received signals from SyncStation."
        "If the Timestapms.log is closed if it was previously opened."
    )
    ON = auto(), (
        "The PC is recording the signals received by the SyncStation."
        "When triggered, this bit reset the internal timer for the"
        "ramp counter sent on the Accessory Ch2 and start the log of"
        "the timestamps on the internal timestamps.log file"
    )


class SyncStationWorkingMode(Enum):
    """
    Enum class for the sampling frequency mode of the SyncStation device.
    """

    _init_ = "value __doc__"

    NONE = 0, "No working mode set."
    EEG = auto(), "EEG Mode Fsamp 500 Hz, DC coupled, 24 bit resolution."
    EMG = (
        auto(),
        "EMG Mode Fsamp 2000 Hz, high pass filter at 10 Hz*, 16 bit resolution",
    )


class SyncStationDetectionMode(Enum):
    """
    Enum class for the detection mode of the SyncStation device.
    """

    _init_ = "value __doc__"

    NONE = 0, "No detection mode set."
    MONOPOLAR_GAIN_HIGH = auto(), (
        "Monopolar Mode. High gain. 32 monopolar bioelectrical signals + 6 accessory signals. "
        "Resolution is 286.1 nV and range +/-9.375 mV."
    )
    MONOPOLAR_GAIN_LOW = auto(), (
        "Monopolar Mode. Low gain. 32 monopolar bioelectrical signals + 6 accessory signals. "
        "Resolution is 572.2nV and range +/-18.75 mV."
    )
    IMPEDANCE_CHECK = auto(), "Impedance Check on all 32 + 6 channels."
    TEST = auto(), "Ramps on all 32 + 6 channels."


class SyncStationProbeConfigMode(Enum):
    """
    Enum class for the probe configuration mode of the SyncStation device.
    """

    _init_ = "value __doc__"

    NONE = 0, "No probe configuration mode set."
    MUOVI_PROBE_ONE = auto(), "Probe configuration mode for Muovi probe one."
    MUOVI_PROBE_TWO = auto(), "Probe configuration mode for Muovi probe two."
    MUOVI_PROBE_THREE = auto(), "Probe configuration mode for Muovi probe three."
    MUOVI_PROBE_FOUR = auto(), "Probe configuration mode for Muovi probe four."
    MUOVI_PLUS_PROBE_ONE = auto(), "Probe configuration mode for Muovi Plus probe one."
    MUOVI_PLUS_PROBE_TWO = auto(), "Probe configuration mode for Muovi Plus probe two."
    DUE_PLUS_PROBE_ONE = (
        auto(),
        "Probe configuration mode for Due Plus probe one.",
    )
    DUE_PLUS_PROBE_TWO = (
        auto(),
        "Probe configuration mode for Due Plus probe two.",
    )
    DUE_PLUS_PROBE_THREE = (
        auto(),
        "Probe configuration mode for Due Plus probe three.",
    )
    DUE_PLUS_PROBE_FOUR = (
        auto(),
        "Probe configuration mode for Due Plus probe four.",
    )
    DUE_PLUS_PROBE_FIVE = (
        auto(),
        "Probe configuration mode for Due Plus probe five.",
    )
    DUE_PLUS_PROBE_SIX = (
        auto(),
        "Probe configuration mode for Due Plus probe six.",
    )
    DUE_PLUS_PROBE_SEVEN = (
        auto(),
        "Probe configuration mode for Due Plus probe seven.",
    )
    DUE_PLUS_PROBE_EIGHT = (
        auto(),
        "Probe configuration mode for Due Plus probe eight.",
    )
    DUE_PLUS_PROBE_NINE = (
        auto(),
        "Probe configuration mode for Due Plus probe nine.",
    )
    DUE_PLUS_PROBE_TEN = (
        auto(),
        "Probe configuration mode for Due Plus probe ten.",
    )


# DICTS

SYNCSTATION_CHARACTERISTICS_DICT: Dict[str, int] = {
    DeviceChannelTypes.ALL: 6,
    "bytes_per_sample": 2,
    "channel_information": {
        SyncStationWorkingMode.EEG: {
            "sampling_frequency": 500,
            "bytes_per_sample": 3,
            "frame_size": 5,
        },
        SyncStationWorkingMode.EMG: {
            "sampling_frequency": 2000,
            "bytes_per_sample": 2,
            "frame_size": 10,
        },
    },
    "number_of_packages": 32,
    "package_size": 1460,
    "FPS": 50,
}

#  TODO: Load information from Device Constants directly!
PROBE_CHARACTERISTICS_DICT: Dict[
    SyncStationProbeConfigMode, Dict[str, Union[str, int]]
] = {
    SyncStationProbeConfigMode.MUOVI_PROBE_ONE: MUOVI_AVAILABLE_CHANNELS_DICT[
        DeviceType.OTB_MUOVI
    ],
    SyncStationProbeConfigMode.MUOVI_PROBE_TWO: MUOVI_AVAILABLE_CHANNELS_DICT[
        DeviceType.OTB_MUOVI
    ],
    SyncStationProbeConfigMode.MUOVI_PROBE_THREE: MUOVI_AVAILABLE_CHANNELS_DICT[
        DeviceType.OTB_MUOVI
    ],
    SyncStationProbeConfigMode.MUOVI_PROBE_FOUR: MUOVI_AVAILABLE_CHANNELS_DICT[
        DeviceType.OTB_MUOVI
    ],
    SyncStationProbeConfigMode.MUOVI_PLUS_PROBE_ONE: MUOVI_AVAILABLE_CHANNELS_DICT[
        DeviceType.OTB_MUOVI_PLUS
    ],
    SyncStationProbeConfigMode.MUOVI_PLUS_PROBE_TWO: MUOVI_AVAILABLE_CHANNELS_DICT[
        DeviceType.OTB_MUOVI_PLUS
    ],
    SyncStationProbeConfigMode.DUE_PLUS_PROBE_ONE: {
        DeviceChannelTypes.ALL: 8,
        DeviceChannelTypes.BIOSIGNAL: 2,
        DeviceChannelTypes.AUXILIARY: 6,
    },
    SyncStationProbeConfigMode.DUE_PLUS_PROBE_TWO: {
        DeviceChannelTypes.ALL: 8,
        DeviceChannelTypes.BIOSIGNAL: 2,
        DeviceChannelTypes.AUXILIARY: 6,
    },
    SyncStationProbeConfigMode.DUE_PLUS_PROBE_THREE: {
        DeviceChannelTypes.ALL: 8,
        DeviceChannelTypes.BIOSIGNAL: 2,
        DeviceChannelTypes.AUXILIARY: 6,
    },
    SyncStationProbeConfigMode.DUE_PLUS_PROBE_FOUR: {
        DeviceChannelTypes.ALL: 8,
        DeviceChannelTypes.BIOSIGNAL: 2,
        DeviceChannelTypes.AUXILIARY: 6,
    },
    SyncStationProbeConfigMode.DUE_PLUS_PROBE_FIVE: {
        DeviceChannelTypes.ALL: 8,
        DeviceChannelTypes.BIOSIGNAL: 2,
        DeviceChannelTypes.AUXILIARY: 6,
    },
    SyncStationProbeConfigMode.DUE_PLUS_PROBE_SIX: {
        DeviceChannelTypes.ALL: 8,
        DeviceChannelTypes.BIOSIGNAL: 2,
        DeviceChannelTypes.AUXILIARY: 6,
    },
    SyncStationProbeConfigMode.DUE_PLUS_PROBE_SEVEN: {
        DeviceChannelTypes.ALL: 8,
        DeviceChannelTypes.BIOSIGNAL: 2,
        DeviceChannelTypes.AUXILIARY: 6,
    },
    SyncStationProbeConfigMode.DUE_PLUS_PROBE_EIGHT: {
        DeviceChannelTypes.ALL: 8,
        DeviceChannelTypes.BIOSIGNAL: 2,
        DeviceChannelTypes.AUXILIARY: 6,
    },
    SyncStationProbeConfigMode.DUE_PLUS_PROBE_NINE: {
        DeviceChannelTypes.ALL: 8,
        DeviceChannelTypes.BIOSIGNAL: 2,
        DeviceChannelTypes.AUXILIARY: 6,
    },
    SyncStationProbeConfigMode.DUE_PLUS_PROBE_TEN: {
        DeviceChannelTypes.ALL: 8,
        DeviceChannelTypes.BIOSIGNAL: 2,
        DeviceChannelTypes.AUXILIARY: 6,
    },
}

SYNCSTATION_CONVERSION_FACTOR_DICT: dict[SyncStationDetectionMode, int] = {
    SyncStationDetectionMode.MONOPOLAR_GAIN_HIGH: 572.2e-6,
    SyncStationDetectionMode.MONOPOLAR_GAIN_LOW: 286.1e-6,
}
"""
Dictionary to get the gain of the Muovi detection mode. \\
The keys are the detection modes of the Muovi device. \\
The values are the gain of the detection mode in V.
"""
