"""
Integrating a device in your own software.
================================
"""

# %% Implementation of a custom device into the Biosignal-Device-Interface package.


# %% Step 1: Implement the device.
#
# %% Step 1.1: Add device type to the DeviceType Enum in biosignal_device_interface.constants.devices.base_device_constants.py.
from aenum import Enum, auto


class DeviceType(Enum):
    """
    Enum class for the different available devices.
    Add new devices here.
    """

    _init_ = "value __doc__"
    OTB_QUATTROCENTO_LIGHT = auto(), "OT Bioelettronica Quattrocento Light"
    OTB_MUOVI = auto(), "OT Bioelettronica Muovi"
    OTB_MUOVI_PLUS = auto(), "OT Bioelettronica Muovi Plus"
    # Add new device here
    MANU_MYNAMEDEVICE = auto(), "Manufacturer MyNameDevice"


# %% Step 1.2: Create a new Python file in the biosignal_device_interface/devices/ directory.
# The file name should be the name of the manufacturer and the device, e.g., manu_mydevicename.py.
# The file should contain the device class that inherits from the BaseDevice class.
from __future__ import annotations
from typing import TYPE_CHECKING, Union, Dict
from biosignal_device_interface.devices.core.base_device import BaseDevice
from biosignal_device_interface.constants.devices.base_device_constants import (
    DeviceType,
)

if TYPE_CHECKING:
    from PySide6.QtWidgets import QMainWindow, QWidget
    from PySide6.QtNetwork import QTcpServer, QTcpSocket, QUdpSocket
    from PySide6.QtSerialPort import QSerialPort
    from aenum import Enum


class MANUMyNameDevice(BaseDevice):
    def __init__(self, parent: Union[QMainWindow, QWidget] = None) -> None:
        super().__init__(parent)
        self._device_type: DeviceType = DeviceType.MANU_MYNAMEDEVICE

        # Device Information
        # TODO: Add fixed device information here

        # Connection Parameters -> Add parameters that are needed to connect to the device.
        # self._interface is the variable that either server sockets or client socket or a serial connection.
        # If self._interface serves as a server socket, a self._client_socket variable should be added.

        self._interface: QTcpServer | QTcpSocket | QUdpSocket | QSerialPort | None = (
            None
        )
        # Optional
        self._client_socket: QTcpSocket | QUdpSocket | None = None

        # Configuration parameters
        # TODO: Add configuration parameters here
        # Example:
        self._sampling_frequency_mode: Enum | None = None


# ..note:: Import your device class in the __init__.py file in the biosignal_device_interface/devices/ directory for more accessible imports.


# %% Step 1.3: Implement the abstract methods of the BaseDevice class.
# Some methods need to call the super() method.
class MANUMyNameDevice(BaseDevice):
    def __init__(self, parent: Union[QMainWindow, QWidget] = None) -> None:
        super().__init__(parent)
        # See Step 1.2

    def _connect_to_device(self) -> bool:
        pass

    def _make_request(self) -> bool:
        pass

    def _disconnect_from_device(self) -> bool:
        super()._disconnect_from_device()

    def configure_device(self, params: Dict[str, Union[Enum, Dict[str, Enum]]]) -> None:
        super().configure_device(params)

    def _start_streaming(self) -> None:
        super()._start_streaming()

    def _stop_streaming(self) -> None:
        super()._stop_streaming()

    def clear_socket(self) -> None:
        pass

    def _read_data(self) -> None:
        pass

    def _process_data(self, input: bytearray) -> None:
        pass


# %% Step 1.4: Emit the necessary signals in the device class.
# By inheriting from the BaseDevice class, the new device class has to emit the following Signals:
#
# - data_arrived: Signal = Signal(np.ndarray) -> Emitted when new data (all channels) is available. Typically emitted in _process_data.
# - biosignal_data_arrived: Signal = Signal(np.ndarray) -> Emitted when new biosignal data is available. Typically emitted in _process_data.
# - auxiliary_data_arrived: Signal = Signal(np.ndarray) -> Emitted when new auxiliary data is available. Typically emitted in _process_data.
#
# - connect_toggled: Signal = Signal(bool) -> Emitted when the connection state of the device changes.
#                                             Typically emitted in _make_request and _disconnect_from_device (_disconnect_from_device is already implemented).
#                                             Emit could also be happen in _read_data when response from device is validating connection.
# - configure_toggled: Signal = Signal(bool) -> Emitted when the configuration state of the device changes. Typically emitted in configure_device.
# - stream_toggled: Signal = Signal(bool) -> Emitted when the streaming state of the device changes. Typically emitted in _start_streaming and _stop_streaming.
#                                            Both are already implemented.
#
# %% Step 1.5: Implement the device configuration parameters as enums and use dictionaries to get correct values.
# Regarding the different configuration options, enums and dictionaries should be used to define the possible values.
# These constants should be defined in biosignal_device_interface/constants/devices/manu_mydevicename_constants.py.
#
# Example: Quattrocento Light device configuration parameters
class MyNameDeviceSamplingFrequency(Enum):
    """
    Enum class for the sampling frequencies of the Quattrocento Light device.
    """

    _init_ = "value __doc__"

    LOW = auto(), "512 Hz"
    MEDIUM = auto(), "2048 Hz"
    HIGH = auto(), "5120 Hz"
    ULTRA = auto(), "10240 Hz"


