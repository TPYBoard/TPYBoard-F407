import pyb
from pyb import UART
 
#定义HC-05/06蓝牙模块连接的串口
#串口编号2 波特率9600 收发数据超时时间100ms
uart = UART(2,9600,timeout=100)

while True:
    #判断串口缓存区是否有数据
    if uart.any() > 0:
        #读取全部数据,返回的是bytes
        data = uart.read()
        #字节数组转字符串
        id = data.decode()
        #字符串转整型
        id = int(id)
        #板载的LED编号是1~4，判断数据是否符合，防止程序异常
        if id > 0 and id < 5:
            pyb.LED(id).toggle()