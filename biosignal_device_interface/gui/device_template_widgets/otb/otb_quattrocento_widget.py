"""
Quattrocento Widget class for GUI configuration
of the Quattrocento from OT Bioelettronica.

Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2025-01-15
"""

from __future__ import annotations
from functools import partial
from typing import TYPE_CHECKING

from biosignal_device_interface.gui.device_template_widgets.core.base_device_widget import (
    BaseDeviceWidget,
)
from biosignal_device_interface.gui.ui_compiled.otb_quattrocento_template_widget import (
    Ui_QuattrocentoForm,
)
from biosignal_device_interface.devices.otb.otb_quattrocento import (
    OTBQuattrocento,
)

# Constants
from biosignal_device_interface.constants.devices.otb.otb_quattrocento_constants import (
    QuattrocentoAcqSettByte,
    QuattrocentoAcquisitionMode,
    QuattrocentoDecimMode,
    QuattrocentoINXConf2Byte,
    QuattrocentoRecordingMode,
    QuattrocentoSamplingFrequencyMode,
    QuattrocentoNumberOfChannelsMode,
    QuattrocentoLowPassFilterMode,
    QuattrocentoHighPassFilterMode,
    QuattrocentoDetectionMode,
)

if TYPE_CHECKING:
    from PySide6.QtWidgets import (
        QMainWindow,
        QWidget,
        QGroupBox,
        QPushButton,
        QCheckBox,
        QComboBox,
        QLabel,
        QLineEdit,
    )


