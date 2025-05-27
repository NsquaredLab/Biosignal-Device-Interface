===============
Troubleshooting
===============

This guide helps you diagnose and resolve common issues when using the Biosignal Device Interface.

Quick Diagnostic Checklist
===========================

Before diving into specific issues, run through this quick checklist:

.. admonition:: Quick Check
   :class: tip

   ✅ **Device powered on and ready**
   
   ✅ **Network connectivity established**
   
   ✅ **Correct IP address and port**
   
   ✅ **Firewall not blocking communication**
   
   ✅ **Latest package version installed**
   
   ✅ **Python environment activated**

Connection Issues
=================

Cannot Connect to Device
-------------------------

**Symptoms:**
- Connection timeout errors
- "Device not found" messages
- `toggle_connection()` returns `False`

**Solutions:**

1. **Verify Network Settings**

   .. code-block:: python

       # Test basic network connectivity
       import socket
       
       def test_network_connection(ip, port, timeout=5):
           try:
               sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               sock.settimeout(timeout)
               result = sock.connect_ex((ip, port))
               sock.close()
               return result == 0
           except Exception as e:
               print(f"Network test failed: {e}")
               return False
       
       # Test your device connection
       if test_network_connection("192.168.1.100", 45454):
           print("✅ Network connection OK")
       else:
           print("❌ Cannot reach device")

2. **Check Device IP Address**

   .. code-block:: bash

       # Windows: Find device IP
       arp -a
       
       # Linux/macOS: Find device IP
       arp -a | grep -i "device_mac_address"
       
       # Ping the device
       ping 192.168.1.100

3. **Verify Firewall Settings**

   .. code-block:: bash

       # Windows: Allow Python through firewall
       netsh advfirewall firewall add rule name="Python" dir=in action=allow program="python.exe"
       
       # Linux: Allow port through firewall
       sudo ufw allow 45454

4. **Check Device Status**

   .. code-block:: python

       from biosignal_device_interface.devices import OTBMuovi
       
       device = OTBMuovi()
       
       # Enable debug logging
       import logging
       logging.basicConfig(level=logging.DEBUG)
       
       # Attempt connection with detailed logging
       success = device.toggle_connection(("192.168.1.100", 45454))
       if not success:
           print("Connection failed - check logs for details")

Intermittent Disconnections
----------------------------

**Symptoms:**
- Device connects but disconnects randomly
- Data streaming stops unexpectedly
- Connection status changes frequently

**Solutions:**

1. **Check Wi-Fi Signal Strength** (for wireless devices)

   .. code-block:: python

       # Monitor connection stability
       import time
       
       def monitor_connection(device, duration=60):
           start_time = time.time()
           disconnections = 0
           
           while time.time() - start_time < duration:
               if not device.is_connected():
                   disconnections += 1
                   print(f"Disconnection detected at {time.time()}")
               time.sleep(1)
           
           print(f"Disconnections in {duration}s: {disconnections}")

2. **Optimize Network Settings**

   .. code-block:: python

       # Increase connection timeout
       device.set_connection_timeout(10)  # 10 seconds
       
       # Enable automatic reconnection
       device.enable_auto_reconnect(True)

3. **Check Power Supply**
   - Ensure stable power supply for wired devices
   - Monitor battery level for wireless devices
   - Use high-quality USB cables

Data Issues
===========

No Data Received
-----------------

**Symptoms:**
- Device connects but no data arrives
- Data signals never trigger
- Empty data arrays

**Solutions:**

1. **Verify Streaming is Started**

   .. code-block:: python

       # Check streaming status
       if device.is_connected():
           if not device.is_streaming():
               print("Starting data streaming...")
               device.toggle_streaming()
           else:
               print("Streaming already active")

