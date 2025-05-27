=============
API Reference
=============

This section provides detailed documentation for all classes, methods, and functions in the Biosignal Device Interface package.

.. grid:: 1 2 2 2
    :gutter: 2

    .. grid-item-card:: 🔧 Devices
        :link: devices
        :link-type: doc

        Core device classes and interfaces for biosignal acquisition devices.

    .. grid-item-card:: 🖥️ GUI Components
        :link: gui
        :link-type: doc

        PySide6 widgets and GUI components for device control and visualization.

    .. grid-item-card:: ⚙️ Constants
        :link: constants
        :link-type: doc

        Device-specific constants, enums, and configuration parameters.

    .. grid-item-card:: 🛠️ Utilities
        :link: utilities
        :link-type: doc

        Helper functions and utility classes.

Package Overview
================

The Biosignal Device Interface is organized into several main modules:

.. autosummary::
   :toctree: generated/
   :template: module.rst

   biosignal_device_interface.devices
   biosignal_device_interface.gui
   biosignal_device_interface.constants

Core Architecture
=================

The package follows a hierarchical architecture:

**Base Classes**
    Abstract base classes that define the common interface for all devices and widgets.

**Device Implementations**
    Concrete implementations for specific biosignal devices from various manufacturers.

**GUI Widgets**
    Ready-to-use PySide6 widgets that provide device control interfaces.

**Constants and Enums**
    Device-specific configuration parameters and enumeration values.

Quick Reference
===============

**Most Common Classes**

.. autosummary::
   :nosignatures:

   biosignal_device_interface.devices.BaseDevice
   biosignal_device_interface.devices.OTBMuovi
   biosignal_device_interface.devices.OTBQuattrocento
   biosignal_device_interface.gui.BaseDeviceWidget
   biosignal_device_interface.gui.OTBMuoviWidget

**Key Methods**

.. autosummary::
   :nosignatures:

   biosignal_device_interface.devices.BaseDevice.toggle_connection
   biosignal_device_interface.devices.BaseDevice.configure_device
   biosignal_device_interface.devices.BaseDevice.toggle_streaming
   biosignal_device_interface.devices.BaseDevice.get_device_information

**Important Signals**

.. autosummary::
   :nosignatures:

   biosignal_device_interface.devices.BaseDevice.data_available
   biosignal_device_interface.devices.BaseDevice.biosignal_data_available
   biosignal_device_interface.devices.BaseDevice.connect_toggled
   biosignal_device_interface.devices.BaseDevice.stream_toggled

Usage Patterns
==============

**Basic Device Usage**

.. code-block:: python

    from biosignal_device_interface.devices import OTBMuovi
    
    # Create and connect
    device = OTBMuovi()
    device.toggle_connection(("192.168.1.100", 45454))
    
    # Configure and start streaming
    device.configure_device(config)
    device.toggle_streaming()

**GUI Widget Usage**

.. code-block:: python

    from biosignal_device_interface.gui import OTBMuoviWidget
    from PySide6.QtWidgets import QApplication, QMainWindow
    
    app = QApplication([])
    window = QMainWindow()
    widget = OTBMuoviWidget()
    window.setCentralWidget(widget)
    window.show()

**Signal Connections**

.. code-block:: python

    # Connect to data signals
    device.data_available.connect(handle_data)
    device.biosignal_data_available.connect(handle_biosignal)
    
    # Connect to status signals
    device.connect_toggled.connect(handle_connection)
    device.stream_toggled.connect(handle_streaming)

.. toctree::
   :maxdepth: 2
   :hidden:

   devices
   gui
   constants
   utilities 