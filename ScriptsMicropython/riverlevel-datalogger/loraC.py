import time
import pycom
import os
from machine import RTC
from machine import I2C

class LORAC():

    def __init__(self, id, frequency, datarate):
        self.id = id
        self.frequency = frequency
        self.datarate = datarate
        self.sf = self._dr_to_sf(self.datarate)
        self.bw = self._dr_to_bw(self.datarate)

    def start(self):
        """
        Starts the LoRaWAN .
        """
        self.lora = LoRa(
            mode=LoRa.LORA,
            region=LoRa.EU868,
            frequency=self.frequency,
            bandwidth=self.bw,
            sf=self.sf,
            preamble=8,
            coding_rate=LoRa.CODING_4_5,
            tx_iq=True
        )

        # create a raw LoRa socket
        self.lora_sock = usocket.socket(usocket.AF_LORA, usocket.SOCK_RAW)
        self.lora_sock.setblocking(False)
        self.lora_tx_done = False

        self.lora.callback(trigger=(LoRa.RX_PACKET_EVENT | LoRa.TX_PACKET_EVENT), handler=self._lora_cb)
        self._log('LoRaWAN online')

    def _dr_to_sf(self, dr):
        sf = dr[2:4]
        if sf[1] not in '0123456789':
            sf = sf[:1]
        return int(sf)

    def _dr_to_bw(self, dr):
        bw = dr[-5:]
        if bw == 'BW125':
            return LoRa.BW_125KHZ
        elif bw == 'BW250':
            return LoRa.BW_250KHZ
        else:
            return LoRa.BW_500KHZ

    def _sf_bw_to_dr(self, sf, bw):
        dr = 'SF' + str(sf)
        if bw == LoRa.BW_125KHZ:
            return dr + 'BW125'
        elif bw == LoRa.BW_250KHZ:
            return dr + 'BW250'
        else:
            return dr + 'BW500'

    def _lora_cb(self, lora):

        events = lora.events()

        if events & LoRa.RX_PACKET_EVENT:
            #print('Lora packet received')

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
                ON_wifi_fttp_server()

            if(type_pkg==4 and device_recept==drips.DEVICE_ID):
                OFF_wifi()

            if(type_pkg==5 and device_recept==drips.DEVICE_ID):
                print("ack pkg")

            drips.lora_sock.close()

        if events & LoRa.TX_PACKET_EVENT:
            print('Lora packet sent')
