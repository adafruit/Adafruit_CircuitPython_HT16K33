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

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_HT16K33.git"

class Matrix8x8(HT16K33):
    """A single matrix."""
    _columns = 8
    _rows = 8

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

    def shift_right(self, rotate=False):
        """
        Shift all pixels right

        :param rotate: (Optional) Rotate the shifted pixels to the left side (default=False)
        """
        for y in range(0, self.rows):
            last_pixel = self[self.columns - 1, y] if rotate else 0
            for x in range(self.columns - 1, 0, -1):
                self[x, y] = self[x - 1, y]
            self[0, y] = last_pixel
        if self._auto_write:
            self.show()

    def shift_left(self, rotate=False):
        """
        Shift all pixels left

        :param rotate: (Optional) Rotate the shifted pixels to the right side (default=False)
        """
        for y in range(0, self.rows):
            last_pixel = self[0, y] if rotate else 0
            for x in range(0, self.columns - 1):
                self[x, y] = self[x + 1, y]
            self[self.columns - 1, y] = last_pixel
        if self._auto_write:
            self.show()

    def shift_up(self, rotate=False):
        """
        Shift all pixels up

        :param rotate: (Optional) Rotate the shifted pixels to bottom (default=False)
        """
        for x in range(0, self.columns):
            last_pixel = self[x, self.rows - 1] if rotate else 0
            for y in range(self.rows - 1, 0, -1):
                self[x, y] = self[x, y - 1]
            self[x, 0] = last_pixel
        if self._auto_write:
            self.show()

    def shift_down(self, rotate=False):
        """
        Shift all pixels down

        :param rotate: (Optional) Rotate the shifted pixels to top (default=False)
        """
        for x in range(0, self.columns):
            last_pixel = self[x, 0] if rotate else 0
            for y in range(0, self.rows - 1):
                self[x, y] = self[x, y + 1]
            self[x, self.rows - 1] = last_pixel
        if self._auto_write:
            self.show()

    @property
    def columns(self):
        """Read-only property for number of columns"""
        return self._columns

    @property
    def rows(self):
        """Read-only property for number of rows"""
        return self._rows

class Matrix16x8(Matrix8x8):
    """The matrix wing."""
    _columns = 16

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

class MatrixBackpack16x8(Matrix16x8):
    """A double matrix backpack."""
    def pixel(self, x, y, color=None):
        """Get or set the color of a given pixel."""
        if not 0 <= x <= 15:
            return None
        if not 0 <= y <= 7:
            return None
        return super()._pixel(x, y, color)

class Matrix8x8x2(Matrix8x8):
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

    def fill(self, color):
        """Fill the whole display with the given color."""
        fill1 = 0xff if color & 0x01 else 0x00
        fill2 = 0xff if color & 0x02 else 0x00
        for i in range(8):
            self._set_buffer(i * 2, fill1)
            self._set_buffer(i * 2 + 1, fill2)
        if self._auto_write:
            self.show()
