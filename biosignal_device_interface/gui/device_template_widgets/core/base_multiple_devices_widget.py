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
from PySide6.QtCore import Signal
import numpy as np
import warnings

# Import Template
from biosignal_device_interface.gui.ui_compiled.devices_template_widget import (
    Ui_DeviceWidgetForm,
)
from biosignal_device_interface.constants.devices.core.base_device_constants import (
    DeviceType,
    DEVICE_NAME_DICT,
)

if TYPE_CHECKING:
    from biosignal_device_interface.gui.device_template_widgets.core.base_device_widget import (
        BaseDeviceWidget,
    )


class BaseMultipleDevicesWidget(QWidget):
    # Signals
    data_arrived: Signal = Signal(np.ndarray)
    biosignal_data_arrived: Signal = Signal(np.ndarray)
    auxiliary_data_arrived: Signal = Signal(np.ndarray)
    connect_toggled = Signal(bool)
    configure_toggled = Signal(bool)
    stream_toggled = Signal(bool)
    device_changed_signal = Signal(None)

    def __init__(self, parent: QWidget | QMainWindow | None = None):
        super().__init__(parent)

        self.parent_widget: QWidget | QMainWindow | None = parent

        self.ui = Ui_DeviceWidgetForm()
        self.ui.setupUi(self)

        self.device_stacked_widget = self.ui.deviceStackedWidget
        self.device_selection_combo_box = self.ui.deviceSelectionComboBox

    def get_device_information(self) -> Dict[str, Union[str, int]]:
        return self._get_current_widget().get_device_information()

    def _update_stacked_widget(self, index: int):
        current_widget = self._get_current_widget()
        current_widget.disconnect_device()

        with warnings.catch_warnings():
            warnings.filterwarnings("ignore")
            try:
                current_widget.data_arrived.disconnect(self.data_arrived.emit)
                current_widget.biosignal_data_arrived.disconnect(
                    self.biosignal_data_arrived.emit
                )
                current_widget.auxiliary_data_arrived.disconnect(
                    self.auxiliary_data_arrived.emit
                )

                current_widget.connect_toggled.disconnect(self.connect_toggled)
                current_widget.configure_toggled.disconnect(self.configure_toggled)
                current_widget.stream_toggled.disconnect(self.stream_toggled)

            except (TypeError, RuntimeError):
                ...

        self.device_stacked_widget.setCurrentIndex(index)
        current_widget = self._get_current_widget()

        # Data arrived
        current_widget.data_arrived.connect(self.data_arrived.emit)
        # Biosignal data arrived
        current_widget.biosignal_data_arrived.connect(self.biosignal_data_arrived.emit)
        # Auxiliary data arrived
        current_widget.auxiliary_data_arrived.connect(self.auxiliary_data_arrived.emit)

        current_widget.connect_toggled.connect(self.connect_toggled)
        current_widget.configure_toggled.connect(self.configure_toggled)
        current_widget.stream_toggled.connect(self.stream_toggled)

        self.device_changed_signal.emit()

    def _set_devices(self, devices: Dict[DeviceType, BaseDeviceWidget]) -> None:
        for device_type, device_widget in devices.items():
            self.device_stacked_widget.addWidget(device_widget)
            self.device_selection_combo_box.addItem(DEVICE_NAME_DICT[device_type])

        self._update_stacked_widget(0)
        self.device_selection_combo_box.currentIndexChanged.connect(
            self._update_stacked_widget
        )

    def _get_current_widget(self) -> BaseDeviceWidget:
        return self.device_stacked_widget.currentWidget()

    def closeEvent(self, event: QCloseEvent) -> None:
        self._get_current_widget().closeEvent(event)
