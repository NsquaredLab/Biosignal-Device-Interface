# Biosignal Device Interface Documentation

## Overview

The Biosignal Device Interface is a Python package that provides a unified communication interface for biosignal devices manufactured by several companies. It is specifically designed for easy integration in custom PySide6 applications and offers real-time data acquisition capabilities.

## Features

- **Real-time Communication**: Low-latency data streaming from biosignal devices
- **PySide6 Integration**: Ready-to-use GUI widgets for device control
- **Multiple Device Support**: Standardized interface for various device types
- **Signal Processing**: Built-in data conversion and processing capabilities
- **Extensible Architecture**: Easy to add support for new devices

## Supported Devices

### OT Bioelettronica Devices

| Device | Channels | Description |
|--------|----------|-------------|
| Muovi | 32 | Wireless EMG acquisition system |
| Muovi Plus | 64 | Enhanced wireless EMG system |
| Quattrocento | up to 408 | High-density EMG system |
| Quattrocento Light | up to 64 | Compact EMG system |
| SyncStation | - | Synchronization device |

## Installation

### Using Poetry (Recommended)

```bash
# Clone the repository
git clone https://github.com/NsquaredLab/Biosignal-Device-Interface.git
cd Biosignal-Device-Interface

# Install dependencies
poetry install

# For development
poetry install --with dev,docs
```

### Using pip

```bash
pip install git+https://github.com/NsquaredLab/Biosignal-Device-Interface.git
```

## Quick Start

### Basic Device Integration

```python
from biosignal_device_interface.devices import OTBMuoviWidget
from PySide6.QtWidgets import QApplication, QMainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Create device widget
        self.device_widget = OTBMuoviWidget(self)
        
        # Connect signals
        self.device_widget.data_arrived.connect(self.handle_data)
        self.device_widget.biosignal_data_arrived.connect(self.handle_emg_data)
        
        # Set as central widget
        self.setCentralWidget(self.device_widget)
    
    def handle_data(self, data):
        print(f"Received data: {data.shape}")
    
    def handle_emg_data(self, emg_data):
        print(f"EMG data: {emg_data.shape}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
```

### Using Device Classes Directly

```python
from biosignal_device_interface.devices import OTBMuovi
from biosignal_device_interface.constants.devices.otb.otb_muovi_constants import (
    MuoviWorkingMode, 
    MuoviDetectionMode
)

# Create device instance
device = OTBMuovi(is_muovi_plus=False)

# Connect to device
success = device.toggle_connection(("192.168.1.100", 45454))

if success:
    # Configure device
    config = {
        "working_mode": MuoviWorkingMode.EMG,
        "detection_mode": MuoviDetectionMode.MONOPOLAR_GAIN_4
    }
    device.configure_device(config)
    
    # Start streaming
    device.toggle_streaming()
```

## Architecture

### Core Components

#### BaseDevice Class

The `BaseDevice` class is the abstract base class for all device implementations. It provides:

- Connection management (TCP/IP, UDP, Serial)
- Configuration parameter handling
- Real-time data streaming
- Signal emission for GUI integration
- Data processing and conversion

#### Device-Specific Implementations

Each supported device has its own implementation class that inherits from `BaseDevice`:

- `OTBMuovi`: Muovi and Muovi Plus devices
- `OTBQuattrocento`: Quattrocento devices
- `OTBQuattrocentoLight`: Quattrocento Light devices

#### GUI Widgets

Pre-built PySide6 widgets for each device type:

- `OTBMuoviWidget`: GUI for Muovi devices
- `OTBMuoviPlusWidget`: GUI for Muovi Plus devices
- `OTBQuattrocentoLightWidget`: GUI for Quattrocento Light devices
- `AllDevicesWidget`: Multi-device interface

### Signal Flow

```
Device Hardware → TCP/IP/Serial → BaseDevice → Data Processing → Qt Signals → GUI/Application
```

## Configuration

### Device Configuration

Each device supports various configuration parameters:

```python
# Muovi configuration example
config = {
    "working_mode": MuoviWorkingMode.EMG,  # EMG, EEG, etc.
    "detection_mode": MuoviDetectionMode.MONOPOLAR_GAIN_4  # Gain settings
}
device.configure_device(config)
```

