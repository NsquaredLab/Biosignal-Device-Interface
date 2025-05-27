=======
Devices
=======

This guide provides detailed information about all supported biosignal acquisition devices and their specific capabilities.

Supported Manufacturers
========================

The Biosignal Device Interface currently supports devices from the following manufacturers:

.. grid:: 1 1 1 1
    :gutter: 2

    .. grid-item-card:: 🏭 OT Bioelettronica
        
        Italian manufacturer specializing in high-quality EMG and biosignal acquisition systems.
        
        **Supported Devices:**
        - Muovi (32 channels)
        - Muovi Plus (64 channels)  
        - Quattrocento (up to 408 channels)
        - Quattrocento Light (up to 64 channels)
        - SyncStation (synchronization)

OT Bioelettronica Devices
==========================

Muovi Series
------------

The Muovi series consists of wireless EMG acquisition systems designed for research and clinical applications.

**Muovi (32 channels)**

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Specification
     - Value
   * - Channels
     - 32 monopolar/16 bipolar
   * - Sampling Rate
     - Up to 2048 Hz
   * - Resolution
     - 16-bit
   * - Input Range
     - ±5 mV
   * - Gain
     - 1, 2, 4, 8, 16
   * - Connectivity
     - Wi-Fi (TCP/IP)
   * - Battery Life
     - ~8 hours continuous
   * - Weight
     - 85g

**Muovi Plus (64 channels)**

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Specification
     - Value
   * - Channels
     - 64 monopolar/32 bipolar
   * - Sampling Rate
     - Up to 2048 Hz
   * - Resolution
     - 16-bit
   * - Input Range
     - ±5 mV
   * - Gain
     - 1, 2, 4, 8, 16
   * - Connectivity
     - Wi-Fi (TCP/IP)
   * - Battery Life
     - ~6 hours continuous
   * - Weight
     - 120g

**Usage Example:**

.. code-block:: python

    from biosignal_device_interface.devices import OTBMuovi
    from biosignal_device_interface.constants.devices.otb.otb_muovi_constants import (
        MuoviWorkingMode, MuoviDetectionMode
    )

    # Create Muovi device (32 channels)
    muovi = OTBMuovi(is_muovi_plus=False)
    
    # Create Muovi Plus device (64 channels)
    muovi_plus = OTBMuovi(is_muovi_plus=True)
    
    # Connect to device
    success = muovi.toggle_connection(("192.168.1.100", 45454))
    
    if success:
        # Configure for EMG acquisition
        config = {
            "working_mode": MuoviWorkingMode.EMG,
            "detection_mode": MuoviDetectionMode.MONOPOLAR_GAIN_4,
            "sampling_rate": 2000
        }
        muovi.configure_device(config)
        muovi.toggle_streaming()

Quattrocento Series
-------------------

The Quattrocento series provides high-density EMG acquisition for advanced research applications.

**Quattrocento (up to 408 channels)**

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Specification
     - Value
   * - Channels
     - Up to 408 (expandable)
   * - Sampling Rate
     - Up to 10240 Hz
   * - Resolution
     - 16-bit
   * - Input Range
     - ±5 mV
   * - Gain
     - 150, 500, 1000, 2000, 5000
   * - Connectivity
     - Ethernet (TCP/IP)
   * - Synchronization
     - Hardware sync capability
   * - Form Factor
     - Desktop unit

**Quattrocento Light (up to 64 channels)**

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Specification
     - Value
   * - Channels
     - Up to 64
   * - Sampling Rate
     - Up to 10240 Hz
   * - Resolution
     - 16-bit
   * - Input Range
     - ±5 mV
   * - Gain
     - 150, 500, 1000, 2000, 5000
   * - Connectivity
     - USB 3.0 / Ethernet
   * - Synchronization
     - Hardware sync capability
   * - Form Factor
     - Compact desktop unit

**Usage Example:**

