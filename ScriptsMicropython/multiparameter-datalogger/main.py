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
import config
from loraW import LORAW
from lorap2p import LORAP2P

#-- Start watchDog 180 seconds
wdt = WDT(timeout=180000)
#-- Config Ds3231 RTC external
ds3231_clock=DS3231()
#-- Config External temp and humidity sensor
sht = SHT11('P23', 'P22')
#-- Config Internal temp and humidity sensor
th = DTH('P21',1)
#-- Pin out config sensor watermarkSoil
out_in_Y = Pin('P11', mode=Pin.OUT,  pull=None)
P_12 = Pin('P12', mode=Pin.OUT,  pull=None)
p_SA= Pin('P3', mode=Pin.OUT,  pull=None)
p_SB= Pin('P8', mode=Pin.OUT,  pull=None)
#-- init value for pins sensor watermarkSoil
out_in_Y.value(0)
P_12.value(0)
#-- Pin switch 3,3 V
sw_3V_supply= Pin('P19', mode=Pin.OUT,  pull=None)
sw_3V_supply.hold(False)
sw_3V_supply.value(0)
#-- Init I2C to ds1307
i2c = I2C(0, I2C.MASTER, baudrate=100000)
#print(i2c.scan())
i2c.deinit()
#-- init external adc ads1115
i2c.init()
ads = ADS1115(i2c)
i2c.deinit()
#-- init internal adc
adc = ADC()
adc.init(bits=12)
apin = adc.channel(pin='P13',attn=ADC.ATTN_11DB)
#-- DS18B20 data line connected to pin P4
pin_P4 = Pin('P4', mode=Pin.OPEN_DRAIN, pull=None)
ow = OneWire(Pin(pin_P4))

## --GloalUseVariable
class Drips:
    pass

drips = Drips()
drips.wifi_bandera=0
drips.lorawanNode= None
drips.flag_trans = 0
drips.lw=None
drips.alarma_temp=None

wakeReason=int(machine.wake_reason()[0])

## -- LoraPaquetTranssmit

def joinLoraWan():
    drips.lorawanNode=LORAW()

def dataSendLoraWan():
    rain, t_int, h_int, t_ext, h_ext,t_18b20,s_rad,h_soil0,h_soil1,h_soil2,h_soil3,volt_node=sensors_data()
    msg = str(rain*0.2)+'\t'+ str((t_int-100)/10)+'\t'+ str(h_int/10)+'\t'+str((t_ext-100)/10)+'\t'+str(h_ext/10)+'\t'+ str((t_18b20-100)/10)+'\t'+ str(round(s_rad*0.074852,1))+'\t'+ str(h_soil0)+'\t'+str(h_soil1)+'\t'+str(h_soil2)+'\t'+str(h_soil3)+'\t'+str(round(4.2*(volt_node/1000)/3.3,1))
    dataStorage(1,msg)
    time.sleep(1)
    drips.lorawanNode.sendData(rain, t_int, h_int, t_ext, h_ext,t_18b20,s_rad,h_soil0,h_soil1,h_soil2,h_soil3,volt_node)
    time.sleep(2)
    drips.lorawanNode.sendData(rain, t_int, h_int, t_ext, h_ext,t_18b20,s_rad,h_soil0,h_soil1,h_soil2,h_soil3,volt_node)

def startGw():
    lr=LORAP2P(868100000)
    lr.loraRaw_Start()
    lr.start_Gw()

## --Gatewaysynchronization

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

##-- wifi-Method

def ON_wifi_fttp_server():
    pycom.heartbeat(False)
    time.sleep(0.5)
    pycom.rgbled(0x007f00)
    wlan = WLAN(mode=WLAN.STA)
    wlan.init(mode=WLAN.AP, ssid='WeatherStation', auth=(WLAN.WPA2,'WeatherStation'), channel=7, antenna=WLAN.INT_ANT)
    time.sleep(0.2)
    server= Server(login=('WeatherStation', 'WeatherStation'), timeout=60)
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

##-- synchronizationTimemethods

rtc = machine.RTC()
rtc.init((2021, 15, 6, 19, 20, 10, 0, 0),source=RTC.INTERNAL_RC)

##-- Stopwatch start

chronos = Timer.Chrono()

##--Data reading methods

def temHumInternal():

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

