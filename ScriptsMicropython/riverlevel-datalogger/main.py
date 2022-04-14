import os
import uos
from network import LoRa
import socket
import time
import utime
import ubinascii
from machine import RTC
import struct
import ustruct
from machine import I2C
from machine import ADC
from machine import SPI
from machine import Pin
from machine import Timer
import machine
from network import WLAN
import _thread
import binascii
import pycom
import math
from dth import DTH
from network import Server
import network
from machine import WDT
from pycom import pulses_get
from ds3231 import DS3231
from sht11 import SHT11
from sim800L import SIM800L
from onewire import DS18X20
from onewire import OneWire
from ads1x15 import ADS1115
from loraW import LORAW
from lorap2p import LORAP2P
import config

#-- Start watchDog 180 seconds
wdt = WDT(timeout=180000)
#-- Config Ds3231 RTC external
ds3231_clock=DS3231()
#-- Config Internal temp and humidity sensor
th = DTH('P23',1)
#-- Pin switch 3,3 V
sw_3V_supply= Pin('P21', mode=Pin.OUT,  pull=None)
sw_3V_supply.hold(False)
time.sleep(0.2)
sw_3V_supply.value(0)
time.sleep(0.2)
sw_3V_supply.value(1)
time.sleep(0.2)
sw_3V_supply.value(0)
#-- Init I2C to ds1307
i2c = I2C(0, I2C.MASTER, baudrate=100000)
#print(i2c.scan())
i2c.deinit()
#-- init internal adc
adc = ADC()
adc.init(bits=12)
apin = adc.channel(pin='P20',attn=ADC.ATTN_11DB)
#--wake_reason
wakeReason=int(machine.wake_reason()[0])
print (wakeReason)

################################################################################
#############################--GloalUseVariable--###############################

global frecuencia_transmit

class Drips:
    pass

drips = Drips()
drips.wifi_bandera=0
drips.lorawanNode= None
drips.flag_trans = 0
drips.lw=None
drips.alarma_temp=None


################################################################################
############################# -- LoraPaquetTranssmit --#########################
################################################################################
def joinLoraWan():
    drips.lorawanNode=LORAW()

def dataSendLoraWan():

    tempIn,humIn,levelData,volt_node = sensors_data()
    #print(levelData,tempIn,humIn, volt_node)

    msg = str((tempIn-100)/10)+'\t'+ str(humIn/10)+'\t'+str(levelData)+'\t'+ str(4.2*(volt_node/1000)/3.3)
    dataStorage(1,msg)

    time.sleep(1)
    drips.lorawanNode.sendData(levelData,tempIn,humIn,volt_node)
    time.sleep(2)
    drips.lorawanNode.sendData(levelData,tempIn,humIn,volt_node)

def startGw():
    lr=LORAP2P(868100000)
    lr.loraRaw_Start()
    lr.start_Gw()

################################################################################
########################## --Gatewaysynchronization-- ##########################
################################################################################
def SincNodefromGateway():
    lr=LORAP2P(config.LORA_FREQUENCY)
    lr.loraRaw_Start()
    lr.get_time()
    time.sleep(5)
    ds3231_clock.ds3231init_sinc()
    lr.loraRaw_Stop()

def sincTimeForLora(time_sinc_epoch,loratupleinfo):
    tuple_time=time.gmtime(time_sinc_epoch[0])
    print (tuple_time)
    rtc.init(tuple_time)
    ds3231_clock.ds3231init_sinc()
    RssiledComprob(loratupleinfo)
    wakeReason=int(machine.wake_reason()[0])
    sleepMode(wakeReason)

