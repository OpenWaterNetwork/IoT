from network import LoRa
from machine import RTC
from ds3231 import DS3231
from pycom import heartbeat
from pycom import rgbled
from machine import RTC
import pycom
import struct
import ustruct
import binascii
import socket
import time
import utime

class LORAP2P():

    def __init__(self,frequency):
        self._LORA_PKG_FORMAT = "BBBB%ds"
        self.DEVICE_ID = 2
        self.GATEWAY_ID = 240
        self.frequency = frequency
        self.lora_sock_raw = ""
        self.loraRaw = LoRa(mode=LoRa.LORA,region=LoRa.US915, frequency=self.frequency,tx_power=20, tx_iq=True,sf=12)
        self.arrayStationReceive=[]
        self.ds3231=DS3231()
        self.rtc = RTC()

    def lora_sock_raw_ON(self):
        self.lora_sock_raw = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        self.lora_sock_raw.setblocking(False)

    def loraRaw_Start(self):
        self.loraRaw.callback(trigger=(LoRa.RX_PACKET_EVENT | LoRa.TX_PACKET_EVENT), handler=self.lora_cb)
        self.lora_sock_raw_ON()

    def loraRaw_Stop(self):
        self.loraRaw.callback(trigger=None,handler=None)
        self.lora_sock_raw.close()

    def synchronizing(self,device):
        self.lora_sock_raw_ON(self)
        time_epoch=time.time()
        bin_time_epoch = bin(time_epoch)
        int_time_epoch = int(bin_time_epoch,2)
        pkg_time_epoch = struct.pack("I",int_time_epoch)
        pkg_sinc = struct.pack(self._LORA_PKG_FORMAT % len(pkg_time_epoch), self.device_id, len(pkg_time_epoch),0x02,device,pkg_time_epoch)
        self.lora_sock_raw.send(pkg_sinc)
        self.lora_sock_raw.close()

    def sincTimeForLora(self,time_sinc_epoch,loratupleinfo):
        tuple_time=time.gmtime(time_sinc_epoch[0])
        print (tuple_time)
        self.rtc.init(tuple_time)
        self.RssiledComprob(loratupleinfo)
        #razon_despertar=int(machine.wake_reason()[0])
        #sleepMode(razon_despertar)

    def RssiledComprob(self,loratupleinfo):
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

    def get_time(self):
        pkg_transmit="OK"
        PKG_TYPE=0x06
        self.lora_sock_raw_ON()
        pkg = struct.pack(self._LORA_PKG_FORMAT % len(pkg_transmit),self.DEVICE_ID, len(pkg_transmit),PKG_TYPE,self.GATEWAY_ID,pkg_transmit)
        self.lora_sock_raw.send(pkg)
        self.lora_sock_raw.close()

    def start_Gw(self):
        pkg_transmit="OK"
        PKG_TYPE=0x07
        self.lora_sock_raw_ON()
        pkg = struct.pack(self._LORA_PKG_FORMAT % len(pkg_transmit),self.DEVICE_ID, len(pkg_transmit),PKG_TYPE,self.GATEWAY_ID,pkg_transmit)
        self.lora_sock_raw.send(pkg)
        self.lora_sock_raw.close()

    ########################### LORA Interruption ##################################
    #################################################################################
    def lora_cb(self, lora):

        events = self.loraRaw.events()

        if events & LoRa.RX_PACKET_EVENT:

            print("Packet Received")
            self.lora_sock_raw_ON()
            recpakcom=self.lora_sock_raw.recvfrom(512)

            recv_pkg =recpakcom[0]
            print(self.loraRaw.stats())

            if (len(recv_pkg) > 2):

                recv_pkg_len = recv_pkg[1]

                try:

                    device_id, pkg_len, type_pkg, device_recept, msg = struct.unpack(self._LORA_PKG_FORMAT % recv_pkg_len, recv_pkg)
                    print (device_id, msg, type_pkg,device_recept)

                    if (type_pkg==2 and device_recept==self.DEVICE_ID):
                        time_sinc_epoch = struct.unpack("I",msg)
                        loratupleinfo=self.loraRaw.stats()
                        self.sincTimeForLora(time_sinc_epoch,loratupleinfo[1])

                except Exception as e:
                    print("Error Packet ")

            self.lora_sock_raw.close()

        if events & LoRa.TX_PACKET_EVENT:
            print('Lora packet sent')