2. **Check Signal Connections**

   .. code-block:: python

       # Monitor data reception
       data_received = False
       
       def data_handler(data):
           global data_received
           data_received = True
           print(f"Data received: {data.shape}")
       
       device.data_available.connect(data_handler)
       
       # Wait for data
       import time
       time.sleep(5)
       
       if not data_received:
           print("❌ No data received - check configuration")

3. **Verify Device Configuration**

   .. code-block:: python

       # Check current configuration
       config = device.get_device_information()
       print(f"Current config: {config}")
       
       # Reconfigure if needed
       new_config = {
           "working_mode": MuoviWorkingMode.EMG,
           "detection_mode": MuoviDetectionMode.MONOPOLAR_GAIN_4,
           "sampling_rate": 2000
       }
       device.configure_device(new_config)

Corrupted or Invalid Data
-------------------------

**Symptoms:**
- Data contains unexpected values
- Inconsistent data shapes
- NaN or infinite values

**Solutions:**

1. **Validate Data Quality**

   .. code-block:: python

       import numpy as np
       
       def validate_data(data):
           issues = []
           
           # Check for NaN values
           if np.isnan(data).any():
               issues.append("Contains NaN values")
           
           # Check for infinite values
           if np.isinf(data).any():
               issues.append("Contains infinite values")
           
           # Check data range
           if np.abs(data).max() > 10:  # Assuming mV range
               issues.append("Values outside expected range")
           
           # Check for constant values
           if np.std(data) < 1e-6:
               issues.append("Data appears constant (no variation)")
           
           return issues
       
       def data_quality_handler(data):
           issues = validate_data(data)
           if issues:
               print(f"Data quality issues: {issues}")
           else:
               print("✅ Data quality OK")

2. **Check Sampling Rate Consistency**

   .. code-block:: python

       import time
       
       class SamplingRateMonitor:
           def __init__(self):
               self.last_time = None
               self.sample_count = 0
               self.intervals = []
           
           def process_data(self, data):
               current_time = time.time()
               if self.last_time is not None:
                   interval = current_time - self.last_time
                   self.intervals.append(interval)
                   
                   if len(self.intervals) > 100:
                       avg_interval = np.mean(self.intervals[-100:])
                       expected_rate = 1.0 / avg_interval
                       print(f"Actual sampling rate: {expected_rate:.1f} Hz")
               
               self.last_time = current_time
               self.sample_count += len(data)

Performance Issues
==================

High CPU Usage
--------------

**Symptoms:**
- Application becomes slow or unresponsive
- High CPU usage in task manager
- Delayed data processing

**Solutions:**

1. **Optimize Data Processing**

   .. code-block:: python

       # Use efficient data processing
       import numpy as np
       from collections import deque
       
       class EfficientDataProcessor:
           def __init__(self, buffer_size=1000):
               self.buffer = deque(maxlen=buffer_size)
           
           def process_data(self, data):
               # Add data to buffer efficiently
               self.buffer.extend(data.flatten())
               
               # Process only when buffer is full
               if len(self.buffer) == self.buffer.maxlen:
                   # Convert to numpy array once
                   array_data = np.array(self.buffer)
                   
                   # Perform batch processing
                   result = self.batch_process(array_data)
                   return result
           
           def batch_process(self, data):
               # Efficient batch processing
               return np.mean(data), np.std(data)

2. **Reduce Sampling Rate**

   .. code-block:: python

       # Lower sampling rate for less critical applications
       config = {
           "sampling_rate": 1000,  # Instead of 2000
           "channels": [0, 1, 2, 3]  # Fewer channels
       }
       device.configure_device(config)

3. **Use Threading for Data Processing**

   .. code-block:: python

       import threading
       import queue
       
       class ThreadedDataProcessor:
           def __init__(self):
               self.data_queue = queue.Queue()
               self.processing_thread = threading.Thread(target=self._process_loop)
               self.processing_thread.daemon = True
               self.processing_thread.start()
           
           def add_data(self, data):
               self.data_queue.put(data)
           
           def _process_loop(self):
               while True:
                   try:
                   data = self.data_queue.get(timeout=1)
                       result = self.process_data(data)
                       self.result_ready.emit(result)
                   except queue.Empty:
                       continue