class OTBQuattrocentoWidget(BaseDeviceWidget):
    def __init__(self, parent: QWidget | QMainWindow | None = None):
        super().__init__(parent)
        self._set_device(OTBQuattrocento(self))

    def _toggle_connection(self):
        if not self._device.is_connected:
            self._connect_push_button.setEnabled(False)

        self._device.toggle_connection(
            (
                self._connection_ip_line_edit.text(),
                int(self._connection_port_line_edit.text()),
            ),
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

    def _toggle_configuration(self):
        self._device_params["grids"] = [
            i
            for i, check_box in enumerate(self._grid_selection_check_box_list)
            if check_box.isChecked()
        ]

        # Acquisition settings
        acq_sett_configuration = QuattrocentoAcqSettByte()
        acq_sett_configuration.update(
            decimation_mode=QuattrocentoDecimMode(
                int(self._acquisition_decimator_check_box.isChecked()) + 1
            ),
            recording_mode=QuattrocentoRecordingMode(
                int(self._acquisition_recording_check_box.isChecked()) + 1
            ),
            sampling_frequency_mode=QuattrocentoSamplingFrequencyMode(
                self._acquisition_sampling_frequency_combo_box.currentIndex() + 1
            ),
            number_of_channels_mode=QuattrocentoNumberOfChannelsMode(
                self._acquisition_number_of_channels_combo_box.currentIndex() + 1
            ),
        )
        self._device_params["acq_sett_configuration"] = acq_sett_configuration

        # Input settings
        inx_configuration = QuattrocentoINXConf2Byte()
        inx_configuration.update(
            high_pass_filter=QuattrocentoHighPassFilterMode(
                self._input_high_pass_filter_combo_box.currentIndex() + 1
            ),
            low_pass_filter=QuattrocentoLowPassFilterMode(
                self._input_low_pass_filter_combo_box.currentIndex() + 1
            ),
            detection_mode=QuattrocentoDetectionMode(
                self._input_detection_mode_combo_box.currentIndex() + 1
            ),
        )

        self._device_params["input_top_left_configuration"] = inx_configuration
        self._device_params["input_top_right_configuration"] = inx_configuration
        self._device_params["multiple_input_one_configuration"] = inx_configuration
        self._device_params["multiple_input_two_configuration"] = inx_configuration
        self._device_params["multiple_input_three_configuration"] = inx_configuration
        self._device_params["multiple_input_four_configuration"] = inx_configuration

        self._device.configure_device(self._device_params)

    def _configuration_toggled(self, is_configured: bool) -> None:
        if is_configured:
            self._stream_push_button.setEnabled(True)

        self.configure_toggled.emit(is_configured)

    def _toggle_stream(self) -> None:
        self._stream_push_button.setEnabled(False)
        self._device.toggle_streaming()

    def _toggle_configuration_group_boxes(self, state: bool) -> None:
        for group_box in self._configuration_group_boxes:
            group_box.setEnabled(state)

    def _stream_toggled(self, is_streaming):
        self._stream_push_button.setEnabled(True)
        if is_streaming:
            self._stream_push_button.setText("Stop Streaming")
            self._stream_push_button.setChecked(True)
            self._configure_push_button.setEnabled(False)
            self._toggle_configuration_group_boxes(False)
        else:
            self._stream_push_button.setText("Start Streaming")
            self._stream_push_button.setChecked(False)
            self._configure_push_button.setEnabled(True)
            self._toggle_configuration_group_boxes(True)

    def _initialize_device_params(self):
        self._device_params: dict = {
            "grids": [],
            "acq_sett_configuration": QuattrocentoAcqSettByte(),
            "input_top_left_configuration": QuattrocentoINXConf2Byte(),
            "input_top_right_configuration": QuattrocentoINXConf2Byte(),
            "multiple_input_one_configuration": QuattrocentoINXConf2Byte(),
            "multiple_input_two_configuration": QuattrocentoINXConf2Byte(),
            "multiple_input_three_configuration": QuattrocentoINXConf2Byte(),
            "multiple_input_four_configuration": QuattrocentoINXConf2Byte(),
        }

    def _initialize_ui(self):
        self.ui = Ui_QuattrocentoForm()
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
        self._connection_group_box: QGroupBox = self.ui.connectionGroupBox
        self._connection_ip_line_edit: QLineEdit = self.ui.connectionIPLineEdit
        self._default_connection_ip: str = self._connection_ip_line_edit.text()
        self._connection_ip_line_edit.editingFinished.connect(
            partial(
                self._check_ip_input,
                self._connection_ip_line_edit,
                self._default_connection_ip,
            )
        )
        self._connection_port_line_edit: QLineEdit = self.ui.connectionPortLineEdit
        self._default_connection_port: str = self._connection_port_line_edit.text()
        self._connection_port_line_edit.editingFinished.connect(
            partial(
                self._check_port_input,
                self._connection_port_line_edit,
                self._default_connection_port,
            )
        )

        # Acquisition parameters
        self._acquisition_group_box: QGroupBox = self.ui.acquisitionGroupBox
        self._acquisition_sampling_frequency_combo_box: QComboBox = (
            self.ui.acquisitionSamplingFrequencyComboBox
        )
        self._acquisition_number_of_channels_combo_box: QComboBox = (
            self.ui.acquisitionNumberOfChannelsComboBox
        )
        self._acquisition_decimator_check_box: QCheckBox = (
            self.ui.acquisitionDecimatorCheckBox
        )
        self._acquisition_recording_check_box: QCheckBox = (
            self.ui.acquisitionRecordingCheckBox
        )

        # Grid selection
        self._grid_selection_group_box: QGroupBox = self.ui.gridSelectionGroupBox
        self._grid_selection_check_box_list: list[QCheckBox] = [
            self.ui.gridOneCheckBox,
            self.ui.gridTwoCheckBox,
            self.ui.gridThreeCheckBox,
            self.ui.gridFourCheckBox,
            self.ui.gridFiveCheckBox,
            self.ui.gridSixCheckBox,
        ]

        [
            check_box.setChecked(False)
            for check_box in self._grid_selection_check_box_list
        ]

        # Input parameters
        self._input_group_box: QGroupBox = self.ui.inputGroupBox
        self._input_channel_combo_box: QComboBox = self.ui.inputChannelComboBox
        self._input_low_pass_filter_combo_box: QComboBox = self.ui.inputLowPassComboBox
        self._input_low_pass_default = self.ui.inputLowPassComboBox.currentIndex()
        self._input_high_pass_filter_combo_box: QComboBox = (
            self.ui.inputHighPassComboBox
        )
        self._input_high_pass_default = self.ui.inputHighPassComboBox.currentIndex()
        self._input_detection_mode_combo_box: QComboBox = (
            self.ui.inputDetectionModeComboBox
        )

        self._configuration_group_boxes: list[QGroupBox] = [
            self._acquisition_group_box,
            self._grid_selection_group_box,
            self._input_group_box,
        ]
