"""
Integrating a device in your own software.
==========================================

This example demonstrates how to integrate a biosignal device widget into your own
PySide6 application. The example shows how to create a main window, instantiate a
device widget, connect its signals, and handle the incoming data.

Note: This example creates a GUI application. When run directly, it will open a window.
During documentation generation, it only demonstrates the setup without showing the GUI.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from biosignal_device_interface.devices import (
    OTBQuattrocentoLightWidget,
)

if TYPE_CHECKING:
    import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the title of the main window
        self.setWindowTitle("Main Window with One Device")

        # Instantiate the QuattrocentoLightWidget
        muovi_widget = OTBQuattrocentoLightWidget(self)

        # Connect the signals of the widget to the main window
        muovi_widget.data_arrived.connect(self._update)
        muovi_widget.biosignal_data_arrived.connect(self._emg_update)
        muovi_widget.auxiliary_data_arrived.connect(self._aux_update)
        muovi_widget.connect_toggled.connect(self._device_connection_state)
        muovi_widget.configure_toggled.connect(self._device_configuration_state)
        muovi_widget.stream_toggled.connect(self._device_stream_state)

        # Set the central widget of the main window
        self.setCentralWidget(muovi_widget)

    def _update(self, data: np.ndarray):
        print("Incoming data from device:", data.shape)

    def _emg_update(self, data: np.ndarray):
        print("Incoming emg data from device:", data.shape)

    def _aux_update(self, data: np.ndarray):
        print("Incoming auxiliary data from device:", data.shape)

    def _device_connection_state(self, is_connected: bool):
        print("Connection state:", is_connected)

    def _device_configuration_state(self, is_configured: bool):
        print("Configuration state:", is_configured)

    def _device_stream_state(self, is_streaming: bool):
        print("Streaming state:", is_streaming)


# %%
# Creating the Application and Main Window
# =========================================
#
# Here we demonstrate how to set up the application and create the main window.
# In a real application, you would call app.exec() to start the event loop.

# Check if we're in a headless environment (like during documentation generation)
# or if DISPLAY is not available
is_headless = (
    os.environ.get('DISPLAY', '') == '' or 
    'sphinx' in sys.modules or
    'PYTEST_CURRENT_TEST' in os.environ
)

if not is_headless:
    # Only create QApplication if we're not in a headless environment
    app = QApplication(sys.argv)
else:
    # For documentation/testing, we can still demonstrate the setup
    app = None

# Create an instance of the main window
# This demonstrates the complete setup process
print("Creating MainWindow instance...")
if app is not None:
    window = MainWindow()
    print("MainWindow created successfully!")
    print("Device widget integrated and signals connected.")
else:
    print("Running in headless mode - skipping GUI creation")
    print("In a real application, you would:")
    print("1. Create QApplication(sys.argv)")
    print("2. Create MainWindow() instance")
    print("3. Call window.show()")
    print("4. Call sys.exit(app.exec())")

# %%
# Running the Application
# =======================
#
# To actually run this application with a visible GUI, execute this script directly:
#
# .. code-block:: bash
#
#    python examples/1_integrating_a_device.py
#
# This will open a window with the device interface where you can:
#
# * Connect to a Quattrocento Light device
# * Configure the device settings
# * Start/stop data streaming
# * Monitor incoming biosignal and auxiliary data

if __name__ == "__main__" and not is_headless:
    # Show the main window and start the event loop
    window.show()
    print("Starting application event loop...")
    sys.exit(app.exec())
elif __name__ == "__main__":
    print("Headless mode detected - example completed without showing GUI")
