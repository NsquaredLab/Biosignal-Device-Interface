=========
Utilities
=========

This section documents utility functions and helper classes used throughout the biosignal device interface.

Data Processing Utilities
==========================

Signal Processing Functions
----------------------------

Functions for processing biosignal data are available as methods on device instances.

.. automethod:: biosignal_device_interface.devices.core.base_device.BaseDevice.extract_biosignal_data

.. automethod:: biosignal_device_interface.devices.core.base_device.BaseDevice.extract_auxiliary_data

Network Utilities
=================

Connection Helper Functions
---------------------------

Functions for network connection management and validation.

.. automethod:: biosignal_device_interface.devices.core.base_device.BaseDevice.check_valid_ip

.. automethod:: biosignal_device_interface.devices.core.base_device.BaseDevice.check_valid_port

.. automethod:: biosignal_device_interface.devices.core.base_device.BaseDevice.get_server_wifi_ip_address

Device Management
=================

Device Information and Control
------------------------------

Methods for managing device connections and retrieving device information.

.. automethod:: biosignal_device_interface.devices.core.base_device.BaseDevice.toggle_connection

.. automethod:: biosignal_device_interface.devices.core.base_device.BaseDevice.toggle_streaming

.. automethod:: biosignal_device_interface.devices.core.base_device.BaseDevice.get_device_information

.. automethod:: biosignal_device_interface.devices.core.base_device.BaseDevice.configure_device 