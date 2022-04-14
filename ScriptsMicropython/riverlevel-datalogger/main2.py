import os
import uos
from network import LoRa
import socket
import time
import utime
import ubinascii
from machine import RTC
import struct
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
from sim800L import SIM800L
from ds3231 import DS3231

wdt = WDT(timeout=180000)                                                       #Inicio watchDog para reseatear sistema en 180 segundos
sim800L=SIM800L()
ds3231_ext=DS3231()

################################################################################
##############################---DHT11Config---#################################
th = DTH('P23',1)

################################################################################
#############################--GloalUseVariable--###############################

global frecuencia_transmit                                                      #Variable de frecuencia de transmision

class Drips:
    pass

drips = Drips()
drips.timer10_flag=0                                                            #Bandera Global para comenzar lecturas de Sensor
drips.datos_serial=False                                                        #BAndera para lectura del Serial UArt a PIC
drips.wifi_bandera=0                                                            #BAndera que indica que wifi está activado
drips.pkg_transmit = struct.pack(">HiBH",4096,1510142703,0,3244)                #Varaiable de datos a transmitir
drips.lora_sock = ""                                                            #Variable global para socket lora

################################################################################
###############################---LoraConfig---################################
################################################################################
drips._LORA_PKG_FORMAT = "BBBB%ds"                                              #Formato de trama de datos a enviar via comunicación LoRa
drips.DEVICE_ID = 0x01                                                          #Id de dispositivo correspondiente a Nivek de Rio
drips.GATEWAY_ID = 240                                                          #Id de dispositivo correspondiente al Gateway alque esta conectada la estación
frecuencia_transmit=433000000                                                   #Variable de frecuencia de transmisión LoRa

lora = LoRa(mode=LoRa.LORA,region=LoRa.EU868, frequency=frecuencia_transmit,tx_power=20, tx_iq=True, sf=12)

def lora_sock_ON():
    drips.lora_sock = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    drips.lora_sock.setblocking(False)

################################################################################
########################### --readInterruption-- ###############################
################################################################################
def pin_handler(arg):
    #print("got an interrupt in pin %s" % (arg.id()))
    if (arg.value()==0):
        print("got an interrupt in pin %s" % (arg.id()))
        time.sleep(2)
        if (p_in.value()==0):
            print("ECENDER WIFI")
            drips.wifi_bandera=1
        #ds1307init_sinc()
        #obtener_ds1307()

#p_in = Pin('P19', mode=Pin.IN,  pull=Pin.PULL_UP) #//P22
#p_in.callback(Pin.IRQ_FALLING, handler=pin_handler)
p_21 = Pin('P21', mode=Pin.OUT)
p_21.hold(False)
p_21.value(0)

#machine.pin_deepsleep_wakeup(pins=['P3'], mode= machine.WAKEUP_ANY_HIGH, enable_pull=True)

################################################################################
############################-- InterruptloraTransmission --#####################
################################################################################
def lora_cb(lora):

    events = lora.events()

    if events & LoRa.RX_PACKET_EVENT:
        #print('Lora packet received')
        lora_sock_ON()
        recv_pkg = drips.lora_sock.recv(512)

        if (len(recv_pkg) > 2):
            recv_pkg_len = recv_pkg[1]
            device_id, pkg_len, type_pkg,device_recept,msg = struct.unpack(drips._LORA_PKG_FORMAT % recv_pkg_len, recv_pkg)
            #print (device_id, msg, type_pkg, device_recept)

        if (type_pkg==2 and device_recept==drips.DEVICE_ID):

            time_sinc_epoch = struct.unpack("I",msg)
            loratupleinfo=lora.stats()
            sincTimeForLora(time_sinc_epoch,loratupleinfo[1])

        if(type_pkg==0 and device_recept==drips.DEVICE_ID):
            print("Asignacion de Canal")
            time.sleep(2)
            transmitirPaquete()

        if(type_pkg==3 and device_recept==drips.DEVICE_ID):
            encenderwifi()

        if(type_pkg==4 and device_recept==drips.DEVICE_ID):
            apagarwifi()

        if(type_pkg==5 and device_recept==drips.DEVICE_ID):
            print("ack pkg")

        drips.lora_sock.close()

    if events & LoRa.TX_PACKET_EVENT:
        print('Lora packet sent')

