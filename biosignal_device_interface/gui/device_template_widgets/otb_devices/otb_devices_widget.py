from __future__ import annotations
from typing import TYPE_CHECKING, Dict

from biosignal_device_interface.gui.device_template_widgets.core.base_multiple_devices_widget import (
    BaseMultipleDevicesWidget,
)
from biosignal_device_interface.constants.devices.base_device_constants import (
    DeviceType,
)
from biosignal_device_interface.gui.device_template_widgets.otb_devices import (
    MuoviPlusWidget,
    MuoviWidget,
    QuattrocentoLightWidget,
)

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget, QMainWindow
    from biosignal_device_interface.gui.device_template_widgets.core.base_device_widget import (
        BaseDeviceWidget,
    )


class AllDevicesWidget(BaseMultipleDevicesWidget):
    def __init__(self, parent: QWidget | QMainWindow | None = None):
        super().__init__(parent)

        self._device_selection: Dict[DeviceType, BaseDeviceWidget] = {
            DeviceType.OTB_QUATTROCENTO_LIGHT: QuattrocentoLightWidget(self),
            DeviceType.OTB_MUOVI: MuoviWidget(self),
            DeviceType.OTB_MUOVI_PLUS: MuoviPlusWidget(self),
        }
        self._set_devices(self._device_selection)
