from biosignal_device_interface import otb_devices, devices, DeviceType

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
muovi: otb_devices.Muovi = otb_devices.Muovi()
assert muovi._device_type == DeviceType.OTB_MUOVI, "Muovi device type is incorrect."

muovi_plus: otb_devices.Muovi = otb_devices.Muovi(is_muovi_plus=True)
assert (
    muovi_plus._device_type == DeviceType.OTB_MUOVI_PLUS
), "Muovi Plus device type is incorrect."

quattrocento_light: otb_devices.QuattrocentoLight = otb_devices.QuattrocentoLight()
assert (
    quattrocento_light._device_type == DeviceType.OTB_QUATTROCENTO_LIGHT
), "Quattrocento Light device type is incorrect."

...