def RssiledComprob(loratupleinfo):
    if (loratupleinfo>-50):
        pycom.heartbeat(False)
        time.sleep(0.5)
        pycom.rgbled(0x007f00) # yellow
        time.sleep(0.5)
        pycom.heartbeat(False)
        time.sleep(0.5)
        pycom.rgbled(0x007f00) # yellow
        time.sleep(0.5)
        pycom.heartbeat(False)

    if (loratupleinfo>-80 and loratupleinfo<-50):
        pycom.heartbeat(False)
        time.sleep(0.5)
        pycom.rgbled(0x7f7f00) # yellow
        time.sleep(0.5)
        pycom.heartbeat(False)
        time.sleep(0.5)
        pycom.rgbled(0x7f7f00) # yellow
        time.sleep(0.5)
        pycom.heartbeat(False)
    if (loratupleinfo>-100 and loratupleinfo<-80):
        pycom.heartbeat(False)
        time.sleep(0.5)
        pycom.rgbled(0x7f0000) # yellow
        time.sleep(0.5)
        pycom.heartbeat(False)
        time.sleep(0.5)
        pycom.rgbled(0x7f0000) # yellow
        time.sleep(0.5)
        pycom.heartbeat(False)

################################################################################
###################################-- wifi-Method --############################
################################################################################
def ON_wifi_fttp_server():
    pycom.heartbeat(False)
    time.sleep(0.5)
    pycom.rgbled(0x007f00)
    wlan = WLAN(mode=WLAN.STA)
    wlan.init(mode=WLAN.AP, ssid='RiverLevel', auth=(WLAN.WPA2,'RiverLevel'), channel=7, antenna=WLAN.INT_ANT)
    time.sleep(0.2)
    server= Server(login=('RiverLevel', 'RiverLevel'), timeout=60)
    server.timeout(300) # change the timeout
    server.timeout() # get the timeout
    print(server.isrunning()) # check whether the server is running or not
    time.sleep(1)
    #pycom.heartbeat(False)

def OFF_wifi():
    pycom.heartbeat(False)
    time.sleep(0.5)
    pycom.rgbled(0x7f0000)
    wlan = WLAN(mode=WLAN.STA)
    wlan.init(mode=WLAN.AP, ssid='RiverLevel', auth=(WLAN.WPA2,'RiverLevel'), channel=7, antenna=WLAN.INT_ANT)
    wlan.deinit()
    time.sleep(1)
    pycom.heartbeat(False)
    drips.wifi_bandera=0

def wlan_conect():
    # setup as a station
    wlan = network.WLAN(mode=network.WLAN.STA)
    wlan.connect('Ofi_ATIMC', auth=(network.WLAN.WPA2, 'diucucuenca'))
    while not wlan.isconnected():
        time.sleep_ms(50)
    print(wlan.ifconfig())

def sinc_RTC_Wifi():
    wlan_conect()
    time.sleep(0.5)
    rtc.ntp_sync("inocar.ntp.ec")
    time.sleep(0.2)
    print(rtc.synced())
    print(rtc.now())
    timeepoch = time.time() - 18000
    tuple_time=time.gmtime(timeepoch)
    rtc.init(tuple_time)
    print(rtc.now())
    ds1307init_sinc()

################################################################################
########################## synchronizationTimemethods ##########################
################################################################################
rtc = machine.RTC()
rtc.init((2021, 15, 6, 19, 20, 10, 0, 0),source=RTC.INTERNAL_RC)

chronos = Timer.Chrono()

def read_voltage():

    volt1=apin.value()

    for i in range(0,1000):
        volt1=apin.value()+volt1

    volt1=volt1/1001
    volt=(3300*volt1)/4095

    return int(volt)

def moda(datos):

    repeticiones = 0

    for i in datos:
        n = datos.count(i)
        if n > repeticiones:
            repeticiones = n

    moda = [] #Arreglo donde se guardara el o los valores de mayor frecuencia

    for i in datos:
        n = datos.count(i) # Devuelve el número de veces que x aparece enla lista.
        if n == repeticiones and i not in moda:
            moda.append(i)

    if len(moda) != len(datos):
        moda = moda[0]
    else:
        moda = datos[int((len(datos)/2))]

    return moda

def temHumInternal():

    th = DTH('P23',1)
    valtemp=0
    valhum=0
    valtempMAt=[]
    valhumMat=[]

    for i in range(0,10):

        result = th.read()

        if result.is_valid():
            valtempMAt.append(int(result.temperature*10))
            valhumMat.append(int(result.humidity*10))
        time.sleep(0.2)

    valtemp=moda(valtempMAt)
    valhum=moda(valhumMat)

    valtempMAt.clear()
    valhumMat.clear()

    return valtemp, valhum

