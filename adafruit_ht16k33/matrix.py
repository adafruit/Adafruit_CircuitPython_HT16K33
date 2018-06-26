# The MIT License (MIT)
#
# Copyright (c) 2016 Radomir Dopieralski & Tony DiCola for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Matrix Displays
================

"""

from adafruit_ht16k33.ht16k33 import HT16K33


class Matrix16x8(HT16K33):
    """A double matrix or the matrix wing."""
    def pixel(self, x, y, color=None):
        """Get or set the color of a given pixel."""
        if not 0 <= x <= 15:
            return None
        if not 0 <= y <= 7:
            return None
        if x >= 8:
            x -= 8
            y += 8
        return super()._pixel(y, x, color)

    def __getitem__(self, key):
        x, y = key
        return self.pixel(x, y)

    def __setitem__(self, key, value):
        x, y = key
        self.pixel(x, y, value)

class Matrix8x8(HT16K33):
    """A single matrix."""
    def pixel(self, x, y, color=None):
        """Get or set the color of a given pixel."""
        if not 0 <= x <= 7:
            return None
        if not 0 <= y <= 7:
            return None
        x = (x - 1) % 8
        return super()._pixel(x, y, color)

    def __getitem__(self, key):
        x, y = key
        return self.pixel(x, y)

    def __setitem__(self, key, value):
        x, y = key
        self.pixel(x, y, value)

class Matrix8x8x2(HT16K33):
    """A bi-color matrix."""
    def pixel(self, x, y, color=None):
        """Get or set the color of a given pixel."""
        if not 0 <= x <= 7:
            return None
        if not 0 <= y <= 7:
            return None
        if color is not None:
            super()._pixel(y, x, (color & 0x01))
            super()._pixel(y + 8, x, (color >> 1) & 0x01)
        else:
            return super()._pixel(y, x) | super()._pixel(y + 8, x) << 1
        return None

    def __getitem__(self, key):
        x, y = key
        return self.pixel(x, y)

    def __setitem__(self, key, value):
        x, y = key
        self.pixel(x, y, value)

    def fill(self, color):
        """Fill the whole display with the given color."""
        fill1 = 0xff if color & 0x01 else 0x00
        fill2 = 0xff if color & 0x02 else 0x00
        for i in range(8):
            self._set_buffer(i * 2, fill1)
            self._set_buffer(i * 2 + 1, fill2)
        if self._auto_write:
            self.show()
