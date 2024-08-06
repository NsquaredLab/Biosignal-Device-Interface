"""
Integrating a device in your own software.
==========================================

This example...
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6.QtWidgets import QApplication, QMainWindow
import sys

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
        print("Incoming data frome device:", data.shape)

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


if __name__ == "__main__":
    # Create the application object
    app = QApplication(sys.argv)

    # Create an instance of the main window
    window = MainWindow()

    # Show the main window
    window.show()

    # Execute the application
    sys.exit(app.exec())
