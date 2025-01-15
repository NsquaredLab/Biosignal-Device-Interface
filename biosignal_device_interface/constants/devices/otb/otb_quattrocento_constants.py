from aenum import Enum, auto

"""
Quattrocento constants.

Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2025-01-14
"""


# ------- Command Byte Sequences --------
class QuattrocentoCommandSequence(Enum):
    """
    Enum class for the different kind of command sequences.
    """

    _init_ = "value __doc__"

    NONE = auto(), "None"
    ACQ_SETT = auto(), "Acquisition settings command sequence"
    AN_OUT_IN_SEL = auto(), "Select input source and gain for the analog output"
    AN_OUT_CH_SEL = auto(), "Select the channel for the analog output source"
    IN_CONF = auto(), (
        "Configuration command sequence for the eight IN inputs or",
        "configuration for the four MULTIPLE IN inputs",
    )
    CRC = auto(), "Configuration command sequence byte (8 bits)"


# ------------ ACQ_SETT BYTE ------------
# Bit 7 is fixed to 1.


class QuattrocentoDecimMode(Enum):
    """
    Enum class for the decimation bit of the Quattrocento device.
    """

    _init_ = "value __doc__"

    INACTIVE = auto(), (
        "Inactive. No decimation. The required sampling",
        "frequency is obtained by sampling the signals",
        "directly at the desired sampling frequency ",
    )
    ACTIVE = auto(), (
        "Active. Decimation active.",
        "The required sampling frequency is obtained by",
        "sampling all the signals at 10240 Hz and then",
        "sending one sample out of 2, 5 or 20, to obtain",
        "the desired number of sample per second.",
    )


class QuattrocentoRecordingMode(Enum):
    """
    Enum class for the recording bit.

    If the Trigger OUT has to be used to synchronize the acquisition with
    other instruments, the recording has to be started when the trigger
    channel has a transition. In other words it is the quattrocento that
    generate a signal indicating to the computer when the data has to be
    recorded.
    """

    _init_ = "value __doc__"

    STOP = auto(), "Stop"
    START = auto(), "Start"


class QuattrocentoSamplingFrequencyMode(Enum):
    """
    Enum class for the sampling frequencies of the Quattrocento device (2 bits).
    """

    _init_ = "value __doc__"

    LOW = auto(), "512 Hz"
    MEDIUM = auto(), "2048 Hz"
    HIGH = auto(), "5120 Hz"
    ULTRA = auto(), "10240 Hz"


class QuattrocentoNumberOfChannelsMode(Enum):
    """
    Enum class for the number of channels of the Quattrocento device (2 bits).
    """

    _init_ = "value __doc__"

    LOW = auto(), "IN1, IN2 and MULTIPLE_IN1 are active."
    MEDIUM = auto(), "IN1-IN4, MULTIPLE_IN1, MULTIPLE_IN2 are active."
    HIGH = auto(), "IN1-IN6, MULTIPLE_IN1-MULTIPLE_IN2 are active."
    ULTRA = auto(), "IN1-IN8, MULTIPLE_IN1-MULTIPLE_IN4 are active."


class QuattrocentoAcquisitionMode(Enum):
    """
    Enum class for the acquisition bit.
    """

    _init_ = "value __doc__"

    INACTIVE = auto(), "Inactive. Data sampling and transfer is not active"
    ACTIVE = auto(), "Active. Data sampling and transfer is active"


class QuattrocentoAcqSettByte:
    """
    Class for the acquisition settings byte of the Quattrocento device.
    """

    def __init__(self):
        self._decimation_mode: QuattrocentoDecimMode = None
        self._recording_mode: QuattrocentoRecordingMode = None
        self._sampling_frequency_mode: QuattrocentoSamplingFrequencyMode = None
        self._sampling_frequency: int = None
        self._number_of_channels_mode: QuattrocentoNumberOfChannelsMode = None
        self._number_of_channels: int = None
        self._acquisition_mode: QuattrocentoAcquisitionMode = (
            QuattrocentoAcquisitionMode
        ).INACTIVE

    def update(
        self,
        decimation_mode: QuattrocentoDecimMode,
        recording_mode: QuattrocentoRecordingMode,
        sampling_frequency_mode: QuattrocentoSamplingFrequencyMode,
        number_of_channels_mode: QuattrocentoNumberOfChannelsMode,
    ):
        self._decimation_mode = decimation_mode
        self._recording_mode = recording_mode
        self._sampling_frequency_mode = sampling_frequency_mode
        self._number_of_channels_mode = number_of_channels_mode

        self._configure()

    def _configure(self):
        self._set_sampling_frequency()
        self._set_number_of_channels()

    def _set_sampling_frequency(self) -> None:
        mode = self._sampling_frequency_mode
        match mode:
            case QuattrocentoSamplingFrequencyMode.LOW:
                self._sampling_frequency = 512
            case QuattrocentoSamplingFrequencyMode.MEDIUM:
                self._sampling_frequency = 2048
            case QuattrocentoSamplingFrequencyMode.HIGH:
                self._sampling_frequency = 5120
            case QuattrocentoSamplingFrequencyMode.ULTRA:
                self._sampling_frequency = 10240
            case _:
                raise ValueError("Invalid sampling frequency mode.")

    def _set_number_of_channels(self) -> None:
        mode = self._number_of_channels_mode
        match mode:
            case QuattrocentoNumberOfChannelsMode.LOW:
                self._number_of_channels = 120
            case QuattrocentoNumberOfChannelsMode.MEDIUM:
                self._number_of_channels = 216
            case QuattrocentoNumberOfChannelsMode.HIGH:
                self._number_of_channels = 312
            case QuattrocentoNumberOfChannelsMode.ULTRA:
                self._number_of_channels = 408
            case _:
                raise ValueError("Invalid number of channels mode.")

    def get_sampling_frequency(self) -> int:
        return self._sampling_frequency

    def get_number_of_channels(self) -> int:
        return self._number_of_channels

    def __int__(self):
        acq_sett_byte = 1 << 7
        acq_sett_byte += (self._decimation_mode.value - 1) << 6
        acq_sett_byte += (self._recording_mode.value - 1) << 5
        acq_sett_byte += (self._sampling_frequency_mode.value - 1) << 3
        acq_sett_byte += (self._number_of_channels_mode.value - 1) << 1
        acq_sett_byte += self._acquisition_mode.value - 1

        return int(acq_sett_byte)


