"""
Integrating all devices and a biosignal plot in your own software.
================================
"""

# ..code-block:: Python
from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout
import sys

from biosignal_device_interface.gui.device_template_widgets.all_devices_widget import (
    AllDevicesWidget,
)
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
            self.biosignal_plot.update_plot(data * 1000)

    def _device_configuration_state(self, is_configured: bool):
        if not is_configured:
            return

        device_information = self.all_devices_widget.get_device_information()

        biosignal_channels = device_information["number_of_biosignal_channels"]
        sampling_frequency = device_information["sampling_frequency"]

        self.biosignal_plot.configure(
            lines=biosignal_channels,
            sampling_freuqency=sampling_frequency,
            display_time=10,
        )


if __name__ == "__main__":
    # Create the application object
    app = QApplication(sys.argv)

    # Create an instance of the main window
    window = MainWindow()

    # Show the main window
    window.show()

    # Execute the application
    sys.exit(app.exec())
