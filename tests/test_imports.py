from PySide6.QtWidgets import QMainWindow, QWidget, QApplication
import sys

from biosignal_device_interface import devices
from biosignal_device_interface.constants.devices import DeviceType

# Test all devices

muovi: devices.OTBMuovi = devices.OTBMuovi()
assert muovi._device_type == DeviceType.OTB_MUOVI, "Muovi device type is incorrect."

muovi_plus: devices.OTBMuovi = devices.OTBMuovi(is_muovi_plus=True)
assert (
    muovi_plus._device_type == DeviceType.OTB_MUOVI_PLUS
), "Muovi Plus device type is incorrect."

quattrocento_light: devices.OTBQuattrocentoLight = devices.OTBQuattrocentoLight()
assert (
    quattrocento_light._device_type == DeviceType.OTB_QUATTROCENTO_LIGHT
), "Quattrocento Light device type is incorrect."

...

# Test all otb devices
muovi: devices.OTBMuovi = devices.OTBMuovi()
assert muovi._device_type == DeviceType.OTB_MUOVI, "Muovi device type is incorrect."

muovi_plus: devices.OTBMuovi = devices.OTBMuovi(is_muovi_plus=True)
assert (
    muovi_plus._device_type == DeviceType.OTB_MUOVI_PLUS
), "Muovi Plus device type is incorrect."

quattrocento_light: devices.OTBQuattrocentoLight = devices.OTBQuattrocentoLight()
assert (
    quattrocento_light._device_type == DeviceType.OTB_QUATTROCENTO_LIGHT
), "Quattrocento Light device type is incorrect."

...


class TestApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.devices_widget = QWidget(self)
        self.setCentralWidget(self.devices_widget)

        # Test all widgets
        # Test All Devices Widget
        self.devices_widget: devices.AllDevicesWidget = devices.AllDevicesWidget()
        assert (
            self.devices_widget._device_selection[
                DeviceType.OTB_MUOVI
            ].device._device_type
            == DeviceType.OTB_MUOVI
        ), "Muovi device type is incorrect."
        assert (
            self.devices_widget._device_selection[
                DeviceType.OTB_MUOVI_PLUS
            ].device._device_type
            == DeviceType.OTB_MUOVI_PLUS
        ), "Muovi Plus device type is incorrect."
        assert (
            self.devices_widget._device_selection[
                DeviceType.OTB_QUATTROCENTO_LIGHT
            ].device._device_type
            == DeviceType.OTB_QUATTROCENTO_LIGHT
        ), "Quattrocento Light device type is incorrect."

        ...
        # Test OTB Devices Widget
        self.devices_widget: devices.OTBDevicesWidget = devices.OTBDevicesWidget()
        assert (
            self.devices_widget._device_selection[
                DeviceType.OTB_MUOVI
            ].device._device_type
            == DeviceType.OTB_MUOVI
        ), "Muovi device type is incorrect."
        assert (
            self.devices_widget._device_selection[
                DeviceType.OTB_MUOVI_PLUS
            ].device._device_type
            == DeviceType.OTB_MUOVI_PLUS
        ), "Muovi Plus device type is incorrect."
        assert (
            self.devices_widget._device_selection[
                DeviceType.OTB_QUATTROCENTO_LIGHT
            ].device._device_type
            == DeviceType.OTB_QUATTROCENTO_LIGHT
        ), "Quattrocento Light device type is incorrect."

        # Individual Widgets
        self.devices_widget: devices.OTBMuoviWidget = devices.OTBMuoviWidget()
        assert (
            self.devices_widget._device._device_type == DeviceType.OTB_MUOVI
        ), "Muovi device type is incorrect."

        self.devices_widget: devices.OTBMuoviPlusWidget = devices.OTBMuoviPlusWidget()
        assert (
            self.devices_widget._device._device_type == DeviceType.OTB_MUOVI_PLUS
        ), "Muovi Plus device type is incorrect."

        self.devices_widget: devices.OTBQuattrocentoLightWidget = (
            devices.OTBQuattrocentoLightWidget()
        )
        assert (
            self.devices_widget._device._device_type
            == DeviceType.OTB_QUATTROCENTO_LIGHT
        ), "Quattrocento Light device type is incorrect."


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test_application = TestApplication()