# ---------- AN_OUT_IN_SEL BYTE ----------
# Bit 7 and bit 6 are fixed to 0.
# TODO:

# ---------- AN_OUT_CH_SEL BYTE ----------
# Bit 7 and bit 6 are fixed to 0.
# TODO:

# -- INX_CONF0 and MULTIPLE_INX_CONF0 BYTE --
# Bit 7 is fixed to 0.


class QuattrocentoMuscleSelectionMode(Enum):
    """
    Enum class for the muscle selection mode of the
    Quattrocento device (5 bits).
    """


class QuattrocentoSensorSelectionMode(Enum):
    """
    Enum class for the sensor selection mode of the
    Quattrocento device (5 bits).
    """

    # TODO: "Implement"
    ...


class QuattrocentoSideMode(Enum):
    """"""

    _init_ = "value __doc__"
    UNDEFINED = auto(), "Undefined"
    LEFT = auto(), "Left"
    RIGHT = auto(), "Right"
    NONE = auto(), "None"


# ---------- INX_CONF2 BYTE ----------


class QuattrocentoHighPassFilterMode(Enum):
    """
    Enum class for the high-pass filter of INPUT INX or MULTIPLE INX (2 bits).
    """

    _init_ = "value __doc__"

    NONE = auto(), "No high-pass filter"
    LOW = auto(), "High-pass filter at 0.7 Hz"
    MEDIUM = auto(), "High-pass filter at 10 Hz"
    HIGH = auto(), "High-pass filter at 100 Hz"
    ULTRA = auto(), "High-pass filter at 200 Hz"


class QuattrocentoLowPassFilterMode(Enum):
    """
    Enum class for the low-pass filter of INPUT INX or MULTIPLE INX (2 bits).
    0 -> LOW: 130 Hz
    1 -> MEDIUM: 500 Hz
    2 -> HIGH: 900 Hz
    3 -> ULTRA: 4400 Hz
    """

    _init_ = "value __doc__"

    LOW = auto(), "Low-pass filter at 130 Hz"
    MEDIUM = auto(), "Low-pass filter at 500 Hz"
    HIGH = auto(), "Low-pass filter at 900 Hz"
    ULTRA = auto(), "Low-pass filter at 4400 Hz"


class QuattrocentoDetectionMode(Enum):
    """
    Enum class for the detection mode of the Quattrocento device (2 bits).
    """

    _init_ = "value __doc_"

    NONE = auto(), "No detection"
    MONOPOLAR = auto(), "Monopolar detection"
    BIPOLAR = auto(), "Bipolar detection"


class QuattrocentoINXConf2Byte:
    """
    Class for the INX_CONF2 byte of the Quattrocento device.
    """

    def __init__(self):
        self._muscle_selection_mode: QuattrocentoMuscleSelectionMode = None
        self._sensor_selection_mode: QuattrocentoSensorSelectionMode = None
        self._side_mode: QuattrocentoSideMode = QuattrocentoSideMode.UNDEFINED
        self._high_pass_filter: QuattrocentoHighPassFilterMode = None
        self._low_pass_filter: QuattrocentoLowPassFilterMode = None
        self._detection_mode: QuattrocentoDetectionMode = None

    def update(
        self,
        high_pass_filter: QuattrocentoHighPassFilterMode,
        low_pass_filter: QuattrocentoLowPassFilterMode,
        detection_mode: QuattrocentoDetectionMode,
    ):
        self._high_pass_filter = high_pass_filter
        self._low_pass_filter = low_pass_filter
        self._detection_mode = detection_mode

    def __int__(self):
        input_conf_byte_1 = 0  # TODO: Muscle
        input_conf_byte_2 = 0  # TODO: Sensor + Adapter
        input_conf_byte_3 = (self._side_mode.value - 1) << 6
        input_conf_byte_3 += (self._high_pass_filter.value - 1) << 4
        input_conf_byte_3 += (self._low_pass_filter.value - 1) << 2
        input_conf_byte_3 += self._detection_mode.value - 1

        return int(
            (input_conf_byte_1 << 16) + (input_conf_byte_2 << 8) + input_conf_byte_3
        )


QUATTROCENTO_AUXILIARY_CHANNELS: int = 16
QUATTROCENTO_SUPPLEMENTARY_CHANNELS: int = 8
QUATTROCENTO_SAMPLES_PER_FRAME: int = 64
QUATTROCENTO_BYTES_PER_SAMPLE: int = 2
