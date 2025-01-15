from __future__ import annotations
from typing import TYPE_CHECKING

from biosignal_device_interface.gui.device_template_widgets.core.base_device_widget import (
    BaseDeviceWidget,
)
from biosignal_device_interface.gui.ui_compiled.otb_muovi_template_widget import (
    Ui_MuoviForm,
)
from biosignal_device_interface.devices.otb.otb_muovi import OTBMuovi

# Constants
from biosignal_device_interface.constants.devices.otb.otb_muovi_constants import (
    MuoviWorkingMode,
    MuoviDetectionMode,
    MUOVI_NETWORK_PORT,
)

if TYPE_CHECKING:
    from PySide6.QtWidgets import (
        QWidget,
        QMainWindow,
        QGroupBox,
        QPushButton,
        QComboBox,
        QLabel,
    )


class OTBMuoviWidget(BaseDeviceWidget):
    def __init__(self, parent: QWidget | QMainWindow | None = None):
        super().__init__(parent)

        self._set_device(OTBMuovi(parent=self))

    def _toggle_connection(self) -> None:
        if not self._device.is_connected:
            self.connect_push_button.setEnabled(False)

        self._device.toggle_connection(
            (
                self.connection_ip_combo_box.currentText(),
                int(self.connection_port_label.text()),
            )
        )

    def _connection_toggled(self, is_connected: bool) -> None:
        self.connect_push_button.setEnabled(True)
        if is_connected:
            self.connect_push_button.setText("Disconnect")
            self.connect_push_button.setChecked(True)
            self.configure_push_button.setEnabled(True)
            self.connection_group_box.setEnabled(False)
        else:
            self.connect_push_button.setText("Connect")
            self.connect_push_button.setChecked(False)
            self.configure_push_button.setEnabled(False)
            self.stream_push_button.setEnabled(False)
            self.connection_group_box.setEnabled(True)

        self.connect_toggled.emit(is_connected)

    def _toggle_configuration(self) -> None:
        self._device_params["working_mode"] = MuoviWorkingMode(
            self.input_working_mode_combo_box.currentIndex() + 1
        )
        self._device_params["detection_mode"] = MuoviDetectionMode(
            self.input_detection_mode_combo_box.currentIndex() + 1
        )

        self._device.configure_device(self._device_params)

    def _configuration_toggled(self, is_configured: bool) -> None:
        if is_configured:
            self.stream_push_button.setEnabled(True)

        self.configure_toggled.emit(is_configured)

    def _toggle_configuration_group_boxes(self) -> None:
        for group_box in self.configuration_group_boxes:
            group_box.setEnabled(not group_box.isEnabled())

    def _toggle_stream(self) -> None:
        self.stream_push_button.setEnabled(False)
        self._device.toggle_streaming()

    def _stream_toggled(self, is_streaming: bool) -> None:
        self.stream_push_button.setEnabled(True)
        if is_streaming:
            self.stream_push_button.setText("Stop Streaming")
            self.stream_push_button.setChecked(True)
            self.configure_push_button.setEnabled(False)
            self._toggle_configuration_group_boxes()
        else:
            self.stream_push_button.setText("Stream")
            self.stream_push_button.setChecked(False)
            self.configure_push_button.setEnabled(True)
            self._toggle_configuration_group_boxes()

        self.stream_toggled.emit(is_streaming)

    def _initialize_device_params(self) -> None:
        self._device_params = {
            "working_mode": MuoviWorkingMode.EMG,
            "detection_mode": MuoviDetectionMode.MONOPOLAR_GAIN_8,
        }

    def _initialize_ui(self) -> None:
        self.ui = Ui_MuoviForm()
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
        self.connection_ip_combo_box: QComboBox = self.ui.connectionIPComboBox
        self.connection_port_label: QLabel = self.ui.connectionPortLabel
        self.connection_update_push_button: QPushButton = (
            self.ui.connectionUpdatePushButton
        )
        self.connection_update_push_button.clicked.connect(
            lambda: (
                self.connection_ip_combo_box.clear(),
                self.connection_ip_combo_box.addItems(
                    self._device.get_server_wifi_ip_address()
                ),
            )
        )

        self.connection_ip_combo_box.clear()
        self.connection_ip_combo_box.addItems(self._device.get_server_wifi_ip_address())

        self.connection_port_label.setText(str(MUOVI_NETWORK_PORT))

        # Input parameters
        self.input_parameters_group_box: QGroupBox = self.ui.inputGroupBox
        self.input_working_mode_combo_box: QComboBox = self.ui.inputWorkingModeComboBox
        self.input_detection_mode_combo_box: QComboBox = (
            self.ui.inputDetectionModeComboBox
        )

        # Configuration parameters
        self.configuration_group_boxes: list[QGroupBox] = [
            self.input_parameters_group_box,
        ]
