from __future__ import annotations
from typing import TYPE_CHECKING, Union, Dict

from biosignal_device_interface.gui.device_template_widgets.core.base_multiple_devices_widget import (
    BaseMultipleDevicesWidget,
)
from biosignal_device_interface.constants.devices.base_device_constants import (
    DeviceType,
)
from biosignal_device_interface.gui.device_template_widgets.otb_devices import (
    OTBMuoviPlusWidget,
    OTBMuoviWidget,
    OTBQuattrocentoLightWidget,
)

if TYPE_CHECKING:
    from PySide6.QtCore import Signal
    from PySide6.QtWidgets import QWidget, QMainWindow
    import numpy as np
    from biosignal_device_interface.gui.device_template_widgets.core.base_device_widget import (
        BaseDeviceWidget,
    )


class AllDevicesWidget(BaseMultipleDevicesWidget):
    def __init__(self, parent: QWidget | QMainWindow | None = None):
        super().__init__(parent)

        self._device_selection: Dict[DeviceType, BaseDeviceWidget] = {
            DeviceType.OTB_QUATTROCENTO_LIGHT: OTBQuattrocentoLightWidget(self),
            DeviceType.OTB_MUOVI: OTBMuoviWidget(self),
            DeviceType.OTB_MUOVI_PLUS: OTBMuoviPlusWidget(self),
        }
        self._set_devices(self._device_selection)
