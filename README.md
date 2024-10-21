# Biosignal-Device-Interface

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/NsquaredLab/Biosignal-Device-Interface">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Biosignal Device Interface</h3>

  <p align="center">
    Python communication interface to many biosignal devices manufactured by several companies to easy integration in custom PySide6 applications.
    <br />
    <a href="https://nsquaredlab.github.io/Biosignal-Device-Interface/"><strong>Explore the docs »</strong></a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#contact">Contact</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#development-installation">Development Installation</a></li>
        <li><a href="#package-installation">Package Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


## About The Project

Give a brief introduction into the project.

<!-- CONTACT -->
### Contact

 [Dominik I. Braun](https://www.nsquared.tf.fau.de/person/dominik-braun/) - dome.braun@fau.de

Project Link: [https://github.com/NsquaredLab/Biosignal-Device-Interface](https://github.com/NsquaredLab/Biosignal-Device-Interface)


<!-- GETTING STARTED -->
## Getting Started

The local set up is made using [Poetry](https://python-poetry.org/). You can install Poetry using the following command.
Note: It is recommeded to install it globally.
```bash
pip install poetry
```

Then, you can install the dependencies in your work area using the following command:
```bash
poetry install
```

### Development installation
If you want to contribute to the project, you can install the development dependencies using the following command:
```bash
poetry install --with dev,docs
```

### Package Installation
Poetry
```Bash
poetry add git+https://github.com/NsquaredLab/Biosignal-Device-Interface.git
```

PIP
```sh
pip install git+https://github.com/NsquaredLab/Biosignal-Device-Interface.git
```


<!-- USAGE EXAMPLES -->
## Usage

Examples of how you can use this package can be found in our [examples gallery](https://nsquaredlab.github.io/Biosignal-Device-Interface/auto_examples/index.html).


<!-- LICENSE -->
## License

Distributed under the GPL-3.0 license License. See `LICENSE.txt` for more information.

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* Find available Python and Matlab implementations of OT Bioelettronica's devices on their [website](https://otbioelettronica.it/en/download/). 
<br>
Note: The example scripts does not provide you with the same level of utility for GUI implementations.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
