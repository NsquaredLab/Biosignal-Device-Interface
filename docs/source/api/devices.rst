=======
Devices
=======

This section documents the device classes and interfaces for biosignal acquisition devices.

Base Classes
============

BaseDevice
-----------

The abstract base class that defines the common interface for all biosignal devices.

.. autoclass:: biosignal_device_interface.devices.core.base_device.BaseDevice
   :members:
   :undoc-members:
   :show-inheritance:

   .. rubric:: Key Methods

   .. autosummary::
      :nosignatures:

      ~BaseDevice.toggle_connection
      ~BaseDevice.configure_device
      ~BaseDevice.toggle_streaming
      ~BaseDevice.get_device_information
      ~BaseDevice.is_connected
      ~BaseDevice.is_streaming

   .. rubric:: Signals

   .. autosummary::
      :nosignatures:

      ~BaseDevice.data_available
      ~BaseDevice.biosignal_data_available
      ~BaseDevice.auxiliary_data_available
      ~BaseDevice.connect_toggled
      ~BaseDevice.configure_toggled
      ~BaseDevice.stream_toggled

OT Bioelettronica Devices
==========================

OTBMuovi
--------

Implementation for Muovi and Muovi Plus wireless EMG devices.

.. autoclass:: biosignal_device_interface.devices.otb.otb_muovi.OTBMuovi
   :members:
   :undoc-members:
   :show-inheritance:

   **Usage Example:**

   .. code-block:: python

       from biosignal_device_interface.devices import OTBMuovi
       from biosignal_device_interface.constants.devices.otb.otb_muovi_constants import (
           MuoviWorkingMode, MuoviDetectionMode
       )

       # Create device instance
       device = OTBMuovi(is_muovi_plus=False)  # False for Muovi, True for Muovi Plus

       # Connect to device
       success = device.toggle_connection(("192.168.1.100", 45454))

       if success:
           # Configure device
           config = {
               "working_mode": MuoviWorkingMode.EMG,
               "detection_mode": MuoviDetectionMode.MONOPOLAR_GAIN_4,
               "sampling_rate": 2000
           }
           device.configure_device(config)
           
           # Start streaming
           device.toggle_streaming()

   **Configuration Parameters:**

   .. list-table::
      :header-rows: 1
      :widths: 25 25 50

      * - Parameter
        - Type
        - Description
      * - ``working_mode``
        - :class:`~biosignal_device_interface.constants.devices.otb.otb_muovi_constants.MuoviWorkingMode`
        - Signal acquisition mode (EMG, EEG, etc.)
      * - ``detection_mode``
        - :class:`~biosignal_device_interface.constants.devices.otb.otb_muovi_constants.MuoviDetectionMode`
        - Electrode configuration and gain settings
      * - ``sampling_rate``
        - int
        - Data acquisition frequency in Hz (up to 2048)
      * - ``channels``
        - list[int]
        - List of channel indices to enable
      * - ``is_muovi_plus``
        - bool
        - True for Muovi Plus (64 ch), False for Muovi (32 ch)

OTBQuattrocento
---------------

Implementation for Quattrocento high-density EMG devices.

