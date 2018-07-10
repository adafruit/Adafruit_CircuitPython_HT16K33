import time
import board
import busio
from adafruit_ht16k33.bargraph import Bicolor24

i2c = busio.I2C(board.SCL, board.SDA)

bar = Bicolor24(i2c)

bar[0] = bar.LED_RED
bar[1] = bar.LED_GREEN
bar[2] = bar.LED_YELLOW

time.sleep(2)

bar.fill(bar.LED_OFF)

for i in range(24):
    bar[i] = bar.LED_RED
    time.sleep(0.1)
    bar[i] = bar.LED_OFF

time.sleep(1)

bar.fill(bar.LED_GREEN)