.. code-block:: python

    from biosignal_device_interface.devices import OTBQuattrocento
    from biosignal_device_interface.constants.devices.otb.otb_quattrocento_constants import (
        QuattrocentoWorkingMode, QuattrocentoDetectionMode
    )

    # Create Quattrocento device
    quattrocento = OTBQuattrocento()
    
    # Connect to device
    success = quattrocento.toggle_connection(("192.168.1.200", 31000))
    
    if success:
        # Configure for high-density EMG
        config = {
            "working_mode": QuattrocentoWorkingMode.EMG_HD,
            "detection_mode": QuattrocentoDetectionMode.MONOPOLAR,
            "sampling_rate": 2048,
            "amplifier_gain": 150,
            "channels": list(range(64))  # First 64 channels
        }
        quattrocento.configure_device(config)
        quattrocento.toggle_streaming()

SyncStation
-----------

The SyncStation provides precise synchronization between multiple devices and external equipment.

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Specification
     - Value
   * - Sync Outputs
     - 8 TTL outputs
   * - Sync Inputs
     - 4 TTL inputs
   * - Timing Accuracy
     - <1 μs
   * - Connectivity
     - Ethernet
   * - Protocols
     - TCP/IP, UDP
   * - External Triggers
     - Configurable

**Usage Example:**

.. code-block:: python

    from biosignal_device_interface.devices import OTBSyncStation

    # Create SyncStation device
    sync_station = OTBSyncStation()
    
    # Connect to device
    success = sync_station.toggle_connection(("192.168.1.201", 31001))
    
    if success:
        # Configure synchronization
        config = {
            "sync_mode": "master",
            "trigger_outputs": [1, 2, 3],  # Enable outputs 1, 2, 3
            "external_trigger": True
        }
        sync_station.configure_device(config)

Device Selection Guide
======================

Choosing the Right Device
-------------------------

**For Basic EMG Research (≤32 channels):**
    - **Muovi**: Ideal for gait analysis, basic muscle activation studies
    - Wireless, portable, good battery life
    - Perfect for field studies and clinical applications

**For Advanced EMG Research (32-64 channels):**
    - **Muovi Plus**: Extended channel count while maintaining portability
    - **Quattrocento Light**: Higher sampling rates, better for detailed analysis
    - Choose Muovi Plus for mobility, Quattrocento Light for precision

**For High-Density EMG (>64 channels):**
    - **Quattrocento**: Maximum channel count and sampling rate
    - Essential for motor unit decomposition and detailed muscle analysis
    - Required for research-grade high-density surface EMG

**For Multi-Device Setups:**
    - **SyncStation**: Ensures precise timing across multiple devices
    - Critical for biomechanics labs with multiple measurement systems
    - Enables integration with motion capture, force plates, etc.

Application-Specific Recommendations
------------------------------------

**Clinical Gait Analysis:**

.. code-block:: python

    # Recommended setup: Muovi for mobility
    device = OTBMuovi(is_muovi_plus=False)
    config = {
        "working_mode": MuoviWorkingMode.EMG,
        "detection_mode": MuoviDetectionMode.MONOPOLAR_GAIN_4,
        "sampling_rate": 1000,  # Sufficient for gait analysis
        "channels": [0, 1, 2, 3, 4, 5, 6, 7]  # 8 muscles
    }

**Sports Biomechanics:**

.. code-block:: python

    # Recommended setup: Muovi Plus for more muscles
    device = OTBMuovi(is_muovi_plus=True)
    config = {
        "working_mode": MuoviWorkingMode.EMG,
        "detection_mode": MuoviDetectionMode.MONOPOLAR_GAIN_4,
        "sampling_rate": 2000,  # Higher rate for dynamic movements
        "channels": list(range(16))  # 16 muscles
    }

**Motor Unit Research:**

.. code-block:: python

    # Recommended setup: Quattrocento for high-density
    device = OTBQuattrocento()
    config = {
        "working_mode": QuattrocentoWorkingMode.EMG_HD,
        "detection_mode": QuattrocentoDetectionMode.MONOPOLAR,
        "sampling_rate": 2048,  # High sampling rate
        "amplifier_gain": 150,
        "channels": list(range(64))  # High-density grid
    }

