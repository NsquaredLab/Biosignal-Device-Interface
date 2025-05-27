============
Installation
============

This guide will help you install the Biosignal Device Interface package and set up your development environment.

System Requirements
===================

**Operating Systems**
    - Windows 10/11 (64-bit)
    - macOS 10.15+ (Intel and Apple Silicon)
    - Linux (Ubuntu 18.04+, CentOS 7+, or equivalent)

**Python Version**
    - Python 3.8 or higher
    - Python 3.9+ recommended for best performance

**Hardware Requirements**
    - Minimum 4GB RAM (8GB+ recommended)
    - Network interface for TCP/IP device communication
    - USB ports for serial device communication

Installation Methods
====================

Method 1: Using Poetry (Recommended)
-------------------------------------

Poetry is the recommended way to install the package as it handles dependency management automatically.

.. code-block:: bash

    # Clone the repository
    git clone https://github.com/NsquaredLab/Biosignal-Device-Interface.git
    cd Biosignal-Device-Interface

    # Install dependencies
    poetry install

    # For development with additional tools
    poetry install --with dev,docs

**Activating the Environment**

.. code-block:: bash

    # Activate the poetry environment
    poetry shell

    # Or run commands directly
    poetry run python your_script.py

Method 2: Using pip
-------------------

You can install directly from the GitHub repository:

.. code-block:: bash

    # Install from GitHub
    pip install git+https://github.com/NsquaredLab/Biosignal-Device-Interface.git

    # Or install in development mode
    git clone https://github.com/NsquaredLab/Biosignal-Device-Interface.git
    cd Biosignal-Device-Interface
    pip install -e .

Method 3: Using conda
---------------------

If you prefer conda for package management:

.. code-block:: bash

    # Create a new environment
    conda create -n biosignal python=3.9
    conda activate biosignal

    # Install dependencies
    conda install numpy scipy matplotlib pyside6
    pip install git+https://github.com/NsquaredLab/Biosignal-Device-Interface.git

Verifying Installation
======================

To verify that the installation was successful, run the following test:

.. code-block:: python

    import biosignal_device_interface
    print(f"Biosignal Device Interface version: {biosignal_device_interface.__version__}")

    # Test importing main components
    from biosignal_device_interface.devices import BaseDevice
    from biosignal_device_interface.gui import BaseDeviceWidget
    print("✅ Installation successful!")

Development Installation
========================

If you plan to contribute to the project or modify the source code:

.. code-block:: bash

    # Clone the repository
    git clone https://github.com/NsquaredLab/Biosignal-Device-Interface.git
    cd Biosignal-Device-Interface

    # Install in development mode with all dependencies
    poetry install --with dev,docs

    # Install pre-commit hooks
    poetry run pre-commit install

**Development Dependencies Include:**
    - pytest (testing framework)
    - black (code formatting)
    - flake8 (linting)
    - mypy (type checking)
    - sphinx (documentation)
    - pre-commit (git hooks)

Optional Dependencies
=====================

Some features require additional packages:

**For Advanced Signal Processing:**

.. code-block:: bash

    pip install scipy scikit-learn

**For Data Visualization:**

.. code-block:: bash

    pip install matplotlib seaborn plotly

**For Data Export:**

.. code-block:: bash

    pip install pandas h5py

Troubleshooting Installation
============================

Common Issues and Solutions
---------------------------

**PySide6 Installation Issues**

If you encounter issues installing PySide6:

.. code-block:: bash

    # On Ubuntu/Debian
    sudo apt-get install qt6-base-dev

    # On macOS with Homebrew
    brew install qt6

    # Then reinstall PySide6
    pip install --upgrade PySide6

**Permission Errors**

If you get permission errors during installation:

.. code-block:: bash

    # Use user installation
    pip install --user git+https://github.com/NsquaredLab/Biosignal-Device-Interface.git

**Network/Firewall Issues**

If you're behind a corporate firewall:

.. code-block:: bash

    # Configure pip to use your proxy
    pip install --proxy http://user:password@proxy.server:port package_name

**Virtual Environment Issues**

If you have conflicts with existing packages:

.. code-block:: bash

    # Create a clean virtual environment
    python -m venv biosignal_env
    
    # On Windows
    biosignal_env\Scripts\activate
    
    # On macOS/Linux
    source biosignal_env/bin/activate
    
    # Install the package
    pip install git+https://github.com/NsquaredLab/Biosignal-Device-Interface.git

Getting Help
============

If you continue to have installation issues:

1. Check the `GitHub Issues <https://github.com/NsquaredLab/Biosignal-Device-Interface/issues>`_ page
2. Create a new issue with:
   - Your operating system and version
   - Python version
   - Complete error message
   - Installation method attempted

Next Steps
==========

Once installation is complete, proceed to the :doc:`quickstart` guide to begin using the Biosignal Device Interface. 