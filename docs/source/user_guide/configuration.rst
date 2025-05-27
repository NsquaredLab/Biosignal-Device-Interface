=============
Configuration
=============

This guide covers how to configure devices and customize settings for optimal performance with your specific setup.

Device Configuration Overview
==============================

Each device in the Biosignal Device Interface has its own set of configuration parameters. These parameters control:

- **Working Mode**: The type of biosignal to acquire (EMG, EEG, etc.)
- **Detection Mode**: Gain settings and electrode configuration
- **Sampling Rate**: Data acquisition frequency
- **Channel Configuration**: Which channels to enable/disable
- **Filtering**: Hardware filtering options

Configuration Methods
======================

There are several ways to configure devices:

1. **Programmatic Configuration**: Using Python dictionaries
2. **GUI Configuration**: Using the built-in device widgets
3. **Configuration Files**: Using JSON or YAML files
4. **Environment Variables**: For deployment settings

Programmatic Configuration
==========================

OT Bioelettronica Muovi
------------------------

.. code-block:: python

    from biosignal_device_interface.devices import OTBMuovi
    from biosignal_device_interface.constants.devices.otb.otb_muovi_constants import (
        MuoviWorkingMode, 
        MuoviDetectionMode
    )

    device = OTBMuovi(is_muovi_plus=False)

    # EMG Configuration
    emg_config = {
        "working_mode": MuoviWorkingMode.EMG,
        "detection_mode": MuoviDetectionMode.MONOPOLAR_GAIN_4,
        "sampling_rate": 2000,
        "channels": list(range(32)),  # All 32 channels
        "high_pass_filter": 20,       # 20 Hz high-pass
        "low_pass_filter": 500        # 500 Hz low-pass
    }

    # EEG Configuration
    eeg_config = {
        "working_mode": MuoviWorkingMode.EEG,
        "detection_mode": MuoviDetectionMode.MONOPOLAR_GAIN_1,
        "sampling_rate": 1000,
        "channels": list(range(16)),  # First 16 channels
        "high_pass_filter": 0.5,     # 0.5 Hz high-pass
        "low_pass_filter": 100       # 100 Hz low-pass
    }

    # Apply configuration
    device.configure_device(emg_config)

OT Bioelettronica Quattrocento
-------------------------------

.. code-block:: python

    from biosignal_device_interface.devices import OTBQuattrocento
    from biosignal_device_interface.constants.devices.otb.otb_quattrocento_constants import (
        QuattrocentoWorkingMode,
        QuattrocentoDetectionMode
    )

    device = OTBQuattrocento()

    # High-density EMG configuration
    hd_emg_config = {
        "working_mode": QuattrocentoWorkingMode.EMG_HD,
        "detection_mode": QuattrocentoDetectionMode.MONOPOLAR,
        "sampling_rate": 2048,
        "channels": list(range(64)),  # 64 channels
        "amplifier_gain": 150,
        "common_mode_rejection": True
    }

    device.configure_device(hd_emg_config)

Configuration Parameters Reference
===================================

Common Parameters
-----------------

All devices support these common configuration parameters:

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Parameter
     - Type
     - Description
   * - ``working_mode``
     - Enum
     - Type of biosignal (EMG, EEG, etc.)
   * - ``detection_mode``
     - Enum
     - Electrode configuration and gain
   * - ``sampling_rate``
     - int
     - Data acquisition frequency in Hz
   * - ``channels``
     - list[int]
     - List of channel indices to enable
   * - ``buffer_size``
     - int
     - Internal buffer size for data

Device-Specific Parameters
--------------------------

**Muovi/Muovi Plus**

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Parameter
     - Type
     - Description
   * - ``is_muovi_plus``
     - bool
     - True for Muovi Plus (64 ch), False for Muovi (32 ch)
   * - ``wireless_mode``
     - Enum
     - Wireless transmission settings
   * - ``battery_level_check``
     - bool
     - Enable battery level monitoring
   * - ``accelerometer_enabled``
     - bool
     - Enable built-in accelerometer

**Quattrocento/Quattrocento Light**

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Parameter
     - Type
     - Description
   * - ``amplifier_gain``
     - int
     - Hardware amplifier gain (1-10000)
   * - ``common_mode_rejection``
     - bool
     - Enable common mode rejection
   * - ``impedance_check``
     - bool
     - Enable electrode impedance checking
   * - ``sync_mode``
     - Enum
     - Synchronization with other devices