Memory Issues
-------------

**Symptoms:**
- Increasing memory usage over time
- Out of memory errors
- Application crashes

**Solutions:**

1. **Implement Proper Buffer Management**

   .. code-block:: python

       class MemoryEfficientBuffer:
           def __init__(self, max_size=10000):
               self.max_size = max_size
               self.data = []
           
           def add_data(self, new_data):
               self.data.extend(new_data)
               
               # Keep buffer size under control
               if len(self.data) > self.max_size:
                   # Remove oldest data
                   excess = len(self.data) - self.max_size
                   self.data = self.data[excess:]
           
           def get_recent_data(self, n_samples):
               return self.data[-n_samples:] if len(self.data) >= n_samples else self.data

2. **Monitor Memory Usage**

   .. code-block:: python

       import psutil
       import os
       
       def monitor_memory():
           process = psutil.Process(os.getpid())
           memory_info = process.memory_info()
           memory_mb = memory_info.rss / 1024 / 1024
           print(f"Memory usage: {memory_mb:.1f} MB")
           return memory_mb
       
       # Monitor periodically
       import threading
       import time
       
       def memory_monitor():
           while True:
               memory_mb = monitor_memory()
               if memory_mb > 500:  # Alert if over 500 MB
                   print("⚠️ High memory usage detected!")
               time.sleep(10)
       
       monitor_thread = threading.Thread(target=memory_monitor)
       monitor_thread.daemon = True
       monitor_thread.start()

GUI Issues
==========

Widget Not Responding
---------------------

**Symptoms:**
- GUI freezes or becomes unresponsive
- Buttons don't respond to clicks
- Interface updates slowly

**Solutions:**

1. **Ensure GUI Updates on Main Thread**

   .. code-block:: python

       from PySide6.QtCore import QTimer, Signal
       from PySide6.QtWidgets import QApplication
       
       class ResponsiveWidget(QWidget):
           data_received = Signal(object)
           
           def __init__(self):
               super().__init__()
               self.data_received.connect(self.update_display)
               
               # Use timer for periodic updates
               self.update_timer = QTimer()
               self.update_timer.timeout.connect(self.periodic_update)
               self.update_timer.start(100)  # Update every 100ms
           
           def handle_device_data(self, data):
               # Emit signal instead of direct update
               self.data_received.emit(data)
           
           def update_display(self, data):
               # This runs on the main thread
               # Update GUI elements here
               pass
           
           def periodic_update(self):
               # Process events to keep GUI responsive
               QApplication.processEvents()

2. **Use Background Threads for Heavy Processing**

   .. code-block:: python

       from PySide6.QtCore import QThread, Signal
       
       class DataProcessingThread(QThread):
           result_ready = Signal(object)
           
           def __init__(self):
               super().__init__()
               self.data_queue = queue.Queue()
           
           def add_data(self, data):
               self.data_queue.put(data)
           
           def run(self):
               while True:
                   try:
                   data = self.data_queue.get(timeout=1)
                       result = self.process_data(data)
                       self.result_ready.emit(result)
                   except queue.Empty:
                       continue

Installation Issues
===================

Package Import Errors
----------------------

**Symptoms:**
- `ModuleNotFoundError` when importing
- `ImportError` for specific components
- Version compatibility issues

**Solutions:**

1. **Verify Installation**

   .. code-block:: bash

       # Check if package is installed
       pip list | grep biosignal-device-interface
       
       # Reinstall if needed
       pip uninstall biosignal-device-interface
       pip install git+https://github.com/NsquaredLab/Biosignal-Device-Interface.git

