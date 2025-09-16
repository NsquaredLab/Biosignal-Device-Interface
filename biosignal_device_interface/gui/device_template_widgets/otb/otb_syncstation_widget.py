"""
Device class for real-time interfacing the OTB Syncstation device.
Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2025-01-09
"""

from __future__ import annotations
from functools import partial
from typing import TYPE_CHECKING, Dict

from biosignal_device_interface.gui.device_template_widgets.core.base_device_widget import (
    BaseDeviceWidget,
)

# Local Libraries
from biosignal_device_interface.gui.ui_compiled.otb_syncstation_template_widget import (
    Ui_SyncStationForm,
)
from biosignal_device_interface.devices.otb.otb_syncstation import OTBSyncStation

# Constants
from biosignal_device_interface.constants.devices.otb.otb_syncstation_constants import (
    SyncStationDetectionMode,
    SyncStationProbeConfigMode,
    SyncStationRecOnMode,
    SyncStationWorkingMode,
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
        QTabWidget,
    )


class OTBSyncStationWidget(BaseDeviceWidget):
    def __init__(self, parent: QWidget | QMainWindow | None = None):
        super().__init__(parent)
        self._set_device(OTBSyncStation(self))

    def _toggle_connection(self):
        if not self._device.is_connected:
            self._command_connect_push_button.setEnabled(False)

        self._device.toggle_connection(
            (self._connection_ip_label.text(), int(self._connection_port_label.text())),
        )

    def _connection_toggled(self, is_connected: bool) -> None:
        self._command_connect_push_button.setEnabled(True)
        if is_connected:
            self._command_connect_push_button.setText("Disconnect")
            self._command_connect_push_button.setChecked(True)
            self._command_configure_push_button.setEnabled(True)
            self._connection_group_box.setEnabled(False)
        else:
            self._command_connect_push_button.setText("Connect")
            self._command_connect_push_button.setChecked(False)
            self._command_configure_push_button.setEnabled(False)
            self._command_stream_push_button.setEnabled(False)
            self._connection_group_box.setEnabled(True)

        self.connect_toggled.emit(is_connected)

    def _toggle_configuration(self) -> None:
        self._device_params["working_mode"] = SyncStationWorkingMode(
            self._input_working_mode_combo_box.currentIndex() + 1
        )

        count_enabled = 0
        for key, value in self._probes_dict.items():
            is_enabled = value["probe_status"].isChecked()
            self._device_params["bytes_configuration_A"][key][
                "probe_status"
            ] = is_enabled
            self._device_params["bytes_configuration_A"][key]["detection_mode"] = (
                SyncStationDetectionMode(value["detection_mode"].currentIndex() + 1)
            )

            if is_enabled:
                count_enabled += 1

        self._device_params["number_of_probes"] = count_enabled

        self._device.configure_device(self._device_params)

    def _configuration_toggled(self, is_configured: bool) -> None:
        if is_configured:
            self._command_stream_push_button.setEnabled(True)

        self.configure_toggled.emit(is_configured)

    def _toggle_stream(self) -> None:
        self._command_stream_push_button.setEnabled(False)
        self._device.toggle_streaming()

    def _stream_toggled(self, is_streaming: bool) -> None:
        self._command_stream_push_button.setEnabled(True)
        if is_streaming:
            self._command_stream_push_button.setText("Stop Streaming")
            self._command_stream_push_button.setChecked(True)
            self._command_configure_push_button.setEnabled(False)
            self._input_group_box.setEnabled(False)
        else:
            self._command_stream_push_button.setText("Start Streaming")
            self._command_stream_push_button.setChecked(False)
            self._command_configure_push_button.setEnabled(True)
            self._input_group_box.setEnabled(True)

        self.stream_toggled.emit(is_streaming)

    def _update_probe_params(self, probe: SyncStationProbeConfigMode, state) -> None:
        self._probes_dict[probe]["detection_mode"].setEnabled(state == 2)

    def _initialize_device_params(self) -> None:
        self._device_params = {
            "rec_on_mode": SyncStationRecOnMode.OFF,
            "working_mode": SyncStationWorkingMode.EMG,
            "number_of_probes": 0,
            "bytes_configuration_A": {
                SyncStationProbeConfigMode(i): {
                    "probe_status": False,
                    "detection_mode": SyncStationDetectionMode.MONOPOLAR_GAIN_LOW,
                }
                for i in range(1, len(SyncStationProbeConfigMode))
            },
        }

    def _set_default_probe_params(self) -> None:
        for values in self._probes_dict.values():
            values["detection_mode"].setCurrentIndex(1)
            values["probe_status"].setChecked(True)
            values["probe_status"].setChecked(False)

        self._probes_dict[SyncStationProbeConfigMode.MUOVI_PROBE_ONE][
            "probe_status"
        ].setChecked(True)

        self._probes_dict[SyncStationProbeConfigMode.MUOVI_PROBE_TWO][
            "probe_status"
        ].setChecked(True)

    def _initialize_ui(self):
        self.ui = Ui_SyncStationForm()
        self.ui.setupUi(self)

        # Command Push Buttons
        self._command_connect_push_button: QPushButton = (
            self.ui.commandConnectionPushButton
        )
        self._command_connect_push_button.clicked.connect(self._toggle_connection)
        self._device.connect_toggled.connect(self._connection_toggled)

        self._command_configure_push_button: QPushButton = (
            self.ui.commandConfigurationPushButton
        )
        self._command_configure_push_button.clicked.connect(self._toggle_configuration)
        self._command_configure_push_button.setEnabled(False)
        self._device.configure_toggled.connect(self._configuration_toggled)

        self._command_stream_push_button: QPushButton = self.ui.commandStreamPushButton
        self._command_stream_push_button.clicked.connect(self._toggle_stream)
        self._command_stream_push_button.setEnabled(False)
        self._device.stream_toggled.connect(self._stream_toggled)

        # Connection Paramters
        self._connection_group_box: QGroupBox = self.ui.connectionGroupBox
        self._connection_ip_label: QLabel = self.ui.connectionIPAddressLabel
        self._connection_port_label: QLabel = self.ui.connectionPortLabel

        # Input Parameters
        self._input_group_box: QGroupBox = self.ui.inputGroupBox
        self._input_working_mode_combo_box: QComboBox = self.ui.inputWorkingModeComboBox
        self._input_working_mode_combo_box.setCurrentIndex(1)

        self._probes_tab_widget: QTabWidget = self.ui.probesTabWidget
        self._probes_tab_widget.setCurrentIndex(0)
        self._probes_dict: Dict[
            SyncStationProbeConfigMode, dict[str, QComboBox | QCheckBox]
        ] = self._configure_probes_dict()

        for key, value in self._probes_dict.items():
            value["probe_status"].stateChanged.connect(
                partial(self._update_probe_params, key)
            )

        self._set_default_probe_params()

    def _configure_probes_dict(self) -> None:
        return {
            SyncStationProbeConfigMode.MUOVI_PROBE_ONE: {
                "probe_status": self.ui.muoviProbeOneEnableCheckBox,
                "detection_mode": self.ui.muoviProbeOneDetectionModeComboBox,
            },
            SyncStationProbeConfigMode.MUOVI_PROBE_TWO: {
                "probe_status": self.ui.muoviProbeTwoEnableCheckBox,
                "detection_mode": self.ui.muoviProbeTwoDetectionModeComboBox,
            },
            SyncStationProbeConfigMode.MUOVI_PROBE_THREE: {
                "probe_status": self.ui.muoviProbeThreeEnableCheckBox,
                "detection_mode": self.ui.muoviProbeThreeDetectionModeComboBox,
            },
            SyncStationProbeConfigMode.MUOVI_PROBE_FOUR: {
                "probe_status": self.ui.muoviProbeFourEnableCheckBox,
                "detection_mode": self.ui.muoviProbeFourDetectionModeComboBox,
            },
            SyncStationProbeConfigMode.MUOVI_PLUS_PROBE_ONE: {
                "probe_status": self.ui.muoviPlusProbeOneEnableCheckBox,
                "detection_mode": self.ui.muoviPlusProbeOneDetectionModeComboBox,
            },
            SyncStationProbeConfigMode.MUOVI_PLUS_PROBE_TWO: {
                "probe_status": self.ui.muoviPlusProbeTwoEnableCheckBox,
                "detection_mode": self.ui.muoviPlusProbeTwoDetectionModeComboBox,
            },
            SyncStationProbeConfigMode.DUE_PLUS_PROBE_ONE: {
                "probe_status": self.ui.duePlusProbeOneEnableCheckBox,
                "detection_mode": self.ui.duePlusProbeOneDetectionModeComboBox,
            },
            SyncStationProbeConfigMode.DUE_PLUS_PROBE_TWO: {
                "probe_status": self.ui.duePlusProbeTwoEnableCheckBox,
                "detection_mode": self.ui.duePlusProbeTwoDetectionModeComboBox,
            },
            SyncStationProbeConfigMode.DUE_PLUS_PROBE_THREE: {
                "probe_status": self.ui.duePlusProbeThreeEnableCheckBox,
                "detection_mode": self.ui.duePlusProbeThreeDetectionModeComboBox,
            },
            SyncStationProbeConfigMode.DUE_PLUS_PROBE_FOUR: {
                "probe_status": self.ui.duePlusProbeFourEnableCheckBox,
                "detection_mode": self.ui.duePlusProbeFourDetectionModeComboBox,
            },
            SyncStationProbeConfigMode.DUE_PLUS_PROBE_FIVE: {
                "probe_status": self.ui.duePlusProbeFiveEnableCheckBox,
                "detection_mode": self.ui.duePlusProbeFiveDetectionModeComboBox,
            },
            SyncStationProbeConfigMode.DUE_PLUS_PROBE_SIX: {
                "probe_status": self.ui.duePlusProbeSixEnableCheckBox,
                "detection_mode": self.ui.duePlusProbeSixDetectionModeComboBox,
            },
            SyncStationProbeConfigMode.DUE_PLUS_PROBE_SEVEN: {
                "probe_status": self.ui.duePlusProbeSevenEnableCheckBox,
                "detection_mode": self.ui.duePlusProbeSevenDetectionModeComboBox,
            },
            SyncStationProbeConfigMode.DUE_PLUS_PROBE_EIGHT: {
                "probe_status": self.ui.duePlusProbeEightEnableCheckBox,
                "detection_mode": self.ui.duePlusProbeEightDetectionModeComboBox,
            },
            SyncStationProbeConfigMode.DUE_PLUS_PROBE_NINE: {
                "probe_status": self.ui.duePlusProbeNineEnableCheckBox,
                "detection_mode": self.ui.duePlusProbeNineDetectionModeComboBox,
            },
            SyncStationProbeConfigMode.DUE_PLUS_PROBE_TEN: {
                "probe_status": self.ui.duePlusProbeTenEnableCheckBox,
                "detection_mode": self.ui.duePlusProbeTenDetectionModeComboBox,
            },
        }