Configuration Files
====================

For complex setups, you can use configuration files:

JSON Configuration
------------------

.. code-block:: json

    {
        "device_type": "OTBMuovi",
        "connection": {
            "ip_address": "192.168.1.100",
            "port": 45454,
            "timeout": 5.0
        },
        "configuration": {
            "working_mode": "EMG",
            "detection_mode": "MONOPOLAR_GAIN_4",
            "sampling_rate": 2000,
            "channels": [0, 1, 2, 3, 4, 5, 6, 7],
            "filters": {
                "high_pass": 20,
                "low_pass": 500,
                "notch": 50
            }
        },
        "data_processing": {
            "buffer_size": 1000,
            "real_time_processing": true,
            "save_raw_data": false
        }
    }

YAML Configuration
------------------

.. code-block:: yaml

    device_type: OTBMuovi
    connection:
      ip_address: "192.168.1.100"
      port: 45454
      timeout: 5.0
    
    configuration:
      working_mode: EMG
      detection_mode: MONOPOLAR_GAIN_4
      sampling_rate: 2000
      channels: [0, 1, 2, 3, 4, 5, 6, 7]
      filters:
        high_pass: 20
        low_pass: 500
        notch: 50
    
    data_processing:
      buffer_size: 1000
      real_time_processing: true
      save_raw_data: false

Loading Configuration Files
----------------------------

.. code-block:: python

    import json
    import yaml
    from biosignal_device_interface.devices import OTBMuovi
    from biosignal_device_interface.constants.devices.otb.otb_muovi_constants import (
        MuoviWorkingMode, MuoviDetectionMode
    )

    def load_json_config(filename):
        """Load configuration from JSON file"""
        with open(filename, 'r') as f:
            config = json.load(f)
        return config

    def load_yaml_config(filename):
        """Load configuration from YAML file"""
        with open(filename, 'r') as f:
            config = yaml.safe_load(f)
        return config

    def apply_config_from_file(device, config_file):
        """Apply configuration from file to device"""
        if config_file.endswith('.json'):
            config = load_json_config(config_file)
        elif config_file.endswith('.yaml') or config_file.endswith('.yml'):
            config = load_yaml_config(config_file)
        else:
            raise ValueError("Unsupported config file format")
        
        # Convert string enums to actual enum values
        if 'working_mode' in config['configuration']:
            config['configuration']['working_mode'] = getattr(
                MuoviWorkingMode, config['configuration']['working_mode']
            )
        
        if 'detection_mode' in config['configuration']:
            config['configuration']['detection_mode'] = getattr(
                MuoviDetectionMode, config['configuration']['detection_mode']
            )
        
        # Apply configuration
        device.configure_device(config['configuration'])
        
        return config

    # Usage
    device = OTBMuovi()
    config = apply_config_from_file(device, 'muovi_config.json')

Environment Variables
=====================

For deployment and CI/CD scenarios, you can use environment variables:

.. code-block:: python

    import os
    from biosignal_device_interface.devices import OTBMuovi

    def get_config_from_env():
        """Get configuration from environment variables"""
        return {
            "ip_address": os.getenv("DEVICE_IP", "192.168.1.100"),
            "port": int(os.getenv("DEVICE_PORT", "45454")),
            "sampling_rate": int(os.getenv("SAMPLING_RATE", "2000")),
            "channels": list(map(int, os.getenv("CHANNELS", "0,1,2,3").split(","))),
            "working_mode": os.getenv("WORKING_MODE", "EMG"),
            "detection_mode": os.getenv("DETECTION_MODE", "MONOPOLAR_GAIN_4")
        }

    # Usage
    config = get_config_from_env()
    device = OTBMuovi()
    device.toggle_connection((config["ip_address"], config["port"]))

GUI Configuration
=================

The device widgets provide intuitive GUI configuration:

.. code-block:: python

    from biosignal_device_interface.gui import OTBMuoviWidget
    from PySide6.QtWidgets import QApplication, QMainWindow

    class ConfigurableDeviceWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Device Configuration")
            
            # Create device widget with configuration panel
            self.device_widget = OTBMuoviWidget(self, show_config_panel=True)
            self.setCentralWidget(self.device_widget)
            
            # Connect configuration signals
            self.device_widget.configuration_changed.connect(self.on_config_changed)
        
        def on_config_changed(self, new_config):
            """Handle configuration changes from GUI"""
            print(f"Configuration updated: {new_config}")
            # Save configuration or apply additional processing

