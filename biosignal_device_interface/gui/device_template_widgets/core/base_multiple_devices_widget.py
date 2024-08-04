"""
Base Device class for real-time interfaces to hardware devices.
Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2024-06-05
"""

# Python Libraries
from __future__ import annotations
from typing import TYPE_CHECKING, Union, Dict
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QWidget, QMainWindow

# Import Template
from biosignal_device_interface.gui.ui_compiled.devices_template_widget import (
    Ui_DeviceWidgetForm,
)

if TYPE_CHECKING:
    from PySide6.QtCore import Signal
    import numpy as np
    from biosignal_device_interface.gui.device_template_widgets.core.base_device_widget import (
        BaseDeviceWidget,
    )
    from biosignal_device_interface.constants.devices.base_device_constants import (
        DeviceType,
        DEVICE_NAME_DICT,
    )


class BaseMultipleDevicesWidget(QWidget):
    # Signals
    data_arrived: Signal = Signal(np.ndarray)
    biosignal_data_arrived: Signal = Signal(np.ndarray)
    auxiliary_data_arrived: Signal = Signal(np.ndarray)
    device_connected_signal = Signal(bool)
    device_configured_signal = Signal(bool)
    device_stream_signal = Signal(bool)
    device_changed_signal = Signal(None)

    def __init__(self, parent: QWidget | QMainWindow | None = None):
        super().__init__(parent)

        self.parent_widget: QWidget | QMainWindow | None = parent

        self.ui = Ui_DeviceWidgetForm()
        self.ui.setupUi(self)

        self.device_stacked_widget = self.ui.deviceStackedWidget
        self.device_selection_combo_box = self.ui.deviceSelectionComboBox
        self.device_selection_combo_box.currentIndexChanged.connect(
            self._update_stacked_widget
        )

    def get_device_information(self) -> Dict[str, Union[str, int]]:
        return self._get_current_widget().get_device_information()

    def _update_stacked_widget(self, index: int):
        current_widget = self._get_current_widget()
        current_widget.disconnect()
        try:
            current_widget.data_arrived.disconnect(self.data_arrived.emit)
            current_widget.biosignal_data_arrived.disconnect(
                self.biosignal_data_arrived.emit
            )
            current_widget.auxiliary_data_arrived.disconnect(
                self.auxiliary_data_arrived.emit
            )

            current_widget.connect_toggled.disconnect(self.device_connected_signal)
            current_widget.configure_toggled.disconnect(self.device_configured_signal)
            current_widget.stream_toggled.disconnect(self.device_stream_signal)

        except Exception:
            pass

        self.device_stacked_widget.setCurrentIndex(index)
        current_widget = self._get_current_widget()

        current_widget.data_arrived.connect(self.data_arrived.emit)
        current_widget.biosignal_data_arrived.connect(self.biosignal_data_arrived.emit)
        current_widget.auxiliary_data_arrived.connect(self.auxiliary_data_arrived.emit)

        current_widget.connect_toggled.connect(self.device_connected_signal)
        current_widget.configure_toggled.connect(self.device_configured_signal)
        current_widget.stream_toggled.connect(self.device_stream_signal)

        self.device_changed_signal.emit()

    def _set_devices(self, devices: Dict[DeviceType, BaseDeviceWidget]) -> None:
        for device_type, device_widget in devices.items():
            self.device_stacked_widget.addWidget(device_widget)
            self.device_selection_combo_box.addItem(DEVICE_NAME_DICT[device_type])

        self._update_stacked_widget(0)

    def _get_current_widget(self) -> BaseDeviceWidget:
        return self.device_stacked_widget.currentWidget()

    def closeEvent(self, event: QCloseEvent) -> None:
        self._get_current_widget().closeEvent(event)
