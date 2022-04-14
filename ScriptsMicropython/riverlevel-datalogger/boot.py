from machine import UART
import machine
import os
from network import WLAN
from network import Server
from machine import WDT

####### Uart para comunicación por consola #######

wdt = WDT(timeout=180000)

uart = UART(0, baudrate=115200)
os.dupterm(uart)

################# Apagar WIFI ######################

wlan = WLAN(mode=WLAN.STA)
wlan.init(mode=WLAN.AP, ssid='wipy-pluvio', auth=(WLAN.WPA2,'www.wipy.io'), channel=7, antenna=WLAN.INT_ANT)
wlan.deinit()

################# Archivo que se ejecutará priemro ################

machine.main('main.py')