.. autoclass:: biosignal_device_interface.devices.otb.otb_quattrocento.OTBQuattrocento
   :members:
   :undoc-members:
   :show-inheritance:

   **Usage Example:**

   .. code-block:: python

       from biosignal_device_interface.devices import OTBQuattrocento
       from biosignal_device_interface.constants.devices.otb.otb_quattrocento_constants import (
           QuattrocentoWorkingMode, QuattrocentoDetectionMode
       )

       # Create device instance
       device = OTBQuattrocento()

       # Connect to device
       success = device.toggle_connection(("192.168.1.200", 31000))

       if success:
           # Configure for high-density EMG
           config = {
               "working_mode": QuattrocentoWorkingMode.EMG_HD,
               "detection_mode": QuattrocentoDetectionMode.MONOPOLAR,
               "sampling_rate": 2048,
               "amplifier_gain": 150,
               "channels": list(range(64))
           }
           device.configure_device(config)
           device.toggle_streaming()

   **Configuration Parameters:**

   .. list-table::
      :header-rows: 1
      :widths: 25 25 50

      * - Parameter
        - Type
        - Description
      * - ``working_mode``
        - :class:`~biosignal_device_interface.constants.devices.otb.otb_quattrocento_constants.QuattrocentoWorkingMode`
        - Signal acquisition mode
      * - ``detection_mode``
        - :class:`~biosignal_device_interface.constants.devices.otb.otb_quattrocento_constants.QuattrocentoDetectionMode`
        - Electrode configuration
      * - ``sampling_rate``
        - int
        - Data acquisition frequency in Hz (up to 10240)
      * - ``amplifier_gain``
        - int
        - Hardware amplifier gain (150, 500, 1000, 2000, 5000)
      * - ``channels``
        - list[int]
        - List of channel indices to enable (up to 408)
      * - ``common_mode_rejection``
        - bool
        - Enable common mode rejection

OTBQuattrocentoLight
--------------------

Implementation for Quattrocento Light compact EMG devices.

.. autoclass:: biosignal_device_interface.devices.otb.otb_quattrocento_light.OTBQuattrocentoLight
   :members:
   :undoc-members:
   :show-inheritance:

   **Usage Example:**

   .. code-block:: python

       from biosignal_device_interface.devices import OTBQuattrocentoLight

       # Create device instance
       device = OTBQuattrocentoLight()

       # Connect via USB or Ethernet
       success = device.toggle_connection("USB")  # or ("192.168.1.201", 31000)

       if success:
           config = {
               "working_mode": QuattrocentoWorkingMode.EMG,
               "detection_mode": QuattrocentoDetectionMode.MONOPOLAR,
               "sampling_rate": 2048,
               "channels": list(range(32))
           }
           device.configure_device(config)
           device.toggle_streaming()

Device Factory
==============

DeviceFactory
-------------

Factory class for creating device instances based on device type.

.. autoclass:: biosignal_device_interface.devices.DeviceFactory
   :members:
   :undoc-members:

   **Usage Example:**

   .. code-block:: python

       from biosignal_device_interface.devices import DeviceFactory

       # Create device using factory
       device = DeviceFactory.create_device("OTBMuovi", is_muovi_plus=False)
       
       # Or with configuration
       config = {
           "device_type": "OTBMuovi",
           "is_muovi_plus": True,
           "connection": ("192.168.1.100", 45454)
       }
       device = DeviceFactory.create_from_config(config)

Connection Management
=====================

Connection Types
----------------

The package supports multiple connection types:

**TCP/IP Connection**

.. code-block:: python

    # Standard TCP/IP connection
    device.toggle_connection(("192.168.1.100", 45454))

**USB Connection**

.. code-block:: python

    # USB connection (device-specific)
    device.toggle_connection("USB")

**Serial Connection**

.. code-block:: python

    # Serial connection
    device.toggle_connection(("COM3", 115200))  # Windows
    device.toggle_connection(("/dev/ttyUSB0", 115200))  # Linux

Connection States
-----------------

Devices can be in one of several connection states:

.. autoclass:: biosignal_device_interface.devices.ConnectionState
   :members:
   :undoc-members:

Data Handling
=============

Data Types
----------

The package handles different types of biosignal data:

.. autoclass:: biosignal_device_interface.devices.DataType
   :members:
   :undoc-members:

Data Processing
---------------

Base data processing functionality:

.. autofunction:: biosignal_device_interface.devices.process_biosignal_data

.. autofunction:: biosignal_device_interface.devices.convert_to_millivolts

.. autofunction:: biosignal_device_interface.devices.extract_channels

Error Handling
==============

Device Exceptions
-----------------

Custom exceptions for device-related errors:

.. autoexception:: biosignal_device_interface.devices.DeviceError
   :members:

.. autoexception:: biosignal_device_interface.devices.ConnectionError
   :members:

