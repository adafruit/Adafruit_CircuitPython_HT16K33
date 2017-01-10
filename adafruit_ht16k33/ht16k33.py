from adafruit_register import i2c_struct
from adafruit_bus_device import i2c_device


_HT16K33_BLINK_CMD = const(0x80)
_HT16K33_BLINK_DISPLAYON = const(0x01)
_HT16K33_CMD_BRIGHTNESS = const(0xE0)
_HT16K33_OSCILATOR_ON = const(0x21)


class HT16K33:
    def __init__(self, i2c, address=0x70):
        self.i2c_device = i2c_device.I2CDevice(i2c, address)
        self._temp = bytearray(1)
        self._buffer = bytearray(17)
        self.fill(0)
        self._write_cmd(_HT16K33_OSCILATOR_ON)
        self.blink_rate(0)
        self.brightness(15)

    def _write_cmd(self, byte):
        self._temp[0] = byte
        with self.i2c_device:
            self.i2c_device.writeto(self._temp)

    def blink_rate(self, rate=None):
        if rate is None:
            return self._blink_rate
        rate = rate & 0x03
        self._blink_rate = rate
        self._write_cmd(_HT16K33_BLINK_CMD |
                        _HT16K33_BLINK_DISPLAYON | rate << 1)

    def brightness(self, brightness):
        if brightness is None:
            return self._brightness
        brightness = brightness & 0x0F
        self._brightness = brightness
        self._write_cmd(_HT16K33_CMD_BRIGHTNESS | brightness)

    def show(self):
        with self.i2c_device:
            self.i2c_device.writeto(self._buffer)  # Byte 0 is 0x00, address of
                                                   # LED data register.  The
                                                   # remaining 16 bytes are The
                                                   # display register data to set.

    def fill(self, color):
        fill = 0xff if color else 0x00
        for i in range(16):
            self._buffer[i+1] = fill

    def _pixel(self, x, y, color=None):
        mask = 1 << x
        if color is None:
            return bool((self._buffer[y + 1] | self._buffer[y + 2] << 8) & mask)
        if color:
            self._buffer[(y * 2) + 1] |= mask & 0xff
            self._buffer[(y * 2) + 2] |= mask >> 8
        else:
            self._buffer[(y * 2) + 1] &= ~(mask & 0xff)
            self._buffer[(y * 2) + 2] &= ~(mask >> 8)

    def _set_buffer(self, i, value):
        self._buffer[i+1] = value  # Offset by 1 to move past register address.

    def _get_buffer(self, i):
        return self._buffer[i+1]   # Offset by 1 to move past register address.