def ReadPulseCounterPluvio():
    i2c.init()
    pulse=i2c.readfrom(0x32,3)
    i2c.deinit()
    #print(pulse[0],pulse[1],pulse[2])
    pulse2_bin="%08d" % int(bin(pulse[2])[2:])
    pulse1_bin="%08d" % int(bin(pulse[1])[2:])
    pulse0_bin="%08d" % int(bin(pulse[0])[2:])
    totPulse_bin=pulse0_bin+pulse1_bin+pulse2_bin
    #print(totPulse_bin)
    totPulse_int= int("%24d" % int(totPulse_bin),2)
    #print(totPulse_int)
    timeReset=rtc.now()

    if timeReset[3]==0:
        reset_PLuv_cont= Pin('P20', mode=Pin.OUT)
        reset_PLuv_cont.value(0)
        time.sleep(0.5)
        reset_PLuv_cont.value(1)

    return totPulse_int

def read18b20Sensor():

    tempds18=DS18X20(ow)
    time.sleep(8)

    for i in range(0,2):
        tempds18.start_conversion()
        time.sleep_ms(750)
        temp18b20=tempds18.read_temp_async()

    return temp18b20

def ReadwatermarkSoil(sensor,temp_soil):

    if sensor == 0:
        p_SA.value(0)
        p_SB.value(0)
        hum_soil_CB=Read_ADCExternal_WatwerMArkSoil(temp_soil)
    if sensor== 1:
        p_SA.value(1)
        p_SB.value(0)
        hum_soil_CB=Read_ADCExternal_WatwerMArkSoil(temp_soil)
    if sensor==2:
        p_SA.value(0)
        p_SB.value(1)
        hum_soil_CB=Read_ADCExternal_WatwerMArkSoil(temp_soil)
    if sensor==3:
        p_SA.value(1)
        p_SB.value(1)
        hum_soil_CB=Read_ADCExternal_WatwerMArkSoil(temp_soil)

    return hum_soil_CB

def Read_ADCInternal_WatermarkSoil():

    out_in_Y.value(1)
    P_12.value(0)

    time.sleep_us(90)
    data1=apin.voltage()

    out_in_Y.value(0)

    print(data1)

    time.sleep_ms(100)

    out_in_Y.value(0)
    P_12.value(1)

    time.sleep_us(90)
    data2=apin.voltage()

    P_12.value(0)

    #print(data2)

def Read_ADCExternal_WatwerMArkSoil(temp_soil):

    out_in_Y.value(1)
    P_12.value(0)
    i2c.init()
    time.sleep_us(90)
    data1=ads.read(4,2,None)
    out_in_Y.value(0)

    time.sleep_ms(100)

    out_in_Y.value(0)
    P_12.value(1)
    time.sleep_us(90)
    data2= ads.read(4,2,None)
    i2c.deinit()
    P_12.value(0)

    volt1=round((data1*3.28)/26545,1)
    volt2=round((data2*3.28)/26545,1)

    #print(volt1, volt2)

    if volt1 ==0:
        volt1=0.01
        RD1= abs((7500 * (3.28 - volt1)) / volt1)
    else:
        RD1= abs((7500 * (3.28 - volt1)) / volt1)

    if volt2 ==0:
        volt2=0.01
        RD2= abs((7500 * volt2)/ (3.28 - volt2))
    else:
        RD2= abs((7500 * volt2)/ (3.28 - volt2))

    #print(RD1,RD2)

    RD = (RD1+RD2)/2

    #print(volt1,volt2,RD1,RD2,RD)

    hum_soil_CB = ShockkPa(RD/1000,temp_soil)

    return abs(hum_soil_CB)

def ShockkPa(Rkohm,tempDegC):

   # Calibration equation Shock, C.C., Barnum, J.M., Seddigh, M., 1998.
   # Calibration of Watermark Soil Moisture Sensors for Irrigation Management,
   # Proceedings of the International Irrigation Show, San Diego, California, USA. pp. 139-146.
   if(Rkohm<=0.094):
       wPotentialkPa=0
   elif(Rkohm>17.0):
       wPotentialkPa=255
   else:
       wPotentialkPa=(4.093 + 3.213 * Rkohm)/(1 - 0.009733 * Rkohm - 0.01205 * tempDegC)
   return wPotentialkPa

