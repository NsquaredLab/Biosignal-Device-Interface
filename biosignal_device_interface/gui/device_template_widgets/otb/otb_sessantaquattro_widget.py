from __future__ import annotations
from typing import TYPE_CHECKING

from biosignal_device_interface.gui.device_template_widgets.core.base_device_widget import (
    BaseDeviceWidget,
)
from biosignal_device_interface.gui.ui_compiled.otb_sessantaquattro_template_widget import (
    Ui_SessantaquattroForm,
)
from biosignal_device_interface.devices.otb.otb_sessantaquattro import (
    OTBSessantaquattro,
)

# Constants
from biosignal_device_interface.constants.devices.otb.otb_sessantaquattro_constants import (
    SessantaquattroChannelMode,
    SessantaquattroDetectionMode,
    SessantaquattroGainMode,
    SessantaquattroResolutionMode,
    SessantaquattroSamplingFrequencyMode,
)

if TYPE_CHECKING:
    from PySide6.QtWidgets import (
        QWidget,
        QMainWindow,
        QGroupBox,
        QPushButton,
        QComboBox,
        QRadioButton,
        QLineEdit,
    )


class OTBSessantaquattroWidget(BaseDeviceWidget):
    def __init__(self, parent: QWidget | QMainWindow | None = None):
        super().__init__(parent)

        self._set_device(OTBSessantaquattro(parent=self))

    def _toggle_connection(self) -> None:
        if not self._device.is_connected:
            self._connect_push_button.setEnabled(False)

        self._device.toggle_connection(
            (
                self._connection_ip_line_edit.text(),
                int(self._connection_port_line_edit.text()),
            )
        )

    def _connection_toggled(self, is_connected: bool) -> None:
        self._connect_push_button.setEnabled(True)
        if is_connected:
            self._connect_push_button.setText("Disconnect")
            self._connect_push_button.setChecked(True)
            self._configure_push_button.setEnabled(True)
            self._connection_group_box.setEnabled(False)
        else:
            self._connect_push_button.setText("Connect")
            self._connect_push_button.setChecked(False)
            self._configure_push_button.setEnabled(False)
            self._stream_push_button.setEnabled(False)
            self._connection_group_box.setEnabled(True)

        self.connect_toggled.emit(is_connected)

    def _toggle_configuration(self) -> None:
        self._update_device_params()

        self._device.configure_device(self._device_params)

    def _configuration_toggled(self, is_configured: bool) -> None:
        if is_configured:
            self._stream_push_button.setEnabled(True)

        self.configure_toggled.emit(is_configured)

    def _toggle_configuration_group_boxes(self) -> None:
        for group_box in self._configuration_group_boxes:
            group_box.setEnabled(not group_box.isEnabled())

    def _toggle_stream(self) -> None:
        self._stream_push_button.setEnabled(False)
        self._device.toggle_streaming()

    def _stream_toggled(self, is_streaming: bool) -> None:
        self._stream_push_button.setEnabled(True)
        if is_streaming:
            self._stream_push_button.setText("Stop Streaming")
            self._stream_push_button.setChecked(True)
            self._configure_push_button.setEnabled(False)
            self._toggle_configuration_group_boxes()
        else:
            self._stream_push_button.setText("Stream")
            self._stream_push_button.setChecked(False)
            self._configure_push_button.setEnabled(True)
            self._toggle_configuration_group_boxes()

        self.stream_toggled.emit(is_streaming)

    def _update_device_params(self) -> None:
        self._device_params = {
            "sampling_frequency_mode": SessantaquattroSamplingFrequencyMode(
                self._get_enum_value(
                    self._acquisition_sampling_frequency_mode_combo_box
                )
            ),
            "channel_mode": SessantaquattroChannelMode(
                self._get_enum_value(self._acquisition_channel_mode_combo_box)
            ),
            "detection_mode": SessantaquattroDetectionMode(
                self._get_enum_value(self._input_detection_mode_combo_box)
            ),
            "resolution_mode": SessantaquattroResolutionMode(
                self._get_resolution_mode()
            ),
            "gain_mode": SessantaquattroGainMode(
                self._get_enum_value(self._input_gain_mode_combo_box)
            ),
            "trigger_mode": None,  # TODO: Implement trigger mode
            "recording_mode": None,  # TODO: Implement recording mode
        }

        print(self._device_params)  # TODO: Remove

    def _initialize_device_params(self) -> None:
        self._device_params = {
            "sampling_frequency_mode": SessantaquattroSamplingFrequencyMode.NONE,
            "channel_mode": SessantaquattroChannelMode.NONE,
            "detection_mode": SessantaquattroDetectionMode.NONE,
            "resolution_mode": SessantaquattroResolutionMode.NONE,
            "gain_mode": SessantaquattroGainMode.NONE,
            "trigger_mode": None,  # TODO: Implement trigger mode
            "recording_mode": None,  # TODO: Implement recording mode
        }

    def _get_enum_value(self, combo_box: QComboBox) -> int | None:
        index = combo_box.currentIndex()
        return index + 1

    def _get_resolution_mode(self) -> SessantaquattroResolutionMode:
        if self._input_high_resolution_mode_combo_box.isChecked():
            return SessantaquattroResolutionMode.HIGH
        else:
            return SessantaquattroResolutionMode.LOW

    def _initialize_ui(self) -> None:
        self.ui = Ui_SessantaquattroForm()
        self.ui.setupUi(self)

        # Command Push Buttons
        self._connect_push_button: QPushButton = self.ui.commandConnectionPushButton
        self._connect_push_button.clicked.connect(self._toggle_connection)
        self._device.connect_toggled.connect(self._connection_toggled)

        self._configure_push_button: QPushButton = (
            self.ui.commandConfigurationPushButton
        )
        self._configure_push_button.clicked.connect(self._toggle_configuration)
        self._configure_push_button.setEnabled(False)
        self._device.configure_toggled.connect(self._configuration_toggled)

        self._stream_push_button: QPushButton = self.ui.commandStreamPushButton
        self._stream_push_button.clicked.connect(self._toggle_stream)
        self._stream_push_button.setEnabled(False)
        self._device.stream_toggled.connect(self._stream_toggled)

        # Connection parameters
        # TODO: Check if IP is valid or 127.0.0.1 and Port is valid or 31000 should be used
        self._connection_group_box: QGroupBox = self.ui.connectionGroupBox
        self._connection_ip_line_edit: QLineEdit = self.ui.connectionIPLineEdit
        self._connection_port_line_edit: QLineEdit = self.ui.connectionPortLineEdit

        # Acquisition parameters
        self._acquisition_group_box: QGroupBox = self.ui.acquisitionGroupBox
        self._acquisition_sampling_frequency_mode_combo_box: QComboBox = (
            self.ui.acquisitionSamplingFrequencyModeComboBox
        )
        self._acquisition_channel_mode_combo_box: QComboBox = (
            self.ui.acquisitionChannelModeComboBox
        )

        # Input parameters
        self._input_parameters_group_box: QGroupBox = self.ui.inputParametersGroupBox
        self._input_low_resolution_mode_combo_box: QRadioButton = (
            self.ui.inputLowResolutionRadioButton
        )
        self._input_high_resolution_mode_combo_box: QRadioButton = (
            self.ui.inputHighResolutionRadioButton
        )
        self._input_detection_mode_combo_box: QComboBox = (
            self.ui.inputDetectionModeComboBox
        )
        self._input_gain_mode_combo_box: QComboBox = self.ui.inputGainModeComboBox
        self._input_detection_mode_combo_box: QComboBox = (
            self.ui.inputDetectionModeComboBox
        )

        # Configuration parameters
        self._configuration_group_boxes: list[QGroupBox] = [
            self._input_parameters_group_box,
            self._acquisition_group_box,
        ]