lora.callback(trigger=(LoRa.RX_PACKET_EVENT | LoRa.TX_PACKET_EVENT), handler=lora_cb)

################################################################################
########################## --Gatewaysynchronization-- ##########################
################################################################################

def sincTimeForLora(time_sinc_epoch,loratupleinfo):

    tuple_time=time.gmtime(time_sinc_epoch[0])
    print (tuple_time)
    rtc.init(tuple_time)
    ds1307init_sinc()
    RssiledComprob(loratupleinfo)
    razon_despertar=int(machine.wake_reason()[0])
    sleepMode(razon_despertar)

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
def encenderwifi():
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

def apagarwifi():
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

def igualar_RTC_WIFI():
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
rtc.init((2018, 2, 5, 17, 52, 10, 0, 0),source=RTC.INTERNAL_RC)

def get_time():
    pkg_transmit="OK"
    PKG_TYPE=0x06
    lora_sock_ON()
    pkg = struct.pack(drips._LORA_PKG_FORMAT % len(pkg_transmit),drips.DEVICE_ID, len(pkg_transmit),PKG_TYPE,drips.GATEWAY_ID,pkg_transmit)
    drips.lora_sock.send(pkg)
    drips.lora_sock.close()

#####################################################################################
############################DataGet()################################################
#####################################################################################
#####################--ID--station and sensor-2bytes---#########################

def getIDS(packetTypePar):

    packetType=packetTypePar       #2bits
    stationId=7                    #12bits
    sensorIdWl=1                   #4bits
    sensorIdBl=20                  #12bits

    packetType_bits="{0:b}".format(packetType)
    stationId_bits="{0:b}".format(stationId)
    sensorIdWl_bits="{0:b}".format(sensorIdWl)
    sensorIdBl_bits="{0:b}".format(sensorIdBl)

    packetType_bits=(10-len(packetType_bits))*'0'+packetType_bits
    stationId_bits=(10-len(stationId_bits))*'0'+stationId_bits
    sensorIdWl_bits=(4-len(sensorIdWl_bits))*'0'+sensorIdWl_bits
    sensorIdBl_bits=(10-len(sensorIdBl_bits))*'0'+sensorIdBl_bits

    IDWl=(int('0b'+packetType_bits+stationId_bits+sensorIdWl_bits,2))
    IDBl=(int('0b'+stationId_bits+sensorIdBl_bits,2))

    print(IDWl)

    return IDWl

def batery_data ():
    cont = 0
    for cont in range(100):
        matrizdatosvolt.append(adc_c.voltage())
    valor_bate = sum(matrizdatosvolt)/len(matrizdatosvolt)
    matrizdatosvolt.clear()
    valor_bate_int = int(valor_bate)
    print (valor_bate,valor_bate_int)
    return valor_bate_int

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

def level_data():

    pin_11 = Pin('P11', mode=Pin.IN)
    time.sleep(0.2)
    data = pulses_get(pin_11, 100)

    return data

################################################################################
############################ -- StartMethods -- ################################
################################################################################

#wlan_conect()
#igualar_RTC_WIFI()
ds3231_ext.sinc_RTC_from_ds3231()

####################### --10SecondtoStartCont-- ################################
def segAlarm10():
    timeStampM=time.localtime()
    segM = 10-(timeStampM[5] % 10)
    return segM

def segAlarm():
    timeStampM=time.localtime()
    minM = 5-(timeStampM[4] % 5)
    segM=minM*60-timeStampM[5]
    print(segM)
    return segM

######################## --5minutscalculator-- ################################
def _seconds_handler_messu(alarm):
    print("Primeros activos")
    activar_5_min()
    datos_5min()

segundos_primeros= segAlarm()
alarma_temp=Timer.Alarm(_seconds_handler_messu, segundos_primeros, periodic=True)

