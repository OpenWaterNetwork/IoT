import os
import pycom
from pycom import heartbeat
from pycom import rgbled
from network import LoRa
from machine import Pin
import socket
import time
import utime
from machine import Timer
from machine import RTC
from machine import I2C
import struct
import ustruct
import binascii
from network import WLAN
from dth import DTH
from network import Server
from machine import ADC
import _thread
from network import Server
import network
import ssl
from ds3231 import DS3231
from sim800L import SIM800L
from mqtt import MQTTClient
import config
from nanogateway import NanoGateway
from lorap2p import LORAP2P
from machine import WDT

#-- Start watchDog 180 seconds
wdt = WDT(timeout=180000)

####################################Pin reset config ###########################
################################################################################
def GPRS_reset():
    p_out_8.value(0)
    time.sleep(1)
    p_out_8.value(1)
    time.sleep(6)
    #sim800L.GPRS_init()

#######################    Create global variables       #######################
################################################################################

class Drips:
    pass

drips = Drips()

drips.wifi_flag=0
drips.count_int=0
drips.device_id=0

class General:
    pass

generals = General()

generals.flag_trans=0
generals.loraRW = None
generals.nanogw =None
generals.timeSincFlag=False
generals.alarma_temp = ""

arrayStationReceive = []
arrayStationTransmit = []
ArrayStation = []

wakeReason=int(machine.wake_reason()[0])


#########################-- RTC EXTERNAL--######################################
################################################################################

def sincTimeRTC_ext():

    wakeReason=int(machine.wake_reason()[0])

    try:
        timeSinc=pycom.nvs_get("tsf")
    except:
        pycom.nvs_set("tsf",20)
        timeSinc=pycom.nvs_get("tsf")

    if wakeReason == 2 or timeSinc == 10:
        ds3231.sinc_RTC_from_ds3231()
    else:
        time.sleep(5)
        sim800L.GPRS_init()
        time.sleep(2)
        timeSincGPRS = sim800L.GPRS_NTP()
        print(timeSincGPRS)
        if timeSincGPRS==True:
            pycom.nvs_set("tsf",10)
        else:
            pycom.nvs_set("tsf",20)
        ds3231.ds3231init_sinc()


############################# Start DHT11 library  #############################
################################################################################

def hum_temp_data():
    result = th.read()
    valtemp=0
    valhum=0

    if result.is_valid():
        valtemp=result.temperature
        valhum=result.humidity
        print("Temperature: %d C" % valtemp)
        print("Humidity: %d %%" % valhum)

    return int(valtemp),int(valhum)

##############################---adcConfig---###################################
################################################################################

def batery_data ():
    cont = 0
    for cont in range(100):
        matrizdatosvolt.append(adc_c.voltage())
    valor_bate = sum(matrizdatosvolt)/len(matrizdatosvolt)
    matrizdatosvolt.clear()
    valor_bate_int = int(valor_bate)
    print (valor_bate,valor_bate_int)
    return valor_bate_int

##########################----Pulsed Read Mode-----#############################
################################################################################

def config_mode(arg):
    if (arg.value()==0):
        time.sleep(2)
        if (p_in.value()==0):
            print("ECENDER WIFI")
            drips.wifi_flag=1
        #ds1307init_sinc()
        #obtener_ds1307()

#p_in.callback(Pin.IRQ_LOW_LEVEL, handler=config_mode)

############################### WIFI METHODS ###################################
################################################################################
def ServerFTPWifiOn():
    pycom.heartbeat(False)
    time.sleep(0.5)
    pycom.rgbled(0x007f00)
    wlan = WLAN(mode=WLAN.STA)
    wlan.init(mode=WLAN.AP, ssid='gateway-station', channel=7, antenna=WLAN.INT_ANT)  #auth=(WLAN.WPA2,'gateway-station')
    time.sleep(0.2)
    server= Server(login=('gateway', 'gateway'), timeout=60)
    server.timeout(300) # change the timeout
    server.timeout() # get the timeout
    print(server.isrunning()) # check whether the server is running or not
    time.sleep(1)
    pycom.heartbeat(False)

def ServerFTPwifiOff():
    pycom.heartbeat(False)
    time.sleep(0.5)
    pycom.rgbled(0x7f0000)
    wlan = WLAN(mode=WLAN.STA)
    wlan.init(mode=WLAN.AP, ssid='gateway-station', auth=(WLAN.WPA2,'gateway-station'), channel=7, antenna=WLAN.INT_ANT)
    wlan.deinit()
    time.sleep(1)
    pycom.heartbeat(False)
    drips.wifi_flag=0

def wlan_conect():
    # setup as a station
    wlan = network.WLAN(mode=network.WLAN.STA)
    wlan.connect('Name', auth=(network.WLAN.WPA2, 'Password'))#
    while not wlan.isconnected():
        time.sleep_ms(50)
    print(wlan.ifconfig())

