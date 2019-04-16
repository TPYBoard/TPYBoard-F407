#main.py
import pyb
from pyb import Pin
from ds18b20 import DS18X20

DQ=DS18X20(Pin('Y12'))#DQ
while True:
	tem = DQ.read_temp()
	print(tem)
	pyb.delay(1000)
