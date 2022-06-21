# SPDX-FileCopyrightText: Radomir Dopieralski 2016 for Adafruit Industries
# SPDX-FileCopyrightText: Tony DiCola 2016 for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_ht16k33.ht16k33`
===========================

* Authors: Radomir Dopieralski, Tony DiCola, and Melissa LeBlanc-Williams for Adafruit Industries

"""

from adafruit_bus_device import i2c_device
from micropython import const

try:
    from typing import Union, List, Tuple, Optional
    from busio import I2C
except ImportError:
    pass

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_HT16K33.git"

_HT16K33_BLINK_CMD = const(0x80)
_HT16K33_BLINK_DISPLAYON = const(0x01)
_HT16K33_CMD_BRIGHTNESS = const(0xE0)
_HT16K33_OSCILATOR_ON = const(0x21)


class HT16K33:
    """
    The base class for all displays. Contains common methods.

    :param I2C i2c: The I2C bus object
    :param int address: The I2C addess of the HT16K33.
    :param bool auto_write: True if the display should immediately change when
        set. If False, `show` must be called explicitly.
    :param float brightness: 0.0 - 1.0 default brightness level.
    """

    def __init__(
        self,
        i2c: I2C,
        address: Union[int, Tuple, List] = 0x70,
        auto_write: bool = True,
        brightness: float = 1.0,
    ) -> None:
        if isinstance(address, (tuple, list)):
            self.i2c_device = []
            for addr in address:
                self.i2c_device.append(i2c_device.I2CDevice(i2c, addr))
        else:
            self.i2c_device = [i2c_device.I2CDevice(i2c, address)]
        self._temp = bytearray(1)
        self._buffer_size = 17
        self._buffer = bytearray((self._buffer_size) * len(self.i2c_device))
        self._auto_write = auto_write
        self.fill(0)
        for i, _ in enumerate(self.i2c_device):
            self._write_cmd(_HT16K33_OSCILATOR_ON, i)
        self._blink_rate = None
        self._brightness = None
        self.blink_rate = 0
        self.brightness = brightness

    def _write_cmd(self, byte: bytearray, i2c_index: int = 0) -> None:
        self._temp[0] = byte
        with self.i2c_device[i2c_index]:
            self.i2c_device[i2c_index].write(self._temp)

    @property
    def blink_rate(self) -> int:
        """The blink rate. Range 0-3."""
        return self._blink_rate

    @blink_rate.setter
    def blink_rate(self, rate: Optional[int] = None) -> None:
        if not 0 <= rate <= 3:
            raise ValueError("Blink rate must be an integer in the range: 0-3")
        rate = rate & 0x03
        self._blink_rate = rate
        for index, _ in enumerate(self.i2c_device):
            self._write_cmd(
                _HT16K33_BLINK_CMD | _HT16K33_BLINK_DISPLAYON | rate << 1, index
            )

    @property
    def brightness(self) -> float:
        """The brightness. Range 0.0-1.0"""
        return self._brightness

    @brightness.setter
    def brightness(self, brightness: float) -> None:
        if not 0.0 <= brightness <= 1.0:
            raise ValueError(
                "Brightness must be a decimal number in the range: 0.0-1.0"
            )

        self._brightness = brightness
        xbright = round(15 * brightness)
        xbright = xbright & 0x0F
        for index, _ in enumerate(self.i2c_device):
            self._write_cmd(_HT16K33_CMD_BRIGHTNESS | xbright, index)

    @property
    def auto_write(self) -> bool:
        """Auto write updates to the display."""
        return self._auto_write

    @auto_write.setter
    def auto_write(self, auto_write: bool) -> None:
        if isinstance(auto_write, bool):
            self._auto_write = auto_write
        else:
            raise ValueError("Must set to either True or False.")

    def show(self) -> None:
        """Refresh the display and show the changes."""
        for index, i2c_dev in enumerate(self.i2c_device):
            with i2c_dev:
                # Byte 0 is 0x00, address of LED data register. The remaining 16
                # bytes are the display register data to set.
                offset = index * self._buffer_size
                buffer = self._buffer[offset : offset + self._buffer_size]
                i2c_dev.write(buffer)

    def fill(self, color: bool) -> None:
        """Fill the whole display with the given color.

        :param bool color: Whether to fill the display
        """

        fill = 0xFF if color else 0x00
        for device, _ in enumerate(self.i2c_device):
            for i in range(self._buffer_size - 1):
                self._buffer[device * self._buffer_size + i + 1] = fill
        if self._auto_write:
            self.show()

    def _pixel(self, x: int, y: int, color: Optional[bool] = None) -> Optional[bool]:
        offset = ((x // 16) + (y // 8)) * self._buffer_size
        addr = 2 * (y % 8) + ((x % 16) // 8)
        addr = (addr % 16) + offset
        mask = 1 << x % 8
        if color is None:
            return bool(self._buffer[addr + 1] & mask)
        if color:
            # set the bit
            self._buffer[addr + 1] |= mask
        else:
            # clear the bit
            self._buffer[addr + 1] &= ~mask
        if self._auto_write:
            self.show()
        return None

    def _set_buffer(self, i: int, value: bool) -> None:
        self._buffer[i + 1] = value  # Offset by 1 to move past register address.

    def _get_buffer(self, i: int) -> bool:
        return self._buffer[i + 1]  # Offset by 1 to move past register address.
