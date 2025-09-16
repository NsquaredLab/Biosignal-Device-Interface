from __future__ import annotations
from typing import TYPE_CHECKING

from biosignal_device_interface.gui.device_template_widgets.core.base_device_widget import (
    BaseDeviceWidget,
)
from biosignal_device_interface.gui.ui_compiled.otb_quattrocento_light_template_widget import (
    Ui_QuattrocentoLightForm,
)
from biosignal_device_interface.devices.otb.otb_quattrocento_light import (
    OTBQuattrocentoLight,
)

# Constants
from biosignal_device_interface.constants.devices.otb.otb_quattrocento_light_constants import (
    QuattrocentoLightSamplingFrequency,
    QuattrocentoLightStreamingFrequency,
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
    )


class OTBQuattrocentoLightWidget(BaseDeviceWidget):
    def __init__(self, parent: QWidget | QMainWindow | None = None):
        super().__init__(parent)
        self._set_device(OTBQuattrocentoLight(self))

    def _toggle_connection(self) -> None:
        if not self._device.is_connected:
            self._connect_push_button.setEnabled(False)

        self._device.toggle_connection(
            (self._connection_ip_label.text(), int(self._connection_port_label.text())),
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
        self._device_params["grids"] = [
            i
            for i, check_box in enumerate(self._grid_selection_check_box_list)
            if check_box.isChecked()
        ]

        self._device_params["streaming_frequency_mode"] = (
            QuattrocentoLightStreamingFrequency(
                self._acquisition_streaming_frequency_combo_box.currentIndex() + 1
            )
        )
        self._device_params["sampling_frequency_mode"] = (
            QuattrocentoLightSamplingFrequency(
                self._acquisition_sampling_frequency_combo_box.currentIndex() + 1
            )
        )

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

    def _initialize_device_params(self) -> None:
        self._device_params = {
            "grids": [2, 3],
            "streaming_frequency_mode": QuattrocentoLightStreamingFrequency.THIRTYTWO,
            "sampling_frequency_mode": QuattrocentoLightSamplingFrequency.MEDIUM,
        }

    def _initialize_ui(self) -> None:
        self.ui = Ui_QuattrocentoLightForm()
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
        self._connection_ip_label: QLabel = self.ui.connectionIPLabel
        self._connection_port_label: QLabel = self.ui.connectionPortLabel

        # Acquisition parameters
        self._acquisition_group_box: QGroupBox = self.ui.acquisitionGroupBox
        self._acquisition_sampling_frequency_combo_box: QComboBox = (
            self.ui.acquisitionSamplingFrequencyComboBox
        )
        self._acquisition_streaming_frequency_combo_box: QComboBox = (
            self.ui.acquisitionStreamingFrequencyComboBox
        )

        # Grid parameters
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
        self._grid_selection_check_box_list[2].setChecked(True)
        self._grid_selection_check_box_list[3].setChecked(True)

        # Configuration parameters
        self._configuration_group_boxes: list[QGroupBox] = [
            self._acquisition_group_box,
            self._grid_selection_group_box,
        ]
