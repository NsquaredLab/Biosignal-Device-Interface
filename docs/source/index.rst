.. Biosignal Device Interface documentation master file

==========================
Biosignal Device Interface
==========================

.. image:: https://img.shields.io/pypi/v/biosignal-device-interface.svg
   :target: https://pypi.org/project/biosignal-device-interface/
   :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/biosignal-device-interface.svg
   :target: https://pypi.org/project/biosignal-device-interface/
   :alt: Python versions

.. image:: https://github.com/NsquaredLab/Biosignal-Device-Interface/workflows/CI/badge.svg
   :target: https://github.com/NsquaredLab/Biosignal-Device-Interface/actions
   :alt: CI Status

.. image:: https://codecov.io/gh/NsquaredLab/Biosignal-Device-Interface/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/NsquaredLab/Biosignal-Device-Interface
   :alt: Coverage

.. image:: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
   :target: https://creativecommons.org/licenses/by-sa/4.0/
   :alt: License

A unified Python interface for real-time communication with biosignal acquisition devices, specifically designed for seamless integration with PySide6 applications.

.. grid:: 1 2 2 2
    :gutter: 2

    .. grid-item-card:: 🚀 Quick Start
        :link: user_guide/installation
        :link-type: doc

        Get up and running with the Biosignal Device Interface in minutes.

    .. grid-item-card:: 📖 User Guide
        :link: user_guide/index
        :link-type: doc

        Learn how to use the interface with comprehensive tutorials and examples.

    .. grid-item-card:: 🔧 API Reference
        :link: api/index
        :link-type: doc

        Detailed documentation of all classes, methods, and functions.

    .. grid-item-card:: 💡 Examples
        :link: auto_examples/index
        :link-type: doc

        Browse through practical examples and use cases.

Key Features
============

.. grid:: 1 2 2 3
    :gutter: 2

    .. grid-item-card:: ⚡ Real-time Communication
        
        Low-latency data streaming from biosignal devices with optimized performance.

    .. grid-item-card:: 🖥️ PySide6 Integration
        
        Ready-to-use GUI widgets for seamless device control and visualization.

    .. grid-item-card:: 🔌 Multiple Device Support
        
        Standardized interface for various biosignal device manufacturers.

    .. grid-item-card:: 📊 Signal Processing
        
        Built-in data conversion and processing capabilities.

    .. grid-item-card:: 🧩 Extensible Architecture
        
        Easy to add support for new devices and protocols.

    .. grid-item-card:: 📱 Cross-platform
        
        Works on Windows, macOS, and Linux systems.

Supported Devices
=================

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 50

   * - Manufacturer
     - Device
     - Channels
     - Description
   * - OT Bioelettronica
     - Muovi
     - 32
     - Wireless EMG acquisition system
   * - OT Bioelettronica
     - Muovi Plus
     - 64
     - Enhanced wireless EMG system
   * - OT Bioelettronica
     - Quattrocento
     - up to 408
     - High-density EMG system
   * - OT Bioelettronica
     - Quattrocento Light
     - up to 64
     - Compact EMG system
   * - OT Bioelettronica
     - SyncStation
     - \-
     - Synchronization device

Quick Example
=============

Here's a simple example to get you started:

.. code-block:: python

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

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Getting Started

   user_guide/installation
   user_guide/quickstart
   user_guide/configuration

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: User Guide

   user_guide/index
   user_guide/devices
   user_guide/gui_widgets
   user_guide/data_processing
   user_guide/troubleshooting

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Examples

   auto_examples/index

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: API Reference

   api/index
   api/devices
   api/gui
   api/constants

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Development

   development/contributing
   development/architecture
   development/adding_devices
   development/testing

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: About

   about/changelog
   about/license
   about/citation

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

