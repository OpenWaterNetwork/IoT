import machine
import os
from machine import UART
from network import WLAN
from network import Server
from machine import WDT

#-- Start watchDog 180 seconds
wdt = WDT(timeout=180000)

#################### Uart for console communication ############################
################################################################################

uart = UART(0, baudrate=115200)
os.dupterm(uart)

#########################  Disable WIFI ########################################
################################################################################

wlan = WLAN(mode=WLAN.STA)
wlan.init(mode=WLAN.AP, ssid='gateway-station', auth=(WLAN.WPA2,'gateway-station'), channel=7, antenna=WLAN.INT_ANT)
wlan.deinit()

####################### File to be run first ###################################
################################################################################
machine.main('main.py')
