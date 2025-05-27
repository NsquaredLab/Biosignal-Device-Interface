"""
Integrating all devices and a biosignal plot in your own software.
==================================================================

This example demonstrates how to integrate all available biosignal device widgets 
along with a real-time biosignal plot into your own PySide6 application. The example 
shows how to create a main window with a horizontal layout containing both the device 
interface and a plot widget that displays incoming biosignal data in real-time.

Note: This example creates a GUI application. When run directly, it will open a window.
During documentation generation, it only demonstrates the setup without showing the GUI.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout

from biosignal_device_interface.devices import AllDevicesWidget

from biosignal_device_interface.gui.plot_widgets.biosignal_plot_widget import (
    BiosignalPlotWidget,
)

if TYPE_CHECKING:
    import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the title of the main window
        self.setWindowTitle("Main Window with All Devices and Biosignal Plot")

        # Instantiate the central widget
        self.central_widget = QWidget(self)

        # Set the central widget of the main window
        self.setCentralWidget(self.central_widget)

        # Create a horizontal layout
        self.horizontal_box_layout = QHBoxLayout(self.central_widget)

        # Instantiate the AllDevicesWidget
        self.all_devices_widget = AllDevicesWidget(self)

        # Connect the signals of the widget to the main window
        self.all_devices_widget.biosignal_data_arrived.connect(self._emg_update)
        self.all_devices_widget.configure_toggled.connect(
            self._device_configuration_state
        )

        # Instantiate Biosignal Plot
        self.biosignal_plot = BiosignalPlotWidget(self)

        self.horizontal_box_layout.addWidget(self.all_devices_widget)
        self.horizontal_box_layout.addWidget(self.biosignal_plot)

    def _emg_update(self, data: np.ndarray):
        if self.biosignal_plot.is_configured:
            self.biosignal_plot.update_plot(data)

    def _device_configuration_state(self, is_configured: bool):
        if not is_configured:
            return

        device_information = self.all_devices_widget.get_device_information()

        biosignal_channels = device_information["number_of_biosignal_channels"]
        sampling_frequency = device_information["sampling_frequency"]

        self.biosignal_plot.configure(
            lines=biosignal_channels,
            sampling_frequency=sampling_frequency,
            line_height=100,
            display_time=10,
        )


# %%
# Creating the Application and Main Window
# =========================================
#
# Here we demonstrate how to set up the application and create the main window
# with both device interface and biosignal plot widgets.

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
    print("Device interface and biosignal plot widgets integrated.")
    print("Real-time plotting configured and ready.")
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
#    python examples/3_integrating_device_interface_and_biosignal_plot.py
#
# This will open a window with:
#
# * **Left panel**: Device interfaces for all available biosignal devices
# * **Right panel**: Real-time biosignal plot that automatically updates
#
# You can:
#
# * Connect to multiple biosignal devices
# * Configure device settings and plot parameters
# * Start data streaming to see real-time biosignal visualization
# * Monitor multiple channels simultaneously with automatic scaling

if __name__ == "__main__" and not is_headless:
    # Show the main window and start the event loop
    window.show()
    print("Starting application event loop...")
    sys.exit(app.exec())
elif __name__ == "__main__":
    print("Headless mode detected - example completed without showing GUI")
