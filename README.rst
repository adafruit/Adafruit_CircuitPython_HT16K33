Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-ht16k33/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/ht16k33/en/latest/
    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://travis-ci.com/adafruit/Adafruit_CircuitPython_HT16K33.svg?branch=master
    :target: https://travis-ci.com/adafruit/Adafruit_CircuitPython_HT16K33
    :alt: Build Status

This is a library for using the I²C-based LED matrices with the HT16K33 chip.
It supports both 16x8 and 8x8 matrices, as well as 7- and 14-segment displays.

* **Notes**

    #. This library is intended for Adafruit CircuitPython's API.  For a library compatible with MicroPython machine API see this `library <https://github.com/adafruit/micropython-adafruit-ht16k33>`_.

    #. This library does not work with the Trellis 4x4 LED+Keypad board. For that product use: `CircuitPython Trellis Library <https://github.com/adafruit/Adafruit_CircuitPython_Trellis/releases/latest>`_

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

.. code-block :: python

    # Import all board pins and bus interface.
    import board
    import busio

    # Import the HT16K33 LED matrix module.
    from adafruit_ht16k33 import matrix

    # Create the I2C interface.
    i2c = busio.I2C(board.SCL, board.SDA)

    # Create the matrix class.
    # This creates a 16x8 matrix:
    matrix = matrix.Matrix16x8(i2c)
    # Or this creates a 8x8 matrix:
    #matrix = matrix.Matrix8x8(i2c)
    # Or this creates a 8x8 bicolor matrix:
    #matrix = matrix.Matrix8x8x2
    # Finally you can optionally specify a custom I2C address of the HT16k33 like:
    #matrix = matrix.Matrix16x8(i2c, address=0x70)

    # Clear the matrix.
    matrix.fill(0)

    # Set a pixel in the origin 0,0 position.
    matrix[0, 0] = 1
    # Set a pixel in the middle 8, 4 position.
    matrix[8, 4] = 1
    # Set a pixel in the opposite 15, 7 position.
    matrix[15, 7] = 1
    matrix.show()

    # Change the brightness
    matrix.brightness = 8

    # Set the blink rate
    matrix.blink_rate = 2


Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_HT16K33/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix adafruit-circuitpython-ht16k33 --library_location .

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.
