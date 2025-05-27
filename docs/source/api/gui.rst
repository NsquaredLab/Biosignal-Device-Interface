===
GUI
===

This section documents the GUI components and widgets for biosignal device interfaces.

Base Widget Classes
===================

BaseDeviceWidget
----------------

The abstract base class for all device-specific GUI widgets.

.. autoclass:: biosignal_device_interface.gui.BaseDeviceWidget
   :members:
   :undoc-members:
   :show-inheritance:

   .. rubric:: Key Methods

   .. autosummary::
      :nosignatures:

      ~BaseDeviceWidget.get_device_information
      ~BaseDeviceWidget.disconnect_device

   .. rubric:: Signals

   .. autosummary::
      :nosignatures:

      ~BaseDeviceWidget.data_arrived
      ~BaseDeviceWidget.biosignal_data_arrived
      ~BaseDeviceWidget.auxiliary_data_arrived
      ~BaseDeviceWidget.connect_toggled
      ~BaseDeviceWidget.configure_toggled
      ~BaseDeviceWidget.stream_toggled

BaseMultipleDevicesWidget
-------------------------

Base class for widgets that manage multiple devices simultaneously.

.. autoclass:: biosignal_device_interface.gui.BaseMultipleDevicesWidget
   :members:
   :undoc-members:
   :show-inheritance:

Device-Specific Widgets
=======================

AllDevicesWidget
----------------

Widget that provides a unified interface for all supported devices.

.. autoclass:: biosignal_device_interface.gui.AllDevicesWidget
   :members:
   :undoc-members:
   :show-inheritance:

OT Bioelettronica Widgets
=========================

OTBMuoviWidget
--------------

GUI widget for controlling OT Bioelettronica Muovi devices.

.. autoclass:: biosignal_device_interface.gui.OTBMuoviWidget
   :members:
   :undoc-members:
   :show-inheritance:

   **Usage Example:**

   .. code-block:: python

       from biosignal_device_interface.gui import OTBMuoviWidget
       from PySide6.QtWidgets import QApplication, QMainWindow

       app = QApplication([])
       window = QMainWindow()
       
       # Create widget for Muovi device
       muovi_widget = OTBMuoviWidget(window)
       window.setCentralWidget(muovi_widget)
       
       # Connect to data signals
       muovi_widget.biosignal_data_arrived.connect(handle_data)
       muovi_widget.connect_toggled.connect(handle_connection)
       
       window.show()
       app.exec()

OTBMuoviPlusWidget
------------------

GUI widget for controlling OT Bioelettronica Muovi Plus devices.

.. autoclass:: biosignal_device_interface.gui.OTBMuoviPlusWidget
   :members:
   :undoc-members:
   :show-inheritance:

OTBQuattrocentoLightWidget
--------------------------

GUI widget for controlling OT Bioelettronica Quattrocento Light devices.

.. autoclass:: biosignal_device_interface.gui.OTBQuattrocentoLightWidget
   :members:
   :undoc-members:
   :show-inheritance:

OTBSyncStationWidget
--------------------

GUI widget for controlling OT Bioelettronica SyncStation devices.

.. autoclass:: biosignal_device_interface.gui.OTBSyncStationWidget
   :members:
   :undoc-members:
   :show-inheritance:

OTBDevicesWidget
----------------

Unified widget for all OT Bioelettronica devices.

.. autoclass:: biosignal_device_interface.gui.OTBDevicesWidget
   :members:
   :undoc-members:
   :show-inheritance: 