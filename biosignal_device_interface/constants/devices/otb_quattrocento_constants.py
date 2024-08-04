from aenum import Enum, auto


# Quattrocento Light constants
############# COMMANDS #############
COMMAND_START_STREAMING = b"startTX"
COMMAND_STOP_STREAMING = b"stopTX"
CONNECTION_RESPONSE = b"OTBioLab"


############# QUATTROCENTO LIGHT #############
class QuattrocentoLightSamplingFrequency(Enum):
    """
    Enum class for the sampling frequencies of the Quattrocento Light device.
    """

    _init_ = "value __doc__"

    LOW = auto(), "512 Hz"
    MEDIUM = auto(), "2048 Hz"
    HIGH = auto(), "5120 Hz"
    ULTRA = auto(), "10240 Hz"


class QuattrocentoLightStreamingFrequency(Enum):
    """
    Enum class for the streaming frequencies of the Quattrocento Light device.
    """

    _init_ = "value __doc__"

    ONE = auto(), "1 Hz"
    TWO = auto(), "2 Hz"
    FOUR = auto(), "4 Hz"
    EIGHT = auto(), "8 Hz"
    SIXTEEN = auto(), "16 Hz"
    THIRTYTWO = auto(), "32 Hz"


QUATTROCENTO_SAMPLING_FREQUENCY_DICT: dict[QuattrocentoLightSamplingFrequency, int] = {
    QuattrocentoLightSamplingFrequency.LOW: 512,
    QuattrocentoLightSamplingFrequency.MEDIUM: 2048,
    QuattrocentoLightSamplingFrequency.HIGH: 5120,
    QuattrocentoLightSamplingFrequency.ULTRA: 10240,
}
"""
Dictionary to get sampling frequency for each mode.
"""

QUATTROCENTO_LIGHT_STREAMING_FREQUENCY_DICT: dict[
    QuattrocentoLightStreamingFrequency, int
] = {
    QuattrocentoLightStreamingFrequency.ONE: 1,
    QuattrocentoLightStreamingFrequency.TWO: 2,
    QuattrocentoLightStreamingFrequency.FOUR: 4,
    QuattrocentoLightStreamingFrequency.EIGHT: 8,
    QuattrocentoLightStreamingFrequency.SIXTEEN: 16,
    QuattrocentoLightStreamingFrequency.THIRTYTWO: 32,
}