2. **Check Python Environment**

   .. code-block:: python

       import sys
       print(f"Python version: {sys.version}")
       print(f"Python path: {sys.path}")
       
       # Check specific imports
       try:
           import biosignal_device_interface
           print(f"Package version: {biosignal_device_interface.__version__}")
       except ImportError as e:
           print(f"Import error: {e}")

3. **Resolve Dependency Conflicts**

   .. code-block:: bash

       # Create clean environment
       python -m venv biosignal_env
       
       # Windows
       biosignal_env\Scripts\activate
       
       # Linux/macOS
       source biosignal_env/bin/activate
       
       # Install package
       pip install git+https://github.com/NsquaredLab/Biosignal-Device-Interface.git

PySide6 Issues
--------------

**Symptoms:**
- GUI components don't display correctly
- Qt-related errors
- Missing GUI dependencies

**Solutions:**

1. **Reinstall PySide6**

   .. code-block:: bash

       pip uninstall PySide6
       pip install PySide6

2. **Check Qt Installation**

   .. code-block:: python

       try:
           from PySide6.QtWidgets import QApplication
           from PySide6.QtCore import QTimer
           print("✅ PySide6 import successful")
       except ImportError as e:
           print(f"❌ PySide6 import failed: {e}")

Advanced Debugging
==================

Enable Debug Logging
---------------------

.. code-block:: python

    import logging
    
    # Configure detailed logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('biosignal_debug.log'),
            logging.StreamHandler()
        ]
    )
    
    # Enable package-specific logging
    logger = logging.getLogger('biosignal_device_interface')
    logger.setLevel(logging.DEBUG)

Network Debugging
-----------------

.. code-block:: python

    import socket
    import time
    
    def detailed_network_test(ip, port):
        print(f"Testing connection to {ip}:{port}")
        
        try:
            # Test DNS resolution
            resolved_ip = socket.gethostbyname(ip)
            print(f"✅ DNS resolution: {ip} -> {resolved_ip}")
        except socket.gaierror as e:
            print(f"❌ DNS resolution failed: {e}")
            return False
        
        try:
            # Test TCP connection
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            start_time = time.time()
            result = sock.connect_ex((ip, port))
            connection_time = time.time() - start_time
            sock.close()
            
            if result == 0:
                print(f"✅ TCP connection successful ({connection_time:.3f}s)")
                return True
            else:
                print(f"❌ TCP connection failed (error {result})")
                return False
        except Exception as e:
            print(f"❌ Connection test failed: {e}")
            return False

Performance Profiling
----------------------

.. code-block:: python

    import cProfile
    import pstats
    
    def profile_data_processing():
        profiler = cProfile.Profile()
        profiler.enable()
        
        # Your data processing code here
        # ... 
        
        profiler.disable()
        
        # Analyze results
        stats = pstats.Stats(profiler)
        stats.sort_stats('cumulative')
        stats.print_stats(10)  # Top 10 functions

Getting Help
============

If you continue to experience issues:

1. **Check GitHub Issues**: `GitHub Issues <https://github.com/NsquaredLab/Biosignal-Device-Interface/issues>`_

2. **Create a Bug Report** with:
   - Operating system and version
   - Python version
   - Package version
   - Complete error message
   - Minimal code to reproduce the issue
   - Debug logs

3. **Community Support**:
   - Check existing documentation
   - Search for similar issues
   - Provide detailed information when asking for help

**Bug Report Template:**

.. code-block:: text

    **Environment:**
    - OS: Windows 10 / macOS 12 / Ubuntu 20.04
    - Python: 3.9.7
    - Package: 1.0.0
    
    **Issue Description:**
    Brief description of the problem
    
    **Steps to Reproduce:**
    1. Step one
    2. Step two
    3. Step three
    
    **Expected Behavior:**
    What should happen
    
    **Actual Behavior:**
    What actually happens
    
    **Error Message:**
    ```
    Complete error traceback
    ```
    
    **Additional Context:**
    Any other relevant information 