Advanced Configuration
======================

Custom Configuration Classes
-----------------------------

For complex applications, create custom configuration classes:

.. code-block:: python

    from dataclasses import dataclass
    from typing import List, Optional
    from biosignal_device_interface.constants.devices.otb.otb_muovi_constants import (
        MuoviWorkingMode, MuoviDetectionMode
    )

    @dataclass
    class MuoviConfiguration:
        """Configuration class for Muovi devices"""
        working_mode: MuoviWorkingMode = MuoviWorkingMode.EMG
        detection_mode: MuoviDetectionMode = MuoviDetectionMode.MONOPOLAR_GAIN_4
        sampling_rate: int = 2000
        channels: List[int] = None
        high_pass_filter: float = 20.0
        low_pass_filter: float = 500.0
        notch_filter: Optional[float] = 50.0
        buffer_size: int = 1000
        
        def __post_init__(self):
            if self.channels is None:
                self.channels = list(range(32))  # Default to all channels
        
        def to_dict(self):
            """Convert to dictionary for device configuration"""
            return {
                "working_mode": self.working_mode,
                "detection_mode": self.detection_mode,
                "sampling_rate": self.sampling_rate,
                "channels": self.channels,
                "high_pass_filter": self.high_pass_filter,
                "low_pass_filter": self.low_pass_filter,
                "notch_filter": self.notch_filter,
                "buffer_size": self.buffer_size
            }
        
        @classmethod
        def from_dict(cls, config_dict):
            """Create configuration from dictionary"""
            return cls(**config_dict)

    # Usage
    config = MuoviConfiguration(
        sampling_rate=1000,
        channels=[0, 1, 2, 3],
        high_pass_filter=10.0
    )
    
    device = OTBMuovi()
    device.configure_device(config.to_dict())

Configuration Validation
-------------------------

Implement configuration validation to prevent errors:

.. code-block:: python

    def validate_muovi_config(config):
        """Validate Muovi configuration parameters"""
        errors = []
        
        # Check sampling rate
        if config.get("sampling_rate", 0) not in [500, 1000, 2000, 4000]:
            errors.append("Invalid sampling rate. Must be 500, 1000, 2000, or 4000 Hz")
        
        # Check channels
        channels = config.get("channels", [])
        if not all(0 <= ch <= 31 for ch in channels):
            errors.append("Invalid channel numbers. Must be between 0 and 31")
        
        # Check filter frequencies
        hp_freq = config.get("high_pass_filter", 0)
        lp_freq = config.get("low_pass_filter", 1000)
        
        if hp_freq >= lp_freq:
            errors.append("High-pass frequency must be less than low-pass frequency")
        
        if errors:
            raise ValueError("Configuration validation failed:\n" + "\n".join(errors))
        
        return True

    # Usage
    try:
        validate_muovi_config(config_dict)
        device.configure_device(config_dict)
    except ValueError as e:
        print(f"Configuration error: {e}")

Best Practices
==============

1. **Start with Default Configurations**: Use the device's default settings as a starting point
2. **Validate Parameters**: Always validate configuration parameters before applying
3. **Save Configurations**: Save working configurations for reproducibility
4. **Document Settings**: Document why specific settings were chosen
5. **Test Configurations**: Test configurations with known signals before real experiments
6. **Version Control**: Keep configuration files in version control
7. **Environment-Specific Configs**: Use different configurations for development, testing, and production

Troubleshooting Configuration Issues
====================================

**Configuration Not Applied**
    - Check if device is connected before configuring
    - Verify parameter names and values
    - Check device-specific parameter limits

**Invalid Parameter Values**
    - Consult device documentation for valid ranges
    - Use enum values instead of strings where required
    - Check data types (int vs float vs string)

**Performance Issues**
    - Reduce sampling rate if not needed
    - Limit number of active channels
    - Adjust buffer sizes for your application

**Connection Issues After Configuration**
    - Some configuration changes require device restart
    - Check if configuration conflicts with hardware capabilities
    - Verify network settings haven't changed

For more troubleshooting help, see the :doc:`troubleshooting` guide. 