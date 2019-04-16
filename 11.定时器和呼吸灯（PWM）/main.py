# main.py -- put your code here!
from pyb import Pin
from pyb import Timer #导入库

#------------定时器-------------#
tim = pyb.Timer(4) #设置Timer编号
tim.init(freq=1) #设置频率，freq=1大约1秒1次。
tim.callback(lambda t:pyb.LED(4).toggle()) #注册回调函数。这里使用了lambda表达式

#------------PWM呼吸灯-------------#
p = Pin('X12',Pin.OUT_PP) 
tim = Timer(2, freq=1000)
ch = tim.channel(2, Timer.PWM, pin=p)

while True:
    for i in range(60):
        ch.pulse_width_percent(i)
        pyb.delay(20)
    for k in range(60,0,-1):
        ch.pulse_width_percent(k)
        pyb.delay(20)