Device Comparison
=================

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 15 15 20

   * - Feature
     - Muovi
     - Muovi Plus
     - Quattrocento Light
     - Quattrocento
     - Best For
   * - Channels
     - 32
     - 64
     - 64
     - 408
     - More = better resolution
   * - Portability
     - ⭐⭐⭐⭐⭐
     - ⭐⭐⭐⭐
     - ⭐⭐
     - ⭐
     - Field studies
   * - Sampling Rate
     - 2048 Hz
     - 2048 Hz
     - 10240 Hz
     - 10240 Hz
     - Research precision
   * - Battery Life
     - 8h
     - 6h
     - N/A
     - N/A
     - Long recordings
   * - Price Range
     - €€
     - €€€
     - €€€€
     - €€€€€
     - Budget considerations

Connection Types
================

TCP/IP (Ethernet/Wi-Fi)
------------------------

Most OT Bioelettronica devices use TCP/IP for communication:

.. code-block:: python

    # Standard TCP/IP connection
    device.toggle_connection(("192.168.1.100", 45454))
    
    # Check connection status
    if device.is_connected():
        print("Device connected successfully")

**Network Configuration:**

- Devices typically use static IP addresses
- Default ports: 45454 (Muovi), 31000 (Quattrocento)
- Ensure firewall allows communication
- Use dedicated network for best performance

USB (Quattrocento Light)
-------------------------

Some devices support USB connectivity:

.. code-block:: python

    # USB connection (device-specific)
    device.toggle_connection("USB")

Serial Communication
--------------------

For legacy devices or special configurations:

.. code-block:: python

    # Serial connection
    device.toggle_connection(("COM3", 115200))  # Windows
    device.toggle_connection(("/dev/ttyUSB0", 115200))  # Linux

Troubleshooting Device Issues
=============================

Connection Problems
-------------------

**Cannot Connect to Device:**

1. Check IP address and port
2. Verify network connectivity
3. Ensure device is powered on
4. Check firewall settings
5. Try different network interface

.. code-block:: python

    # Test network connectivity
    import socket
    
    def test_connection(ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip, port))
            sock.close()
            return result == 0
        except:
            return False
    
    if test_connection("192.168.1.100", 45454):
        print("Network connection OK")
    else:
        print("Cannot reach device")

**Intermittent Disconnections:**

1. Check Wi-Fi signal strength (wireless devices)
2. Verify power supply stability
3. Reduce network traffic
4. Update device firmware

Data Quality Issues
-------------------

**Noisy Signals:**

1. Check electrode placement and skin preparation
2. Verify gain settings are appropriate
3. Enable hardware filters if available
4. Check for electromagnetic interference

**Missing Data:**

1. Verify sampling rate settings
2. Check buffer sizes
3. Ensure adequate processing power
4. Monitor network bandwidth

**Synchronization Issues:**

1. Use SyncStation for multi-device setups
2. Check system clock synchronization
3. Verify trigger signal connections
4. Monitor timing accuracy

Device Maintenance
==================

Regular Maintenance
-------------------

**Hardware:**
- Clean device housing regularly
- Check cable connections
- Inspect electrodes and connectors
- Calibrate devices annually

**Software:**
- Keep firmware updated
- Update device drivers
- Backup configuration settings
- Monitor performance metrics

**Network:**
- Verify IP address assignments
- Check network performance
- Update network drivers
- Monitor bandwidth usage

Best Practices
==============

1. **Always test connections before important recordings**
2. **Use appropriate sampling rates for your application**
3. **Configure devices consistently across sessions**
4. **Document device settings for reproducibility**
5. **Implement proper error handling in your applications**
6. **Regular calibration and maintenance schedules**
7. **Keep spare cables and electrodes available**

For more detailed troubleshooting, see the :doc:`troubleshooting` guide. 