def rtcWifiNtp():

    drips.count_int=drips.count_int+1

    if drips.count_int==4:
        machine.reset()

    wlan_conect()
    time.sleep(0.5)
    rtc.ntp_sync("ec.pool.ntp.org") #ec.pool.ntp.org inocar.ntp.ec
    time.sleep(0.2)
    print(rtc.now())
    print(rtc.synced())

    if rtc.synced()==False:

        time.sleep(1)
        wlan_conect()
        time.sleep(1)
        rtcWifiNtp()

    timeepoch = time.time() - 18000
    tuple_time=time.gmtime(timeepoch)
    rtc.init(tuple_time)
    print(rtc.now())
    rtc.ntp_sync(None)

################################################################################
############################ LORA COMMUNICATION METHODS ########################
def lorawanStart():
    floatServerConnect=True
    try:
        generals.loraRW.loraRaw_Stop()
        print("LoraRaw to LoraWan")
        generals.nanogw = NanoGateway(
            id=config.GATEWAY_ID,
            frequency=config.LORA_FREQUENCY,
            datarate=config.LORA_GW_DR,
            dir_sim=config.SIM,
            user_sim=config.SIM_USER,
            password_sim=config.SIM_PASS,
            server=config.SERVER,
            port=config.PORT,
            ntp_server='',
            ntp_reg='',
            ntp_period=False
            )

        floatServerConnect = generals.nanogw.start()
        if floatServerConnect==False:
            GPRS_reset()
            time.sleep(5)
            sim800L.GPRS_init()
            time.sleep(1)
            generals.nanogw.start()

    except:
        print("LoraWan Start")
        generals.nanogw = NanoGateway(
            id=config.GATEWAY_ID,
            frequency=config.LORA_FREQUENCY,
            datarate=config.LORA_GW_DR,
            dir_sim=config.SIM,
            user_sim=config.SIM_USER,
            password_sim=config.SIM_PASS,
            server=config.SERVER,
            port=config.PORT,
            ntp_server='',
            ntp_reg='',
            ntp_period=False
            )
        floatServerConnect = generals.nanogw.start()
        if floatServerConnect==False:
            GPRS_reset()
            time.sleep(5)
            sim800L.GPRS_init()
            time.sleep(1)
            generals.nanogw.start()

def SincTimeNodes():
    try:
        generals.nanogw.stop()
        print("LoraWan to LoraRaw")
        generals.loraRW=LORAP2P(config.LORA_FREQUENCY)
        generals.loraRW.loraRaw_Start()
    except:
        print("Start LoraRaw")
        generals.loraRW=LORAP2P(config.LORA_FREQUENCY)
        generals.loraRW.loraRaw_Start()

####################     5 minutes Interruption   ##############################
################################################################################

def segAlarm():
    timeStampM=time.localtime()
    minM = config.TIME_FREQ_SAMPLING-(timeStampM[4] % config.TIME_FREQ_SAMPLING)
    segM=minM*60-timeStampM[5]
    #print('timeStampM:segAlarm',timeStampM)
    return segM

def _seconds_handler_messu(alarm):
    generals.alarma_temp.cancel()
    print("System Sleep in a few seconds")
    Timer.Alarm(_seconds_handler_Sleep, 50, periodic=False)

def getAlarm():
    segundos_primeros= segAlarm()
    print("alarm will be activated in " + str(segundos_primeros) + " seconds" )
    generals.alarma_temp = Timer.Alarm(_seconds_handler_messu, segundos_primeros, periodic=False)

def _seconds_handler_Sleep(alarm):
    wdt.feed()
    generals.nanogw.stop()
    tiempoSinc=rtc.now()

    sim800L.GPRS_sleep()
    sleepMode(wakeReason)

############################ Data file Mahager #################################
################################################################################
def logsDir():

    try:
        files=os.listdir('data_storage')
        #os.remove(pathCurrentFile)
    except Exception as e:
        print("logsDir doesn't exist")
        os.mkdir('/flash/data_storage')
        time.sleep(0.1)

def gettemhum():

    result = th.read()
    valtemp=0
    valhum=0
    if result.is_valid():
         valtemp=result.temperature
         valhum=result.humidity
         print("Temperature: %d C" % valtemp)
         print("Humidity: %d %%" % valhum)
    return valtemp,valhum

def runModeOutConsole():
    print("Wake up on Run Mode - Off Console")
    pycom.nvs_set("tsf",10)
    pycom.nvs_set("mf",2)
    machine.reset()

def runModeInConsole():
    print("Wake up on Run Mode - ON Console")
    pycom.nvs_set("tsf",10)
    pycom.nvs_set("mf",3)
    machine.reset()

def resetConfig():
    print("Wake up on Config Mode")
    pycom.nvs_erase_all()
    machine.reset()

