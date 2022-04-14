import network
from network import WLAN, LoRa
from machine import I2C, RTC, Timer, Pin, deepsleep
import machine
import ustruct
import socket
import pycom
import time
import sys
import struct
import _thread
from dth import DTH
from machine import WDT
from network import Server

i2c = I2C(0)                         # create on bus 0
i2c = I2C(0, I2C.MASTER)             # create and init as a master
i2c.init(I2C.MASTER, baudrate=100000) # init as a master

#############################---ADS1115-CHANNELS---#############################
_CHANNEL0=const(0xC3)   #channel waterLevelSensor
_CHANNEL1=const(0xD3)   #channel battery
_CHANNEL2=const(0xE3)
_CHANNEL3=const(0xF3)

#############################----ads1115Write----###############################
#Configura el ads1115 en modo Single-Shot, y habilita el canal (channel)
def ads1115Write(channel):
    data = ustruct.pack('>BBB', 0x01,channel,0x83)
    i2c.init()
    i2c.writeto(0x48, data)
    time.sleep(0.5)
    i2c.deinit()
################################----ads1115Read----#############################
#Adquiere los datos analógicos de channel(habilitado en ads1115Write)
def ads1115Read():
    i2c.init()
    data = i2c.readfrom_mem(0x48, 0x00, 2 )
    i2c.deinit()
    time.sleep(0.1)
    vX=ustruct.unpack('>H', data)[0]
    print(vX)
    return vX

def ReadChannel_0():

    ads1115Write(_CHANNEL0)
    SolarRadiation = ads1115Read()
    SolarRadiation=SolarRadiation*0.074852
    print(SolarRadiation)

def ReadChannel_1():

    ads1115Write(_CHANNEL1)
    batteryVolt = ads1115Read()

def ReadPulseCounterPluvio():
    i2c.init()
    pulse=i2c.readfrom(0x32,3)
    i2c.deinit()
    print(pulse[0],pulse[1],pulse[2])
    pulse2_bin="%08d" % int(bin(pulse[2])[2:])
    pulse1_bin="%08d" % int(bin(pulse[1])[2:])
    pulse0_bin="%08d" % int(bin(pulse[0])[2:])
    totPulse_bin=pulse0_bin+pulse1_bin+pulse2_bin
    print(totPulse_bin)
    totPulse_int= int("%24d" % int(totPulse_bin),2)
    print(totPulse_int)
