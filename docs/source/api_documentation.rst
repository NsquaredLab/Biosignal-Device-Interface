API - Biosignal Device Interface
==============================================

The device classes are responsible for interfacing to the device and reading the data, 
while the device widget classes are responsible for displaying the data in a GUI.

Devices (QObjects)
======================
The Biosignal Device Interface package consists of device classes derived from BaseDevice.
The device classes are responsible for interfacing to the device and reading the data.

The base device must be inherited by all other devices. It is the base class for all devices.

.. toctree::
    :maxdepth: 1

    modules/devices/core/base_device.rst

Available devices are listed in the following section:

.. toctree::
    :maxdepth: 2

    modules/devices/otb/otb.rst



Device Widgets (QWidgets)
==========================
The Biosignal Device Interface package consists of device widget classes derived from BaseDeviceWidget. 
The device widget classes are responsible for displaying the device configurations in a GUI.

.. toctree::
    :maxdepth: 2

    modules/gui/device_template_widgets

The Device Widget UI files were created using Qt Designer (saved in .ui folder).
The Qt Designer is automatically installed by installing the PySide6 package.

.. note:: It is recommended to install the PySide6 package globally and link the pyside6-designer.exe to your IDE as external tool (e.g., PyCharm) or a PyQt Plugin (e.g., VSCode).

After creating the UI files, the .ui files must be converted to .py files using the following tool: pyside6-uic.exe.
The command to convert the .ui file to .py file is as follows:
pyside6-uic <path_to_ui_file> -o <path_to_ui_file_parent_folder/ui_file_name.ui>


Device Constants
=================

It is highly recommeded to use the device constants to configure respective devices if the device widget classes are not used in your own software.

Device widget classes should only use the device constants to configure the devices. Enums are used to define the device constants while Dictionaries with Enum keys are used to set the respective value.
The features can be set in the configuration file:

.. toctree::
    :maxdepth: 2

    modules/constants/devices