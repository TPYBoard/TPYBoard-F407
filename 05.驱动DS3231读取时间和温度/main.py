# main.py -- put your code here!
import pyb
from ds3231 import DS3231  
ds=DS3231(1)
#设置日期
ds.DATE([19,04,01])
#设置时间
ds.TIME([15,10,10])
#延时5秒查看效果
pyb.delay(5000)
#读取秒并打印
print(ds.sec())
#读取日期
print(ds.DATE())
#读取时间
print(ds.TIME())

#读取温度
print(ds.TEMP())