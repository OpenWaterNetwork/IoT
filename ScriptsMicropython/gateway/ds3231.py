import time
import pycom
import os
from machine import RTC
from machine import I2C

class DS3231():

    def __init__(self):
        self.__i2c = I2C(0, I2C.MASTER, baudrate=100000)
        self.__rtc = RTC()
        time.sleep(1.0)
        self.__i2c.deinit()
###--Set external clock to default values.
    def DS3231init(self):
        self.__i2c.init()
        time.sleep(0.5)
        #self.__i2c.writeto(0x68,chr(0xD0))
        self.__i2c.writeto(0x68,chr(0))
        self.__i2c.writeto_mem(0x68,0,chr(0x00))
        self.__i2c.writeto_mem(0x68,1,chr(0x49))
        self.__i2c.writeto_mem(0x68,2,chr(0x17))
        self.__i2c.writeto_mem(0x68,4,chr(0x14))
        self.__i2c.writeto_mem(0x68,5,chr(0x06))
        self.__i2c.writeto_mem(0x68,6,chr(0x18))
        self.__i2c.writeto_mem(0x68,7,0x10)
        self.__i2c.deinit()
###-- Synchronize external clock ds3231 from the Lopy4 clock.
    def ds3231init_sinc(self):
        reloj_rtc_int=self.__rtc.now()
        hora_rtc_ext= str(reloj_rtc_int[3])
        hora_rtc_ext_hex = int(self.decode_ds3231(hora_rtc_ext))
        min_rtc_ext= str(reloj_rtc_int[4])
        min_rtc_ext_hex= int(self.decode_ds3231(min_rtc_ext))
        seg_rtc_ext= str(reloj_rtc_int[5])
        seg_rtc_ext_hex = int(self.decode_ds3231(seg_rtc_ext))
        dia_rtc_ext= str(reloj_rtc_int[2])
        dia_rtc_ext_hex = int(self.decode_ds3231(dia_rtc_ext))
        mes_rtc_ext= str(reloj_rtc_int[1])
        mes_rtc_ext_hex = int(self.decode_ds3231(mes_rtc_ext))
        ann_rtc_ext= str(reloj_rtc_int[0])
        ann_rtc_ext_hex = int(self.decode_ds3231(ann_rtc_ext[2:4]))
        #print(hora_rtc_ext_hex, min_rtc_ext_hex, seg_rtc_ext_hex)
        self.__i2c.init()
        self.__i2c.writeto(0x68,chr(0))
        self.__i2c.writeto_mem(0x68,0,chr(seg_rtc_ext_hex))
        self.__i2c.writeto_mem(0x68,1,chr(min_rtc_ext_hex))
        self.__i2c.writeto_mem(0x68,2,chr(hora_rtc_ext_hex))
        self.__i2c.writeto_mem(0x68,4,chr(dia_rtc_ext_hex))
        self.__i2c.writeto_mem(0x68,5,chr(mes_rtc_ext_hex))
        self.__i2c.writeto_mem(0x68,6,chr(ann_rtc_ext_hex))
        self.__i2c.writeto_mem(0x68,7,0x10)
        self.__i2c.deinit()
###-- Decode and Code Methods ds3231.
    def decode_ds3231(self,valor_rtc_int):
        binstring = ''
        x=int(valor_rtc_int)
        while True:
            q, r = divmod(x, 10)
            nibble = bin(r).replace('0b', "")
            while len(nibble) < 4:
                nibble = '0' + nibble
            binstring = nibble + binstring
            if q == 0:
                break
            else:
                x = q
        valorhex = int(binstring, 2)
        return valorhex

    def code_ds3231(self,valor_ds1307):
        valor=hex(ord(valor_ds1307))
        valor1= int(valor) & 15                     #segundos.encode("hex")
        valor2= int(valor)>>4
        valorint= int(str(valor2)+str(valor1))
        return valorint
###-- Get time from external clock ds3231.
    def get_time_ds3231(self):
        self.__i2c.init()
        #self.__i2c.writeto(0x68,chr(0xD0))
        self.__i2c.writeto(0x68,chr(0))
        #self.__i2c.writeto(0x68,chr(0xD1))
        segundos=self.__i2c.readfrom_mem(0x68,0,1)
        segundosint= self.code_ds3231(segundos)
        minutos=self.__i2c.readfrom_mem(0x68,1,1)
        minutosint=self.code_ds3231(minutos)
        horas=self.__i2c.readfrom_mem(0x68,2,1)
        horasint=self.code_ds3231(horas)
        dia=self.__i2c.readfrom_mem(0x68,4,1)
        diaint=self.code_ds3231(dia)
        mes=self.__i2c.readfrom_mem(0x68,5,1)
        mesint=self.code_ds3231(mes)
        ann=self.__i2c.readfrom_mem(0x68,6,1)
        annint=self.code_ds3231(ann)
        print(segundos,minutos,horas, segundosint, minutosint, horasint, diaint, mesint, annint)
        self.__i2c.deinit()
###-- Synchronize lopy4 from external clock ds3231.
    def sinc_RTC_from_ds3231(self):
        #self.__i2c = I2C(0, I2C.MASTER, baudrate=100000)
        self.__i2c.init()
        #self.__i2c.writeto(0x68,chr(0xD0))
        self.__i2c.writeto(0x68,chr(0))
        #self.__i2c.writeto(0x68,chr(0xD1))
        segundos=self.__i2c.readfrom_mem(0x68,0,1)
        segundosint= self.code_ds3231(segundos)
        minutos=self.__i2c.readfrom_mem(0x68,1,1)
        minutosint=self.code_ds3231(minutos)
        horas=self.__i2c.readfrom_mem(0x68,2,1)
        horasint=self.code_ds3231(horas)
        dia=self.__i2c.readfrom_mem(0x68,4,1)
        diaint=self.code_ds3231(dia)
        mes=self.__i2c.readfrom_mem(0x68,5,1)
        mesint=self.code_ds3231(mes)
        ann=self.__i2c.readfrom_mem(0x68,6,1)
        annint=self.code_ds3231(ann)+2000
        self.__i2c.deinit()
        self.__rtc.init((annint, mesint, diaint, horasint, minutosint, segundosint, 0, 0),source=RTC.INTERNAL_RC)
        print(self.__rtc.now())
