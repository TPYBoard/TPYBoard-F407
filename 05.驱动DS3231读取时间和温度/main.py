# main.py -- put your code here!
import pyb
from ds3231 import DS3231  
ds=DS3231(1)
#��������
ds.DATE([19,04,01])
#����ʱ��
ds.TIME([15,10,10])
#��ʱ5��鿴Ч��
pyb.delay(5000)
#��ȡ�벢��ӡ
print(ds.sec())
#��ȡ����
print(ds.DATE())
#��ȡʱ��
print(ds.TIME())

#��ȡ�¶�
print(ds.TEMP())