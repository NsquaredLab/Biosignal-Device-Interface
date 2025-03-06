"""
Device class for real-time interfacing the Mindrove device.
Developer: Amin Olamazadeh
Contact: amin.olamazadeh@fau.de
Last Update: 2025-02-28
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Union, Dict
import numpy as np
from PySide6.QtCore import QTimer

from biosignal_device_interface.devices.core.base_device import BaseDevice
from mindrove.board_shim import BoardShim, MindRoveInputParams, BoardIds
from mindrove.data_filter import DataFilter, DetrendOperations

if TYPE_CHECKING:
    from PySide6.QtWidgets import QMainWindow, QWidget
    from aenum import Enum

from biosignal_device_interface.constants.devices.core.base_device_constants import DeviceType

class Mindrove(BaseDevice):
    def __init__(self, parent: Union[QMainWindow, QWidget] = None) -> None:
        # Ensure BaseDevice is initialized first
        super().__init__(parent)

        # Set device type
        self._device_type = DeviceType.Mindrove

        # Initialize board
        self.board_id = BoardIds.MINDROVE_WIFI_BOARD
        self.params = MindRoveInputParams()
        self.board_shim = BoardShim(self.board_id, self.params)

      
        self._sampling_frequency = BoardShim.get_sampling_rate(self.board_id)

    
        self.emg_channels = BoardShim.get_exg_channels(self.board_id)

        # Set number of biosignal channels
        self._number_of_biosignal_channels = len(self.emg_channels)
        self._biosignal_channel_indices = self.emg_channels

      
        self._number_of_auxiliary_channels = 0  

    
        self._samples_per_frame = self._determine_samples_per_frame()

 
        self._number_of_channels = self._number_of_biosignal_channels + self._number_of_auxiliary_channels

   
        self._conversion_factor_biosignal = 6e-6 # Scale raw data to mV
        self._conversion_factor_auxiliary = 1


        self.num_points = self._samples_per_frame

    
        #self.timer_interval_ms = int((self.num_points / self._sampling_frequency) * 1000)
        self.timer_interval_ms = 20


        # Timer for polling data
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._read_data)

        self._is_streaming = False

    def _determine_samples_per_frame(self) -> int:
        """
        Determines the optimal number of samples per frame dynamically based on the sampling frequency.
        Ensures at least 10 updates per second.
        """
        if self._sampling_frequency is None or self._sampling_frequency <= 0:
            raise ValueError("Invalid sampling frequency detected.")

        return max(1, self._sampling_frequency // 10)

    def _connect_to_device(self) -> bool:
        """ Prepares the session for the Mindrove board. """
        try:
            self.board_shim.prepare_session()
            self.is_connected = True
            self.connect_toggled.emit(self.is_connected)
            print("Mindrove connected")

            self._is_configured = True
            self.configure_toggled.emit(True)
            return True
        except Exception as e:
            self.is_connected = False
            print("Connection failed:", e)
            return False

    def _disconnect_from_device(self) -> bool:
        """ Releases the Mindrove session. """
        try:
            self.board_shim.release_session()
            self.is_connected = False
            self.connect_toggled.emit(self.is_connected)
            return True
        except Exception as e:
            print("Disconnection failed:", e)
            return False

    def configure_device(self, params: Dict[str, Union[Enum, Dict[str, Enum]]]) -> None:
        """ No extra configuration needed for raw EMG streaming. """
        super().configure_device(params)
        self.configure_toggled.emit(True)

    def _start_streaming(self) -> None:
        """ Starts the Mindrove data stream and polling timer. """
        if not self.is_connected:
            if not self._connect_to_device():
                return
        try:
            self.board_shim.start_stream()
            self._is_streaming = True
            self._timer.start(self.timer_interval_ms)
            super()._start_streaming()
            print("Streaming started")
        except Exception as e:
            print("Error starting stream:", e)

    def _stop_streaming(self) -> None:
        """ Stops the data stream and polling timer. """
        if self._is_streaming:
            try:
                self._timer.stop()
                self.board_shim.stop_stream()
                self._is_streaming = False
                super()._stop_streaming()
                print("Streaming stopped")
            except Exception as e:
                print("Error stopping stream:", e)

    def toggle_streaming(self) -> None:
        """ Toggles streaming on and off. """
        if self._is_streaming:
            self._stop_streaming()
        else:
            self._start_streaming()

    def _read_data(self) -> None:
        """ Reads data from the Mindrove board and processes it. """
        if not self._is_streaming:
            return

        try:
            # Read data from the board using dynamically determined num_points
            data = self.board_shim.get_current_board_data(self.num_points)

            # Extract only the EMG channels (EXG channels)
            raw_emg = data[self.emg_channels, :]

            # Process data (detrending and scaling)
            processed_data = self._process_data(raw_emg)

            # Emit processed data
            self.data_available.emit(processed_data)
            self.biosignal_data_available.emit(processed_data)

        except Exception as e:
            print("Error reading or processing data:", e)

    def _process_data(self, data: np.ndarray) -> np.ndarray:
        """ Processes raw EMG data by applying detrending and scaling. """
        # Apply Detrending (Remove DC Offset)
        for ch in range(data.shape[0]):
            if data[ch].size > 0:
                DataFilter.detrend(data[ch], DetrendOperations.CONSTANT.value)

        # Apply Scaling Factor (Convert to mV)
        return data * self._conversion_factor_biosignal