### Connection Settings

Different connection types require different settings:

```python
# TCP/IP connection
tcp_settings = ("192.168.1.100", 45454)  # (IP, Port)

# Serial connection  
serial_settings = ("COM3", 115200)  # (Port, Baudrate)

device.toggle_connection(tcp_settings)
```

## Data Processing

### Data Types

The package handles different types of data:

- **Biosignal Data**: EMG, EEG, and other physiological signals
- **Auxiliary Data**: Accelerometer, gyroscope, and other sensor data
- **Raw Data**: Unprocessed data from the device

### Data Conversion

Data is automatically converted to appropriate units:

```python
# Data is converted to millivolts by default
biosignal_data = device._extract_biosignal_data(raw_data, milli_volts=True)
auxiliary_data = device._extract_auxiliary_data(raw_data, milli_volts=True)
```

### Signal Emission

The package uses Qt signals for real-time data distribution:

```python
# Connect to data signals
device.data_available.connect(handle_all_data)
device.biosignal_data_available.connect(handle_biosignal_data)
device.auxiliary_data_available.connect(handle_auxiliary_data)

# Connect to status signals
device.connect_toggled.connect(handle_connection_status)
device.configure_toggled.connect(handle_configuration_status)
device.stream_toggled.connect(handle_streaming_status)
```

## Examples

### Example 1: Single Device Integration

See `examples/1_integrating_a_device.py` for a complete example of integrating a single device.

### Example 2: Multiple Devices

See `examples/2_integrating_multiple_devices.py` for handling multiple devices simultaneously.

### Example 3: Real-time Plotting

See `examples/3_integrating_device_interface_and_biosignal_plot.py` for real-time data visualization.

### Example 4: Custom Device Implementation

See `examples/4_implementing_new_device.py` for adding support for new devices.

## API Reference

### BaseDevice

The core abstract base class for all device implementations.

#### Methods

- `toggle_connection(settings)`: Connect/disconnect to/from device
- `configure_device(params)`: Configure device parameters
- `toggle_streaming()`: Start/stop data streaming
- `get_device_information()`: Get current device configuration
- `check_valid_ip(ip_address)`: Validate IP address
- `check_valid_port(port)`: Validate port number

#### Signals

- `connect_toggled(bool)`: Connection status changed
- `configure_toggled(bool)`: Configuration status changed
- `stream_toggled(bool)`: Streaming status changed
- `data_available(np.ndarray)`: New data available
- `biosignal_data_available(np.ndarray)`: New biosignal data
- `auxiliary_data_available(np.ndarray)`: New auxiliary data

### OTBMuovi

Muovi and Muovi Plus device implementation.

#### Configuration Parameters

- `working_mode`: EMG, EEG, etc.
- `detection_mode`: Gain and detection settings

#### Connection

Uses TCP/IP protocol where the application acts as a server and the device connects as a client.

## Troubleshooting

### Common Issues

1. **Connection Timeout**
   - Check IP address and port settings
   - Ensure device is powered on and in range
   - Verify network connectivity

2. **No Data Received**
   - Verify device configuration
   - Check if streaming is started
   - Ensure proper signal connections

3. **Data Corruption**
   - Check buffer sizes
   - Verify data processing parameters
   - Ensure stable connection

### Debug Mode

Enable debug logging for troubleshooting:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Contributing

### Adding New Devices

1. Create a new device class inheriting from `BaseDevice`
2. Implement all abstract methods
3. Add device constants and enums
4. Create corresponding GUI widget
5. Add tests and documentation

### Development Setup

```bash
# Install development dependencies
poetry install --with dev,docs

# Run tests
pytest

# Build documentation
sphinx-build -b html docs docs/_build
```

## License

This project is licensed under the CC BY-SA 4.0 License. See the LICENSE file for details.

## Contact

**Author**: Dominik I. Braun  
**Email**: dome.braun@fau.de  
**Institution**: n-squared lab, Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU)

## Acknowledgments

- OT Bioelettronica for device specifications and support
- n-squared lab team for development and testing
- Contributors and users for feedback and improvements 