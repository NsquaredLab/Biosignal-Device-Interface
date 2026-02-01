# Biosignal-Device-Interface

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/NsquaredLab/Biosignal-Device-Interface">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Biosignal Device Interface</h3>

  <p align="center">
    Python communication interface to many biosignal devices manufactured by several companies for easy integration in custom PySide6 applications.
    <br />
    <a href="https://nsquaredlab.github.io/Biosignal-Device-Interface/"><strong>Explore the docs »</strong></a>
  </p>

[![PyPI version](https://img.shields.io/pypi/v/biosignal-device-interface.svg)](https://pypi.org/project/biosignal-device-interface/)
[![Python versions](https://img.shields.io/pypi/pyversions/biosignal-device-interface.svg)](https://pypi.org/project/biosignal-device-interface/)
[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)](LICENSE)

</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#supported-devices">Supported Devices</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#development-installation">Development Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


## About The Project

Biosignal Device Interface provides a unified Python API for communicating with biosignal acquisition devices from multiple manufacturers. It includes ready-to-use PySide6 widgets for device configuration and data streaming, making it easy to integrate biosignal acquisition into custom applications.

## Supported Devices

### OT Bioelettronica
- **Quattrocento** - 400+ channel EMG/EEG amplifier
- **Quattrocento Light** - Compact version of Quattrocento
- **Muovi** - Wearable EMG sensor
- **Muovi+** - Enhanced wearable EMG sensor
- **SyncStation** - Multi-device synchronization hub (Muovi, Muovi+, Due+)

### Other Devices
- More devices coming soon...

<!-- GETTING STARTED -->
## Getting Started

### Installation

Install from PyPI:
```bash
pip install biosignal-device-interface
```

Or with Poetry:
```bash
poetry add biosignal-device-interface
```

### Development Installation

Clone the repository and install with development dependencies:

```bash
git clone https://github.com/NsquaredLab/Biosignal-Device-Interface.git
cd Biosignal-Device-Interface
poetry install --with dev,docs
```

<!-- USAGE EXAMPLES -->
## Usage

Examples of how you can use this package can be found in our [examples gallery](https://nsquaredlab.github.io/Biosignal-Device-Interface/auto_examples/index.html).

<!-- LICENSE -->
## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

- [Dominik I. Braun](https://www.nsquared.tf.fau.de/person/dominik-braun/) - dome.braun@fau.de
- [Raul C. Sîmpetru](https://www.nsquared.tf.fau.de/person/raul-simpetru/) - raul.simpetru@fau.de

Project Link: [https://github.com/NsquaredLab/Biosignal-Device-Interface](https://github.com/NsquaredLab/Biosignal-Device-Interface)

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* Find available Python and Matlab implementations of OT Bioelettronica's devices on their [website](https://otbioelettronica.it/en/download/).
<br>
Note: The example scripts do not provide you with the same level of utility for GUI implementations.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