def sleepMode(motivoDespertar):

    segundos_primeros= (segAlarm()-20)*1000
    print("Wake up of system: " + str(segundos_primeros) + (" ms"))

    if (motivoDespertar==2 or motivoDespertar==0) and segundos_primeros > 40:

        sim800L.GPRS_sleep()
        time.sleep(1)
        segundos_primeros= (segAlarm()-80)*1000
        machine.deepsleep(segundos_primeros)

################# start object and variable initialization #####################
################################################################################
logsDir()

rtc = machine.RTC()
rtc.init((2018, 2, 5, 17, 52, 10, 0, 0),source=RTC.INTERNAL_RC) ## Clock Default initialization

sim800L = SIM800L(config.SIM, config.NTP) # Serial start and Reset GPRS
sim800L.atcom()
time.sleep(0.05)
sim800L.GPRS_wakeUp()

p_out_8 = Pin('P8', mode=Pin.OUT)
p_out_8.value(1)
#GPRS_reset()

ds3231 = DS3231()
sincTimeRTC_ext()

th = DTH('P23',1)

adc = ADC()
adc.vref(1060)
adc_c = adc.channel(pin='P20',attn=ADC.ATTN_11DB)

p_in_21 = Pin('P21', mode=Pin.IN,  pull=Pin.PULL_UP)
machine.pin_sleep_wakeup([p_in_21], machine.WAKEUP_ALL_LOW, True)

if int(machine.wake_reason()[0])==1:
    chrono = Timer.Chrono()
    print("System wake up")
    chrono.start()

    while p_in_21()==0:

        pulsedTime=chrono.read()

        if pulsedTime > 3.00 and pulsedTime< 5.00:
            pycom.heartbeat(False)
            time.sleep(0.5)
            pycom.rgbled(0x1f0000) # yellow
            time.sleep(1)
            pycom.heartbeat(False)
            time.sleep(1)
            pycom.nvs_set("mf",1)

        if pulsedTime > 5.00 and pulsedTime< 7.00:
            pycom.heartbeat(False)
            time.sleep(0.5)
            pycom.rgbled(0x001f00) # gr
            time.sleep(1)
            pycom.heartbeat(False)
            time.sleep(1)
            pycom.nvs_set("mf",2)

        if pulsedTime > 7.00 and pulsedTime< 9.00:
            pycom.heartbeat(False)
            time.sleep(0.5)
            pycom.rgbled(0x00001f) # gr
            time.sleep(1)
            pycom.heartbeat(False)
            time.sleep(1)
            pycom.nvs_set("mf",3)

    chrono.reset()

try:
    modeFun=pycom.nvs_get("mf")
except:
    pycom.nvs_set("mf",1)
    pycom.nvs_set("tef",0)
    modeFun=pycom.nvs_get("mf")

########################## Operating mode verification #########################
################################################################################
if modeFun== 3:

    uart = UART(0, baudrate=115200)
    os.dupterm(uart)
    print("Run Mode - console Start")
    getAlarm()
    time.sleep(2)
    lorawanStart()

    time.sleep(2)
    wakeReason=int(machine.wake_reason()[0])

    if wakeReason==0 or wakeReason==1:
        generals.nanogw.stop()
        sim800L.GPRS_sleep()
        time.sleep(1)
        sleepMode(0)

if modeFun== 2:

    print("Run Mode")
    uart.deinit()
    getAlarm()
    time.sleep(2)
    lorawanStart()
    time.sleep(2)

    wakeReason=int(machine.wake_reason()[0])

    if wakeReason==0 or wakeReason==1:
        generals.nanogw.stop()
        sim800L.GPRS_sleep()
        time.sleep(1)
        sleepMode(0)

if modeFun== 1 or modeFun== None:
    uart = UART(0, baudrate=115200)
    os.dupterm(uart)
    print("Config Mode")
    pycom.nvs_set("mf",1)
    SincTimeNodes()

########################## Infinite loop program ###############################
#################################################################################

def threadSleep(delay,id):

    wakeReason=int(machine.wake_reason()[0])
    chrono = Timer.Chrono()
    fecha_anterior=rtc.now()
    print(fecha_anterior)
    ServerFTPwifiOff()
    flagReceive=False

    while(True):

        tiemoptras=chrono.read()

        if (drips.wifi_flag==1):
            ServerFTPWifiOnwifiOn()
            drips.wifi_flag=0
            wif_encendido=1

        if (generals.flag_trans==1):
            chrono.reset()
            chrono.start()
            generals.flag_trans=0
            print("In a few seconds - sleep mode")

        if (int(tiemoptras)==50.00 and (modeFun==2 or modeFun==3)):
            wdt.feed()
            generals.nanogw.stop()
            tiempoSinc=rtc.now()

            sim800L.GPRS_sleep()
            sleepMode(wakeReason)

#_thread.start_new_thread(threadSleep,(1,2))