def level_data():

    contNumRead=10
    _data_=[]
    pin_11 = Pin('P11', mode=Pin.OPEN_DRAIN)
    time.sleep(0.2)
    data = (pulses_get(pin_11, 100))
    #print(data)
    #while len(data)==0:
    for i in range(0,contNumRead):
        time.sleep(0.01)
        #print("lectura: "+ str(i))
        data= (pulses_get(pin_11, 100))
        if len(data)!=0:
            data_= data[0]
            #print(data_[1])
            _data_.append(data_[1])
    print(_data_)
    if len(_data_)==0:
        level=0
    else:
        level = int(sum(_data_)/len(_data_))
        _data_.clear()

    return level

def sensors_data():

    tempIn,humIn = temHumInternal()
    time.sleep(1)
    levelData=level_data()
    #levelData=1556
    tempIn=int(tempIn+100)
    humIn=int(humIn)
    volt_node=read_voltage()
    print('Internal Temperature: ', (tempIn-100)/10, '*C')
    print('Internal Humidity: ', (humIn)/10, '%')
    print('level River : ', levelData, 'mm')
    print('Volt : ', 4.2*(volt_node/1000)/3.3, 'V')

    return (tempIn,humIn,levelData,volt_node)

####################     5 minutes Interruption   ##############################
################################################################################

def segAlarm():
    timeStampM=time.localtime()
    minM = config.TIME_FREQ_SAMPLING-(timeStampM[4] % config.TIME_FREQ_SAMPLING)
    segM=minM*60-timeStampM[5]
    #print('timeStampM:segAlarm',timeStampM)
    return segM

def _seconds_handler_messu(alarm):
    drips.alarma_temp.cancel()
    print("System start sleep Mode in a few seconds")
    Timer.Alarm(_seconds_handler_SleepMode, 30, periodic=False)
    fiveMinData()

def getAlarm():
    segundos_primeros= segAlarm() + 20
    print("alarm will be activated in " + str(segundos_primeros) + " seconds" )
    drips.alarma_temp = Timer.Alarm(_seconds_handler_messu, segundos_primeros, periodic=False)

def _seconds_handler_SleepMode(alarm):
    sleepMode(wakeReason)

def fiveMinData():
    joinLoraWan()
    dataSendLoraWan()
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

def runModeOutConsole():
    pycom.nvs_set("mf",2)
    machine.reset()

def runModeInConsole():
    pycom.nvs_set("mf",3)
    machine.reset()

def resetConfig():
    pycom.nvs_erase_all()

def sleepMode(motivoDespertar):

    segundos_primeros= (segAlarm()-20)*1000
    print("Wake up of system: " + str(segundos_primeros) + (" ms"))

    if (motivoDespertar==2 or motivoDespertar==0) and segundos_primeros > 40:
        sw_3V_supply.value(1)
        sw_3V_supply.hold(True)
        time.sleep(1)
        segundos_primeros= (segAlarm()-20)*1000
        machine.deepsleep(segundos_primeros)

################# start object and variable initialization #####################
################################################################################
def dataStorage(type,msg):

    if type ==1:

        try:
            files=os.listdir('data_LS01')
            #os.remove(pathCurrentFile)
        except Exception as e:
            print("logsDir doesn't exist")
            os.mkdir('/flash/data_LS01')
            time.sleep(0.1)

        files=os.listdir('data_LS01')
        #print(files)
        timeStamp=rtc.now()
        numfile=len(files)
        fecha = str(timeStamp[2])+"/"+str(timeStamp[1])+"/"+str(timeStamp[0])
        hora = str(timeStamp[3])+":"+str(timeStamp[4])+":"+str(timeStamp[5])
        namefile = str(timeStamp[2])+str(timeStamp[1])+str(timeStamp[0])+'.txt'
        compFile = namefile in files
        log = open('/flash/data_LS01/'+namefile, 'a')
        if compFile == False:
            log.write("Date"+'\t'+"Time"+'\t'+'t_int'+'\t'+'h_int'+'\t'+'level'+'\t'+'volt_node'+ '\n')
            time.sleep(0.2)
        log.write(fecha+'\t'+hora+'\t'+msg + '\n')
        log.close()

        sizefree=os.getfree("/flash")

        if sizefree<1500:
            removeFile(0)

