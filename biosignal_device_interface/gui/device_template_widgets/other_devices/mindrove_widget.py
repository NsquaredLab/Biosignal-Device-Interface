from __future__ import annotations
from typing import TYPE_CHECKING

from biosignal_device_interface.gui.device_template_widgets.core.base_device_widget import (
    BaseDeviceWidget,
)
from biosignal_device_interface.gui.ui_compiled.mindrove_template_widget import (
    Ui_MindroveForm,
)
from biosignal_device_interface.devices.other_devices.mindrove import Mindrove  

if TYPE_CHECKING:
    from PySide6.QtWidgets import (
        QWidget,
        QMainWindow,
        QGroupBox,
        QPushButton,
        QComboBox,
        QLabel,
    )

class MindroveWidget(BaseDeviceWidget):
    def __init__(self, parent: QWidget | QMainWindow | None = None):
        super().__init__(parent)
        self._set_device(Mindrove(parent=self))

    def _toggle_connection(self) -> None:
        self.connect_push_button.setEnabled(False)

        # ✅ Only toggle UI if connection is actually successful
        if self._device._connect_to_device():
            self._connection_toggled(True)
        else:
            self._connection_toggled(False)  # Ensure UI reflects failed connection



    def _connection_toggled(self, is_connected: bool) -> None:
        self.connect_push_button.setEnabled(True)

        if is_connected:
            self.connect_push_button.setText("Disconnect")
            self.connect_push_button.setChecked(True)
            self.configure_push_button.setEnabled(True)  # Only enable if connected
            self.connection_group_box.setEnabled(False)
        else:
            self.connect_push_button.setText("Connect")
            self.connect_push_button.setChecked(False)
            self.configure_push_button.setEnabled(False)  # Disable on failed connection
            self.stream_push_button.setEnabled(False)  # Disable on failed connection
            self.connection_group_box.setEnabled(True)

        self.connect_toggled.emit(is_connected)



    def _toggle_configuration(self) -> None:
        self._device.configure_device(self._device_params)

    def _configuration_toggled(self, is_configured: bool) -> None:
        if is_configured:
            self.stream_push_button.setEnabled(True)

        self.configure_toggled.emit(is_configured)

    def _toggle_stream(self) -> None:
        self.stream_push_button.setEnabled(False)
        self._device.toggle_streaming()

    def _stream_toggled(self, is_streaming: bool) -> None:
        self.stream_push_button.setEnabled(True)
        if is_streaming:
            self.stream_push_button.setText("Stop Streaming")
            self.stream_push_button.setChecked(True)
            self.configure_push_button.setEnabled(False)
        else:
            self.stream_push_button.setText("Stream")
            self.stream_push_button.setChecked(False)
            self.configure_push_button.setEnabled(True)

        self.stream_toggled.emit(is_streaming)

    def _initialize_device_params(self) -> None:
        self._device_params = {}

    def _initialize_ui(self) -> None:
        self.ui = Ui_MindroveForm()
        self.ui.setupUi(self)

        # Command Push Buttons
        self.connect_push_button: QPushButton = self.ui.commandConnectionPushButton
        self.connect_push_button.clicked.connect(self._toggle_connection)
        self._device.connect_toggled.connect(self._connection_toggled)

        self.configure_push_button: QPushButton = self.ui.commandConfigurationPushButton
        self.configure_push_button.clicked.connect(self._toggle_configuration)
        self.configure_push_button.setEnabled(False)
        self._device.configure_toggled.connect(self._configuration_toggled)

        self.stream_push_button: QPushButton = self.ui.commandStreamPushButton
        self.stream_push_button.clicked.connect(self._toggle_stream)
        self.stream_push_button.setEnabled(False)
        self._device.stream_toggled.connect(self._stream_toggled)

        # Connection parameters
        self.connection_group_box: QGroupBox = self.ui.connectionGroupBox
        self.connection_group_box.setVisible(False)