import pyb
from pyb import UART
 
#����HC-05/06����ģ�����ӵĴ���
#���ڱ��2 ������9600 �շ����ݳ�ʱʱ��100ms
uart = UART(2,9600,timeout=100)

while True:
    #�жϴ��ڻ������Ƿ�������
    if uart.any() > 0:
        #��ȡȫ������,���ص���bytes
        data = uart.read()
        #�ֽ�����ת�ַ���
        id = data.decode()
        #�ַ���ת����
        id = int(id)
        #���ص�LED�����1~4���ж������Ƿ���ϣ���ֹ�����쳣
        if id > 0 and id < 5:
            pyb.LED(id).toggle()