def _seconds_handler_5min(alarm):
    print("alarma 5min")
    datos_5min()

def activar_5_min():
    alarma_temp.cancel()
    Timer.Alarm(_seconds_handler_5min, 300, periodic=True)

def datos_5min():

    reloj_var=rtc.now()
    dias_rtc=int(reloj_var[2])
    meses_rtc=int(reloj_var[1])
    ann_rtc=int(reloj_var[0])

    valtemp,valhum=hum_temp_data()
    level_ = level_data()

    pycom.heartbeat(False)
    pycom.rgbled(0x007f00)

    time_epoch=utime.time()
    bin_epoch= bin(time_epoch)
    binepoch = int(bin_epoch,2)

    pkg_save = struct.pack("iBBBH",binepoch,level_,valtemp,valhum)

    # Guardar datos en memoria Lopy4 #

    #log = open('/flash/data_rain/'+str(ann_rtc)+str(meses_rtc)+str(dias_rtc)+'.log', 'a')
    #log.write(pkg_save + '\r\n')
    #log.close()

    if int(reloj_var[4])==55:
        id_s_e=getIDS(1)
        drips.pkg_transmit = struct.pack(">HiBBBH",id_s_e,binepoch,level_,valtemp,valhum,valor_bate_int)

    else:

        id_s_e=getIDS(0)
        drips.pkg_transmit = struct.pack(">HiB",id_s_e,binepoch,level_)

    time.sleep(1)
    pycom.heartbeat(False)

################################################################################
############################# -- LoraPaquetTranssmit --#########################
################################################################################

def transmitirPaquete():
    lora_sock_ON()
    pkg = struct.pack(drips._LORA_PKG_FORMAT % len(drips.pkg_transmit), drips.DEVICE_ID, len(drips.pkg_transmit),0, drips.GATEWAY_ID ,drips.pkg_transmit)  # type_pkg=0 paquete de datos
    drips.lora_sock.send(pkg)
    drips.lora_sock.close()

def logsDir():
    try:
        files=os.listdir('levelData')
        #os.remove(pathCurrentFile)
    except Exception as e:
        print("logsDir doesn't exist")
        os.mkdir('/flash/levelData')
        time.sleep(0.1)

def sleepMode(motivoDespertar):
    segundos_primeros= (segAlarm()-10)*1000
    print(segundos_primeros)
    if motivoDespertar==0 and segundos_primeros > 15 :
        machine.deepsleep(segundos_primeros)

logsDir()
time.sleep(2)


################################################################################
############################# -- threadexecute --###############################
################################################################################

def th_func(delay,id):

    razon_despertar=int(machine.wake_reason()[0])
    print (razon_despertar)
    chrono = Timer.Chrono()
    drips.timer10_flag=1
    wif_encendido=0
    tiempoSinc=rtc.now()
    bandera_Sincronizar=True
    chrono.start()

    while(1):

        tiemoptras=chrono.read()
        tiempo_10=segAlarm10()

        #print(tiemoptras)
        if(tiempo_10==10 and drips.timer10_flag==1):
            drips.timer10_flag=0

        if(drips.wifi_bandera==1):
            encenderwifi()
            drips.wifi_bandera=0
            wif_encendido=1

        if razon_despertar==0:
            get_time()
            time.sleep(3)
            razon_despertar=3

        if(int(tiemoptras)==50.00 and wif_encendido==0):

            wdt.feed()
            p_21.value(1)
            p_21.hold(True)

            tiempoSinc=rtc.now()

            if (int(tiempoSinc[4])== 5 or int(tiempoSinc[4])==6 or int(tiempoSinc[4])==7 or int(tiempoSinc[4])==8 or int(tiempoSinc[4])==9):
                bandera_Sincronizar=False
                get_time()
                time.sleep(4)

            segundos_primeros= (segAlarm()-10)*1000
            print(segundos_primeros)
            machine.deepsleep(segundos_primeros)

_thread.start_new_thread(th_func,(1,1))
