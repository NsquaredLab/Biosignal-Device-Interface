==========
Quick Start
==========

This guide will get you up and running with the Biosignal Device Interface in just a few minutes. We'll walk through connecting to a device, configuring it, and receiving data.

Your First Connection
=====================

Let's start with a simple example using the OT Bioelettronica Muovi device:

.. code-block:: python

    from biosignal_device_interface.devices import OTBMuovi
    from biosignal_device_interface.constants.devices.otb.otb_muovi_constants import (
        MuoviWorkingMode, 
        MuoviDetectionMode
    )

    # Create device instance
    device = OTBMuovi(is_muovi_plus=False)

    # Connect to device (replace with your device's IP)
    success = device.toggle_connection(("192.168.1.100", 45454))

    if success:
        print("✅ Connected to Muovi device!")
        
        # Configure device
        config = {
            "working_mode": MuoviWorkingMode.EMG,
            "detection_mode": MuoviDetectionMode.MONOPOLAR_GAIN_4
        }
        device.configure_device(config)
        
        # Start streaming
        device.toggle_streaming()
        print("📡 Data streaming started!")
    else:
        print("❌ Failed to connect to device")

Using GUI Widgets
==================

For rapid application development, use the pre-built GUI widgets:

.. code-block:: python

    from biosignal_device_interface.devices import OTBMuoviWidget
    from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
    import sys

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Biosignal Device Interface - Quick Start")
            self.setGeometry(100, 100, 800, 600)
            
            # Create central widget and layout
            central_widget = QWidget()
            self.setCentralWidget(central_widget)
            layout = QVBoxLayout(central_widget)
            
            # Create device widget
            self.device_widget = OTBMuoviWidget(self)
            layout.addWidget(self.device_widget)
            
            # Connect signals for data handling
            self.device_widget.data_arrived.connect(self.handle_data)
            self.device_widget.biosignal_data_arrived.connect(self.handle_emg_data)
            self.device_widget.connect_toggled.connect(self.handle_connection)
        
        def handle_data(self, data):
            """Handle all incoming data"""
            print(f"📊 Received data: {data.shape}")
        
        def handle_emg_data(self, emg_data):
            """Handle EMG-specific data"""
            print(f"💪 EMG data: {emg_data.shape}")
            # Process EMG data here
        
        def handle_connection(self, connected):
            """Handle connection status changes"""
            status = "Connected" if connected else "Disconnected"
            print(f"🔌 Device {status}")

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())

Data Processing Example
=======================

Here's how to process the incoming biosignal data:

.. code-block:: python

    import numpy as np
    from scipy import signal
    import matplotlib.pyplot as plt

    class DataProcessor:
        def __init__(self, sampling_rate=2000):
            self.sampling_rate = sampling_rate
            self.buffer = []
            self.buffer_size = 1000  # Store last 1000 samples
        
        def process_emg_data(self, emg_data):
            """Process EMG data with filtering and feature extraction"""
            # Add to buffer
            self.buffer.extend(emg_data.flatten())
            
            # Keep buffer size manageable
            if len(self.buffer) > self.buffer_size:
                self.buffer = self.buffer[-self.buffer_size:]
            
            if len(self.buffer) >= 100:  # Process when we have enough data
                # Convert to numpy array
                data = np.array(self.buffer[-100:])
                
                # Apply bandpass filter (20-500 Hz for EMG)
                sos = signal.butter(4, [20, 500], btype='band', 
                                  fs=self.sampling_rate, output='sos')
                filtered_data = signal.sosfilt(sos, data)
                
                # Calculate RMS (Root Mean Square)
                rms = np.sqrt(np.mean(filtered_data**2))
                
                # Calculate mean frequency
                freqs, psd = signal.welch(filtered_data, fs=self.sampling_rate)
                mean_freq = np.sum(freqs * psd) / np.sum(psd)
                
                return {
                    'rms': rms,
                    'mean_frequency': mean_freq,
                    'filtered_data': filtered_data
                }
            
            return None

    # Usage in your main application
    processor = DataProcessor()

    def enhanced_handle_emg_data(emg_data):
        """Enhanced EMG data handler with processing"""
        result = processor.process_emg_data(emg_data)
        if result:
            print(f"RMS: {result['rms']:.4f}")
            print(f"Mean Frequency: {result['mean_frequency']:.2f} Hz")

