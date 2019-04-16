import pyb
from pyb import I2C

BMP180_I2C_ADDR = const(0x77)

class BMP180():
    def __init__(self, i2c_num):
        self.i2c = I2C(i2c_num, I2C.MASTER, baudrate = 100000)
        self.AC1 = self.short(self.get2Reg(0xAA))
        self.AC2 = self.short(self.get2Reg(0xAC))
        self.AC3 = self.short(self.get2Reg(0xAE))
        self.AC4 = self.get2Reg(0xB0)
        self.AC5 = self.get2Reg(0xB2)
        self.AC6 = self.get2Reg(0xB4)
        self.B1 = self.short(self.get2Reg(0xB6))
        self.B2 = self.short(self.get2Reg(0xB8))
        self.MB = self.short(self.get2Reg(0xBA))
        self.MC = self.short(self.get2Reg(0xBC))
        self.MD = self.short(self.get2Reg(0xBE))
        self.UT = 0
        self.UP = 0
        self.B3 = 0
        self.B4 = 0
        self.B5 = 0
        self.B6 = 0
        self.B7 = 0
        self.X1 = 0
        self.X2 = 0
        self.X3 = 0

    def short(self, dat):
        if dat > 32767:
            return dat - 65536
        else:
            return dat
    
    def setReg(self, dat, reg):
        buf = bytearray(2)
        buf[0] = reg
        buf[1] = dat
        self.i2c.send(buf, BMP180_I2C_ADDR)
        
    def getReg(self, reg):
        buf = bytearray(1)
        buf[0] = reg
        self.i2c.send(buf, BMP180_I2C_ADDR)
        t = self.i2c.recv(1, BMP180_I2C_ADDR)
        return t[0]
    
    def get2Reg(self, reg):
        a = self.getReg(reg)
        b = self.getReg(reg + 1)
        return a*256 + b
 
    def measure(self):
        self.setReg(0x2E, 0xF4)
        pyb.delay(5)
        self.UT = self.get2Reg(0xF6)
        self.setReg(0x34, 0xF4)
        pyb.delay(5)
        self.UP = self.get2Reg(0xF6)

    def getTemp(self):
        self.measure()
        self.X1 = (self.UT - self.AC6) * self.AC5/(1<<15)
        self.X2 = self.MC * (1<<11) / (self.X1 + self.MD)
        self.B5 = self.X1 + self.X2
        return (self.B5 + 8)/160
        
    def getPress(self):
        self.getTemp()
        self.B6 = self.B5 - 4000
        self.X1 = (self.B2 * (self.B6*self.B6/(1<<12))) / (1<<11)
        self.X2 = (self.AC2 * self.B6)/(1<<11)
        self.X3 = self.X1 + self.X2
        self.B3 = ((self.AC1*4+self.X3) + 2)/4
        self.X1 = self.AC3 * self.B6 / (1<<13)
        self.X2 = (self.B1 * (self.B6*self.B6/(1<<12))) / (1<<16)
        self.X3 = (self.X1 + self.X2 + 2)/4
        self.B4 = self.AC4 * (self.X3 + 32768)/(1<<15)
        self.B7 = (self.UP-self.B3) * 50000
        if self.B7 < 0x80000000:
            p = (self.B7*2)/self.B4
        else:
            p = (self.B7/self.B4) * 2
        self.X1 = (p/(1<<8))*(p/(1<<8))
        self.X1 = (self.X1 * 3038)/(1<<16)
        self.X2 = (-7357*p)/(1<<16)
        p = p + (self.X1 + self.X2 + 3791)/16
        return p
    
    def getAltitude(self):
        p = self.getPress()
        return (44330*(1-(p/101325)**(1/5.255)))

    def get(self):
        t = []
        t.append(self.getPress())
        t.append(self.getAltitude())
        t.append(self.getTemp())
        return t
