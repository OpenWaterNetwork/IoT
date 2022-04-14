from network import LoRa
from machine import RTC
import pycom
import machine
import struct
import ustruct
import binascii
import socket
import time
import utime

class LORAP2P():

    def __init__(self,frequency):
        self._LORA_PKG_FORMAT = "!BBBB%ds"
        self.frequency = frequency
        self.lora_sock_raw = ""
        self.device_id = 240
        self.loraRaw = LoRa(mode=LoRa.LORA,region=LoRa.US915, frequency=self.frequency,tx_power=20, rx_iq=True,sf=12)
        self.arrayStationReceive=[]

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
        self.lora_sock_raw_ON()
        time_epoch=time.time()
        bin_time_epoch = bin(time_epoch)
        int_time_epoch = int(bin_time_epoch,2)
        pkg_time_epoch = struct.pack("I",int_time_epoch)
        pkg_sinc = struct.pack(self._LORA_PKG_FORMAT % len(pkg_time_epoch), self.device_id, len(pkg_time_epoch),0x02,device,pkg_time_epoch)
        self.lora_sock_raw.send(pkg_sinc)
        self.lora_sock_raw.close()

    def runModeFromLora(self):
        pycom.nvs_set("tsf",20)
        pycom.nvs_set("mf",2)
        machine.reset()

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

                #try:

                device_id, pkg_len, type_pkg, device_recept, msg = struct.unpack(self._LORA_PKG_FORMAT % recv_pkg_len, recv_pkg)
                print (device_id, msg, type_pkg,device_recept)

                if (type_pkg==6 and device_recept==self.device_id):
                    print("Synchronized "+str(device_id))
                    self.synchronizing(device_id)

                if (type_pkg==7 and device_recept==self.device_id):
                    print("Run Mode Start From Node")
                    self.runModeFromLora()
                #except Exception as e:
                #    print("Error Packet ")

            self.lora_sock_raw.close()

        if events & LoRa.TX_PACKET_EVENT:
            print('Lora packet sent')
