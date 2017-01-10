Segment Displays
****************

.. module:: ht16k33_seg

.. class:: Seg14x4(i2c, address=0x70)

    Alpha-numeric, 14-segment display.

    .. method:: scroll(self, count=1)

        Scroll the display by specified number of places.

    .. method:: put(self, char, index=0)

        Put a character at the specified place.

    .. method:: push(self, char)

        Scroll the display and add a character at the end.

    .. method:: text(text)

        Display the specified text.

    .. method:: number(number)

        Display the specified decimal number.

    .. method:: hex(number)

        Display the specified hexadecimal number.

.. class:: Seg7x4(i2c, address-0x70)

    Numeric 7-segment display. It has the same methods as the alphanumeric
    diplsay, but only supports displaying decimal and hex digits, period and
    a minus sign.