.. autoexception:: biosignal_device_interface.devices.ConfigurationError
   :members:

.. autoexception:: biosignal_device_interface.devices.StreamingError
   :members:

Utility Functions
=================

Network Utilities
-----------------

.. autofunction:: biosignal_device_interface.devices.check_valid_ip

.. autofunction:: biosignal_device_interface.devices.check_valid_port

.. autofunction:: biosignal_device_interface.devices.test_network_connection

Device Discovery
----------------

.. autofunction:: biosignal_device_interface.devices.discover_devices

.. autofunction:: biosignal_device_interface.devices.scan_network_for_devices

Examples
========

Basic Device Usage
------------------

.. code-block:: python

    from biosignal_device_interface.devices import OTBMuovi
    from biosignal_device_interface.constants.devices.otb.otb_muovi_constants import (
        MuoviWorkingMode, MuoviDetectionMode
    )

    # Create and configure device
    device = OTBMuovi(is_muovi_plus=False)
    
    # Connect
    if device.toggle_connection(("192.168.1.100", 45454)):
        print("Connected successfully")
        
        # Configure
        config = {
            "working_mode": MuoviWorkingMode.EMG,
            "detection_mode": MuoviDetectionMode.MONOPOLAR_GAIN_4,
            "sampling_rate": 2000
        }
        device.configure_device(config)
        
        # Start streaming
        device.toggle_streaming()
    else:
        print("Connection failed")

Data Handling Example
---------------------

.. code-block:: python

    import numpy as np

    def handle_data(data):
        """Process incoming biosignal data"""
        print(f"Received data shape: {data.shape}")
        
        # Basic signal processing
        mean_values = np.mean(data, axis=1)
        std_values = np.std(data, axis=1)
        
        print(f"Channel means: {mean_values}")
        print(f"Channel std: {std_values}")

    def handle_emg_data(emg_data):
        """Process EMG-specific data"""
        # Calculate RMS for each channel
        rms_values = np.sqrt(np.mean(emg_data**2, axis=1))
        print(f"EMG RMS values: {rms_values}")

    # Connect signal handlers
    device.data_available.connect(handle_data)
    device.biosignal_data_available.connect(handle_emg_data)

Multi-Device Setup
------------------

.. code-block:: python

    from biosignal_device_interface.devices import OTBMuovi, OTBQuattrocento

    # Create multiple devices
    muovi = OTBMuovi(is_muovi_plus=False)
    quattrocento = OTBQuattrocento()

    # Connect devices
    devices = [muovi, quattrocento]
    connections = [
        ("192.168.1.100", 45454),
        ("192.168.1.200", 31000)
    ]

    for device, connection in zip(devices, connections):
        if device.toggle_connection(connection):
            print(f"Connected to {device.__class__.__name__}")
            device.toggle_streaming()
        else:
            print(f"Failed to connect to {device.__class__.__name__}")

Error Handling Example
----------------------

.. code-block:: python

    from biosignal_device_interface.devices import (
        OTBMuovi, DeviceError, ConnectionError, ConfigurationError
    )

    try:
        device = OTBMuovi()
        
        # Attempt connection with error handling
        if not device.toggle_connection(("192.168.1.100", 45454)):
            raise ConnectionError("Failed to connect to device")
        
        # Configure with validation
        config = {
            "working_mode": MuoviWorkingMode.EMG,
            "detection_mode": MuoviDetectionMode.MONOPOLAR_GAIN_4,
            "sampling_rate": 2000
        }
        
        if not device.configure_device(config):
            raise ConfigurationError("Failed to configure device")
        
        # Start streaming
        device.toggle_streaming()
        
    except ConnectionError as e:
        print(f"Connection error: {e}")
    except ConfigurationError as e:
        print(f"Configuration error: {e}")
    except DeviceError as e:
        print(f"Device error: {e}")
    finally:
        # Cleanup
        if 'device' in locals() and device.is_connected():
            device.toggle_streaming()  # Stop streaming
            device.toggle_connection(None)  # Disconnect 