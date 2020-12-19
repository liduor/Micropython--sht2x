# This program is distributed under Apache License Version 2.0
#
# (ɔ) Albertas Mickėnas 2016
# mic@wemakethings.net
# albertas@technariumas.lt
#

import time
from machine import I2C,  Pin
from sht2x import SHT2x


sensor = SHT2x(I2C(scl=Pin(5), sda=Pin(4)))


while True:
	temperature = sensor.getTemperature()
	humidity = sensor.getHumidity()
	print(str(temperature) + ", " + str(humidity))
	time.sleep(1)