def ConvtoKPA(WM1_Resistance,TempC):

    open_resistance=17589.0 #check the open resistance value by replacing sensor with an open and replace the value here...this value might vary slightly with circuit components
    short_resistance=93.0 # similarly check short resistance by shorting the sensor terminals and replace the value here.
    short_CB=240
    open_CB=255
    print(WM1_Resistance)
    if WM1_Resistance>550.00:
        if WM1_Resistance>8000.00:
            WM1_CB=-2.246-5.239*(WM1_Resistance/1000.00)*(1+.018*(TempC-24.00))-.06756*(WM1_Resistance/1000.00)*(WM1_Resistance/1000.00)*((1.00+0.018*(TempC-24.00))*(1.00+0.018*(TempC-24.00)))
            #print("Entered WM1 >8000 Loop")
        elif (WM1_Resistance>1000.00):
            WM1_CB=(-3.213*(WM1_Resistance/1000.00)-4.093)/(1-0.009733*(WM1_Resistance/1000.00)-0.01205*(TempC))
            #print("Entered WM1 >1000 Loop")
        else:
            WM1_CB=((WM1_Resistance/1000.00)*23.156-12.736)*(1.00+0.018*(TempC-24.00))
            #print("Entered WM1>550 Loop")
    else:
        if (WM1_Resistance>=300.00):
            WM1_CB=0.00
            #print("Entered 550<WM1>0 Loop")
        if (WM1_Resistance<300.00 and WM1_Resistance>=short_resistance):
            WM1_CB=short_CB #240 is a fault code for sensor terminal short
            #print("Entered Sensor Short Loop WM1")
    if(WM1_Resistance>=open_resistance):
        WM1_CB=open_CB #255 is a fault code for open circuit or sensor not present
        #print("Entered Open or Fault Loop for WM1 \n")

    #print(WM1_CB)

    return WM1_CB

def SolarRadiation_ads1115():

    adsVal=[]
    adsVal.clear()
    i2c.init()
    for i in range(0, 10):
        adsVal.append(ads.read(4,0,None))
        time.sleep(0.05)
    i2c.deinit()

    #print(adsVal)
    solarRadVal=sum(adsVal)/len(adsVal)#*0.074852

    return solarRadVal

def BatteryVolt_ads1115():
    i2c.init()
    adsVal=ads.read(4,1,None)
    i2c.deinit()
    batteryVoltVal=(adsVal*3.3)/26545
    return batteryVoltVal

def avg_Mat(lista):
  s = 0
  for elemento in lista:
    s += elemento
  return s / float(len(lista))

def varianza(lista):
  s = 0
  m = avg_Mat(lista)
  for elemento in lista:
    s += (elemento - m) ** 2
  return s / float(len(lista))

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

def temHumExternal():
    tempOutMat=[]
    humOutMat=[]

    for i in range (0,5):
        tempOutMat.append(int(sht.temperature()*10))
        humOutMat.append(int(sht.humidity()*10))

    tempOut=moda(tempOutMat)
    humOut=moda(humOutMat)

    tempOutMat.clear()
    humOutMat.clear()

    return tempOut, humOut

##-- Data reading

def sensors_data():

    data=0

    try:
        temp18b20=read18b20Sensor()
        temp18b20=int(temp18b20*10)+100
        print("18b20 Temperature: ", (temp18b20-100)/10, '*C')
    except:
        temp18b20=0

    try:
        h_soil=ReadwatermarkSoil(0,(temp18b20-100)/10)
        h_soil0=int(h_soil)
        print("Soil humidity 0: ", h_soil0, 'CB')
        time.sleep(1)
        h_soil=ReadwatermarkSoil(1,(temp18b20-100)/10)
        h_soil1=int(h_soil)
        print("Soil humidity 1: ", h_soil1, 'CB')
        time.sleep(1)
        h_soil=ReadwatermarkSoil(2,(temp18b20-100)/10)
        h_soil2=int(h_soil)
        print("Soil humidity 2: ", h_soil2, 'CB')
        time.sleep(1)
        h_soil=ReadwatermarkSoil(3,(temp18b20-100)/10)
        h_soil3=int(h_soil)
        print("Soil humidity 3: ", h_soil3, 'CB')
    except:
        h_soil0=0
        h_soil1=0
        h_soil2=0
        h_soil3=0

    try:
        solarRAd=SolarRadiation_ads1115()
        solarRAd=int(solarRAd)
        print("Solar Radiation: ", round(solarRAd*0.074852,1))
    except:
        solarRAd=0

    try:
        batteryVolt=BatteryVolt_ads1115()
        batteryVolt=int(batteryVolt*1000)
        print("BatteryVolt_ads1115: ", round(4.2*(batteryVolt/1000)/3.3,1))
    except:
        batteryVolt=0

    try:
        rain=int(ReadPulseCounterPluvio())
        print("Rain: ", rain*0.2, "mm")
    except:
        rain=0

    #read temperature and humidity
    try:
        tempOut,humOut =temHumExternal()
        tempOut=int(tempOut+100)
        humOut=int(humOut)
        print('External Temperature: ', (tempOut-100)/10, '*C')
        print('External Humidity: ', (humOut)/10, '%')
    except:
        tempOut=0
        humOut=0

    try:
        #read temperature and humidity
        tempIn,humIn = temHumInternal()
        tempIn=int(tempIn+100)
        humIn=int(humIn+100)
        print('Internal Temperature: ', (tempIn-100)/10, '*C')
        print('Internal Humidity: ', (humIn)/10, '%')
    except:
        tempIn=0
        humIn=0


    return rain, tempIn, humIn, tempOut, humOut,temp18b20,solarRAd,h_soil0,h_soil1,h_soil2,h_soil3,batteryVolt