def removeFile(numfile):
    try:
        files=os.listdir('data_LS01')
        dirRemove= "/flash/data_LS01/"+files[numfile]
        os.remove(dirRemove)
    except Exception as e:
        print("No file")

rtc = machine.RTC()

ds3231 = DS3231()

p_in_18 = Pin('P19', mode=Pin.IN,  pull=Pin.PULL_UP)
machine.pin_sleep_wakeup([p_in_18], machine.WAKEUP_ALL_LOW, True)

if int(machine.wake_reason()[0])==1:
    chrono = Timer.Chrono()
    print("System wake up")
    chrono.start()

    while p_in_18()==0:

        pulsedTime=chrono.read()

        if pulsedTime > 3.00 and pulsedTime< 5.00:
            pycom.heartbeat(False)
            time.sleep(0.5)
            pycom.rgbled(0x1f0000) # red
            time.sleep(1)
            pycom.heartbeat(False)
            time.sleep(1)
            pycom.nvs_set("mf",1)

        if pulsedTime > 5.00 and pulsedTime< 7.00:
            pycom.heartbeat(False)
            time.sleep(0.5)
            pycom.rgbled(0x001f00) # green
            time.sleep(1)
            pycom.heartbeat(False)
            time.sleep(1)
            pycom.nvs_set("mf",2)

        if pulsedTime > 7.00 and pulsedTime< 9.00:
            pycom.heartbeat(False)
            time.sleep(0.5)
            pycom.rgbled(0x00001f) # blue
            time.sleep(1)
            pycom.heartbeat(False)
            time.sleep(1)
            pycom.nvs_set("mf",3)

    chrono.reset()

try:
    modeFun=pycom.nvs_get("mf")
except:
    pycom.nvs_set("mf",1)
    modeFun=pycom.nvs_get("mf")

########################## Operating mode verification #########################
################################################################################
if modeFun== 3:

    uart = UART(0, baudrate=115200)
    os.dupterm(uart)

    pycom.heartbeat(False)
    time.sleep(0.5)
    pycom.rgbled(0x00001f) # yellow
    time.sleep(1)
    pycom.heartbeat(False)

    print("Run Mode - console Start")
    ds3231_clock.sinc_RTC_from_ds3231()
    time.sleep(0.2)
    getAlarm()
    wakeReason=int(machine.wake_reason()[0])

    if wakeReason==0 or wakeReason==1:
        sleepMode(0)

if modeFun== 2:

    pycom.heartbeat(False)
    time.sleep(0.5)
    pycom.rgbled(0x001f00) # yellow
    time.sleep(1)
    pycom.heartbeat(False)

    print("Run Mode")
    uart.deinit()
    ds3231_clock.sinc_RTC_from_ds3231()
    time.sleep(0.2)
    getAlarm()

    wakeReason=int(machine.wake_reason()[0])

    if wakeReason==0 or wakeReason==1:
        sleepMode(0)

if modeFun== 1 or modeFun== None:

    pycom.heartbeat(False)
    time.sleep(0.5)
    pycom.rgbled(0x1f0000) # yellow
    time.sleep(1)
    pycom.heartbeat(False)

    print("Config Mode")
    ds3231_clock.sinc_RTC_from_ds3231()
    time.sleep(0.5)
    SincNodefromGateway()

################################################################################
############################# -- threadexecute --###############################
################################################################################

def threadSleep(delay,id):

    wakeReason=int(machine.wake_reason()[0])
    print (wakeReason)
    chrono = Timer.Chrono()
    wif_encendido=0
    tiempoSinc=rtc.now()
    bandera_Sincronizar=True

    while(1):

        tiemoptras=chrono.read()

        if(drips.wifi_bandera==1):
            ON_wifi_fttp_server()
            drips.wifi_bandera=0
            wif_encendido=1

        if (drips.flag_trans==1):
            chrono.start()
            drips.flag_trans=0

        if(int(tiemoptras)==15.00 and (modeFun==2 or modeFun==3)):
            wdt.feed()
            tiempoSinc=rtc.now()
            sleepMode(wakeReason)

#_thread.start_new_thread(threadSleep,(1,2))
