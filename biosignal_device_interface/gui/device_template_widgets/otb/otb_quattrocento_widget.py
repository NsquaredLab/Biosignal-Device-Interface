"""
Quattrocento Widget class for GUI configuration
of the Quattrocento from OT Bioelettronica.

Developer: Dominik I. Braun
Contact: dome.braun@fau.de
Last Update: 2025-01-14
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from biosignal_device_interface.gui.device_template_widgets.core.base_device_widget import (
    BaseDeviceWidget,
)
from biosignal_device_interface.gui.ui_compiled.otb_quattrocento_template_widget import (
    Ui_QuattrocentoForm,
)
from biosignal_device_interface.devices.otb.otb_quattrocento import (
    OTBQuattrocento,
)

# Constants
from biosignal_device_interface.constants.devices.otb.otb_quattrocento_constants import (
    QuattrocentoSamplingFrequencyMode,
    QuattrocentoNumberOfChannelsMode,
    QuattrocentoLowPassFilterMode,
    QuattrocentoHighPassFilterMode,
    QuattrocentoDetectionMode,
)