Multiple Devices Example
========================

Working with multiple devices simultaneously:

.. code-block:: python

    from biosignal_device_interface.gui import AllDevicesWidget
    from PySide6.QtWidgets import QApplication, QMainWindow

    class MultiDeviceWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Multi-Device Interface")
            self.setGeometry(100, 100, 1200, 800)
            
            # Create the all-devices widget
            self.devices_widget = AllDevicesWidget(self)
            self.setCentralWidget(self.devices_widget)
            
            # Connect to device signals
            self.devices_widget.device_data_received.connect(self.handle_multi_device_data)
        
        def handle_multi_device_data(self, device_id, data):
            """Handle data from multiple devices"""
            print(f"📡 Device {device_id}: {data.shape}")

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MultiDeviceWindow()
        window.show()
        sys.exit(app.exec())

Configuration Tips
==================

**Network Configuration**

For TCP/IP devices like the Muovi:

.. code-block:: python

    # Common IP configurations
    DEVICE_CONFIGS = {
        'muovi_default': ("192.168.1.100", 45454),
        'muovi_custom': ("10.0.0.100", 45454),
        'localhost_test': ("127.0.0.1", 45454)
    }

    # Use the appropriate configuration
    device.toggle_connection(DEVICE_CONFIGS['muovi_default'])

**Device Settings**

.. code-block:: python

    # EMG Configuration
    emg_config = {
        "working_mode": MuoviWorkingMode.EMG,
        "detection_mode": MuoviDetectionMode.MONOPOLAR_GAIN_4,
        "sampling_rate": 2000
    }

    # EEG Configuration  
    eeg_config = {
        "working_mode": MuoviWorkingMode.EEG,
        "detection_mode": MuoviDetectionMode.MONOPOLAR_GAIN_1,
        "sampling_rate": 1000
    }

Common Patterns
===============

**Error Handling**

.. code-block:: python

    try:
        device = OTBMuovi(is_muovi_plus=False)
        success = device.toggle_connection(("192.168.1.100", 45454))
        
        if not success:
            raise ConnectionError("Failed to connect to device")
            
        device.configure_device(config)
        device.toggle_streaming()
        
    except ConnectionError as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        # Always clean up
        if 'device' in locals():
            device.toggle_streaming()  # Stop streaming
            device.toggle_connection(None)  # Disconnect

**Data Logging**

.. code-block:: python

    import csv
    from datetime import datetime

    class DataLogger:
        def __init__(self, filename=None):
            if filename is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"biosignal_data_{timestamp}.csv"
            
            self.filename = filename
            self.file = open(filename, 'w', newline='')
            self.writer = csv.writer(self.file)
            self.writer.writerow(['timestamp', 'channel', 'value'])
        
        def log_data(self, data):
            timestamp = datetime.now().isoformat()
            for channel, values in enumerate(data):
                for value in values:
                    self.writer.writerow([timestamp, channel, value])
            self.file.flush()
        
        def close(self):
            self.file.close()

    # Usage
    logger = DataLogger()
    
    def logging_data_handler(data):
        logger.log_data(data)
        # Don't forget to call logger.close() when done

Next Steps
==========

Now that you have the basics working:

1. **Explore Examples**: Check out the :doc:`../auto_examples/index` for more complex scenarios
2. **Learn About Devices**: Read the :doc:`devices` guide for device-specific information
3. **GUI Development**: Dive deeper into :doc:`gui_widgets` for advanced GUI features
4. **Data Processing**: Learn more about :doc:`data_processing` techniques
5. **API Reference**: Consult the :doc:`../api/index` for detailed documentation

Troubleshooting
===============

**Can't Connect to Device?**
    - Check IP address and port settings
    - Ensure device is powered on and in range
    - Verify network connectivity

**No Data Received?**
    - Verify device configuration
    - Check if streaming is started
    - Ensure proper signal connections

**Performance Issues?**
    - Reduce buffer sizes for real-time applications
    - Use appropriate sampling rates
    - Consider running data processing in separate threads

For more detailed troubleshooting, see the :doc:`troubleshooting` guide. 