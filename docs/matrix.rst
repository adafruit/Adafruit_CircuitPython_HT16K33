Matrices
********

.. module:: ht16k33_matrix

.. class:: HT16K33(i2c, address=0x70)

    The base class for all displays. Contains common methods.

    .. method:: blink_rate([rate])

        Get or set the blink rate. Range 0-3.

    .. method:: brightness([brightness])

        Get or set the brightness. Range 0-15.

    .. method:: show()

        Refresh the display and show the changes.

    .. method:: fill(color)

        Fill the whole display with the given color.

    .. method:: pixel(x, y, [color])

        Get or set the color of a given pixel.

.. class:: Matrix16x18

    A double matrix or the matrix wing.

.. class:: Matrix8x8

    A single matrix.

.. class:: Matrix8x8x2

    A bi-color matrix.
