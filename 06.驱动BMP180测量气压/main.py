from bmp180 import BMP180

bmp=BMP180(1)
tem=bmp.getTemp()
press=bmp.getPress()
altitude=bmp.getAltitude()
print('tem:',tem)
print('press:',press)
print('altude:',altitude)