##- alarm activation methods - 5 min

def segAlarm():
    timeStampM=time.localtime()
    minM = config.TIME_FREQ_SAMPLING-(timeStampM[4] % config.TIME_FREQ_SAMPLING)
    segM=minM*60-timeStampM[5]
    #print('timeStampM:segAlarm',timeStampM)
    return segM

def _seconds_handler_messu(alarm):
    drips.alarma_temp.cancel()
    print("System start sleep Mode in a few seconds")
    Timer.Alarm(_seconds_handler_5min, 30, periodic=False)
    fiveMinData()

def getAlarm():
    segundos_primeros= segAlarm()
    print("alarm will be activated in " + str(segundos_primeros) + " seconds" )
    drips.alarma_temp = Timer.Alarm(_seconds_handler_messu, segundos_primeros, periodic=False)

def _seconds_handler_5min(alarm):

    wdt.feed()
    sw_3V_supply.value(1)
    sw_3V_supply.hold(True)

    sleepMode(wakeReason)

def fiveMinData():
    joinLoraWan()
    dataSendLoraWan()

############################ Data file Mahager #################################
################################################################################
def dataStorage(type,msg):

    if type ==1:

        try:
            files=os.listdir('data_WS01')
            #os.remove(pathCurrentFile)
        except Exception as e:
            print("logsDir doesn't exist")
            os.mkdir('/flash/data_WS01')
            time.sleep(0.1)

        files=os.listdir('data_WS01')
        #print(files)
        timeStamp=rtc.now()
        numfile=len(files)
        fecha = str(timeStamp[2])+"/"+str(timeStamp[1])+"/"+str(timeStamp[0])
        hora = str(timeStamp[3])+":"+str(timeStamp[4])+":"+str(timeStamp[5])
        namefile =str(timeStamp[2])+str(timeStamp[1])+str(timeStamp[0])+'.txt'
        compFile = namefile in files
        log = open('/flash/data_WS01/'+namefile, 'a')
        if compFile == False:
            log.write("Date"+'\t'+"Time"+'\t'+"rain"+'\t'+'t_int'+'\t'+'h_int'+'\t'+'t_ext'+'\t'+'h_ext'+'\t'+'t_18b20'+'\t'+'s_rad'+'\t'+'h_soil'+'\t'+'volt_node'+ '\r\n')
            time.sleep(0.2)
        log.write(fecha+'\t'+hora+'\t'+msg + '\r\n')
        log.close()

        sizefree=os.getfree("/flash")

        if sizefree<1500:
            removeFile(0)

def removeFile(numfile):
    try:
        files=os.listdir('data_WS01')
        dirRemove= "/flash/data_WS01/"+files[numfile]
        os.remove(dirRemove)
    except Exception as e:
        print("No file")

def runModeOutConsole():
    pycom.nvs_set("mf",2)
    machine.reset()

def runModeInConsole():
    pycom.nvs_set("mf",3)
    machine.reset()

def resetConfig():
    pycom.nvs_erase_all()

def sleepMode(motivoDespertar):

    segundos_primeros= (segAlarm())*1000
    print("Wake up of system: " + str(segundos_primeros) + (" ms"))
    if (motivoDespertar==2 or motivoDespertar==0) and segundos_primeros > 40 :
        time.sleep(1)
        segundos_primeros= (segAlarm()-20)*1000
        machine.deepsleep(segundos_primeros)

################# start object and variable initialization #####################
################################################################################

rtc = machine.RTC()

ds3231 = DS3231()

p_in_18 = Pin('P18', mode=Pin.IN,  pull=Pin.PULL_UP)
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
        sw_3V_supply.value(1)
        sw_3V_supply.hold(True)
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
        sw_3V_supply.value(1)
        sw_3V_supply.hold(True)
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

def th_func(delay,id):

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

        #if wakeReason==0:
            #get_time()
            #time.sleep(3)
            #wakeReason=3

        if (drips.flag_trans==1):
            chrono.reset()
            chrono.start()
            drips.flag_trans=0

        if(int(tiemoptras)==20.00 and (modeFun==2 or modeFun==3)):

            wdt.feed()
            sw_3V_supply.value(1)
            sw_3V_supply.hold(True)

            tiempoSinc=rtc.now()

            #if (int(tiempoSinc[4])== 5 or int(tiempoSinc[4])==6 or int(tiempoSinc[4])==7 or int(tiempoSinc[4])==8 or int(tiempoSinc[4])==9):
            #    bandera_Sincronizar=False
            #    SincNodefromGateway()

            sleepMode(wakeReason)

#_thread.start_new_thread(th_func,(1,1))