MY_NAME_DEVICE_SAMPLING_FREQUENCY_DICT: dict[MyNameDeviceSamplingFrequency, int] = {
    MyNameDeviceSamplingFrequency.LOW: 512,
    MyNameDeviceSamplingFrequency.MEDIUM: 2048,
    MyNameDeviceSamplingFrequency.HIGH: 5120,
    MyNameDeviceSamplingFrequency.ULTRA: 10240,
}
"""
Dictionary to get sampling frequency for each mode.
"""

# How to use that in configure_device(self, params: Dict[str, Union[Enum, Dict[str, Enum]]]) -> None:
# Example params (should be defined in your software or using the template_widgets):
# .. note:: Even though the configuration parameter is initialized as a private variable with self._my_param, do not use the underscore in the dictionary key.
params = {
    "sampling_frequency_mode": MyNameDeviceSamplingFrequency.LOW,
}


class MANUMyNameDevice(BaseDevice):
    def __init__(self, parent: Union[QMainWindow, QWidget] = None) -> None:
        super().__init__(parent)
        # See Step 1.2

        # Configuration parameters
        self._sampling_frequency_mode: Enum | None = None

    def configure_device(self, params: Dict[str, Union[Enum, Dict[str, Enum]]]) -> None:
        # Super call automatically sets the parameters to your device attributes.
        super().configure_device(params)

        # Get the actual value of your configuration mode from the dictionary
        self._sampling_frequency = MY_NAME_DEVICE_SAMPLING_FREQUENCY_DICT[
            self._sampling_frequency_mode
        ]


# %% Step 1.6: Implement additional methods that you might need which are unique for your device.
# Typically such methods are needed to properly decode the data from the device.

# %% Step 2: Desing the graphical user interface in PySide6.
# Preferably, design the GUI in Qt Designer and compile it to a Python file afterwards.
# The QT Designer file should be saved in the biosignal_device_interface/gui/ui/ directory.
# The compiled .py file should be saved in the biosignal_device_interface/gui/ui_compiled/ directory.

# %% Step 3: Implement the device widget.
# The device widget is the graphical representation of the device in the Biosignal-Device-Interface.
# The device widget should inherit from the BaseDeviceWidget class.
# The device widget file should be implemented in the biosignal_device_interface/gui/device_template_widgets/ directory.
# The device widget file should be implemented with the name of the manufacturer and the device, e.g., manu_mydevicename_widget.

# %% Step 3.1: Implement the device widget.
# Import the necessary libraries and classes.
from __future__ import annotations
from typing import TYPE_CHECKING

from biosignal_device_interface.gui.device_template_widgets.core.base_device_widget import (
    BaseDeviceWidget,
)

# TODO: Import the compiled UI file from the biosignal_device_interface/gui/ui_compiled/ directory.
from biosignal_device_interface.gui.ui_compiled.manu_mydevicename_widget import (
    Ui_MyDeviceNameForm,
)

# TODO: Import the device class from the biosignal_device_interface/devices/ directory.
from biosignal_device_interface.devices import MANUMyNameDevice

# Constants
# TODO: Implement your device constants here

if TYPE_CHECKING:
    from PySide6.QtWidgets import (
        QMainWindow,
        QWidget,
        QGroupBox,
        QPushButton,
        QComboBox,
        QLabel,
    )


# The device widget should inherit from the BaseDeviceWidget class.
# The device widget should implement the necessary methods to connect, configure, and stream the device.
class MANUMyNameDeviceWidget(BaseDeviceWidget):
    def __init__(self, parent: QWidget | QMainWindow | None = None):
        super().__init__(parent)
        # Set the device to the device widget
        self._set_device(MANUMyNameDevice(parent=self))

    def _toggle_connection(self) -> None:
        # TODO: Call self.device.toggle_connection() with the necessary connection parameters.
        pass

    def _connection_toggled(self, is_connected: bool) -> None:
        # Implement the connection toggled method that is called when the connection state changes.
        pass

    def _toggle_configuration(self) -> None:
        # TODO: Call self.device.configure_device(self._device_params) with the necessary configuration parameters.
        # Get the configuration parameters from the UI.
        # QComboBox recommended for multiple options.
        pass

    def _configuration_toggled(self, is_configured: bool) -> None:
        # Implement the configuration toggled method that is called when the configuration state changes.
        pass

    def _toggle_streaming(self) -> None:
        # TODO: Call self.device.toggle_streaming().
        pass

    def _streaming_toggled(self, is_streaming: bool) -> None:
        # Implement the streaming toggled method
        pass

    def _initialize_device_params(self) -> None:
        # Example: Set the default sampling frequency mode
        self._device_params = {
            "sampling_frequency_mode": MyNameDeviceSamplingFrequency.MEDIUM
        }

    def _initialize_ui(self) -> None:
        # Instantiate your UI class and set it up
        self.ui = Ui_MyDeviceNameForm()
        self.ui.setupUi(self)

        # TODO: Implement the necessary UI elements and link their signals here.


# %% Step 3.2: Implement the device widget in the __init__.py file in the biosignal_device_interface/gui/device_template_widgets/ directory.

# %% Step 3.3: Add the device widget to the AllDevicesWidget and the respective ManufacturerDeviceWidget.

# %% Step 4: Run example 3_integrating_device_interfaces_and_biosignal_plot.py to test your device widget and the transmitted signals.
