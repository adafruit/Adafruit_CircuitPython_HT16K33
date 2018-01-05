Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-ht16k33/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/ht16k33/en/latest/
    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

This is a library for using the I²C-based LED matrices with the HT16K33 chip.
It supports both 16x8 and 8x8 matrices, as well as 7- and 14-segment displays.

Note this library is intended for Adafruit CircuitPython's API.  For a library
compatible with MicroPython machine API see this library: https://github.com/adafruit/micropython-adafruit-ht16k33

Installation
=============
This driver depends on many other libraries! Please install it by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

.. code-block :: python

    # Import all board pins.
    from board import *
    import busio

    # Import the HT16K33 LED matrix module.
    from adafruit_ht16k33 import matrix

    # Create the I2C interface.
    i2c = busio.I2C(SCL, SDA)

    # Create the matrix class.
    # This creates a 16x8 matrix:
    matrix = matrix.Matrix16x8(i2c)
    # Or this creates a 8x8 matrix:
    #matrix = matrix.Matrix8x8(i2c)
    # Or this creates a 8x8 bicolor matrix:
    #matrix = matrix.Matrix8x8x2
    # Finally you can optionally specify a custom I2C address of the HT16k33 like:
    #matrix = matrix.Matrix16x8(i2c, address=0x70)

    # Clear the matrix.  Always call show after changing pixels to make the display
    # update visible!
    matrix.fill(0)
    matrix.show()

    # Set a pixel in the origin 0,0 position.
    matrix.pixel(0, 0, 1)
    # Set a pixel in the middle 8, 4 position.
    matrix.pixel(8, 4, 1)
    # Set a pixel in the opposite 15, 7 position.
    matrix.pixel(15, 7, 1)
    matrix.show()

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_HT16K33/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

API Reference
=============

.. toctree::
    :maxdepth: 2

    adafruit_ht16k33/index
