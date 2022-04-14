from network import LoRa
import socket
import ubinascii
import struct
import time
import binascii
import config

print("DEVEUI: ")
print(binascii.hexlify(LoRa(region=LoRa.US915).mac()).upper())

class LORAW():

    def __init__(self):

        self.loraw = LoRa(mode=LoRa.LORAWAN, region=LoRa.US915)

        self.dev_addr = struct.unpack(">l", ubinascii.unhexlify('260CBD62'))[0]
        self.nwk_swkey = ubinascii.unhexlify('7CBB6AFB2F43A64DFF8DFF187F1FE517')
        self.app_swkey = ubinascii.unhexlify('285AEE54A1B21CB3AB0A01DE61AD7842')

        # remove all the channels
        for channel in range(0,16):
            self.loraw.remove_channel(channel)

         # remove all the channels
        for channel in range(0,72):
            self.loraw.remove_channel(channel)

        # set all channels to the same frequency (must be before sending the OTAA join request
        for channel in range(8,16):
            self.loraw.add_channel(channel, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=3)

        # join a network using ABP (Activation By Personalization)
        self.loraw.join(activation=LoRa.ABP, auth=(self.dev_addr, self.nwk_swkey, self.app_swkey))

        # wait until the module has joined the network
        while not self.loraw.has_joined():
            time.sleep(2.5)
            print('Not yet joined...')

        print('Joined')

    def sendData(self, level, t_int, h_int, vol_int):

        self.sock_loraw = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        # set the LoRaWAN data rate
        self.sock_loraw.setsockopt(socket.SOL_LORA, socket.SO_DR, config.LORA_NODE_DR)
        # make the socket non-blocking
        self.sock_loraw.setblocking(False)

        print('Sending:')

        data = struct.pack(">H",level) + struct.pack(">H",t_int) + struct.pack(">H",h_int) + struct.pack(">H",vol_int)
        print(data)

        #data = struct.pack(">B",1) + struct.pack(">B",2) + struct.pack(">B",3) + struct.pack(">B",4)
        #print(data)


        self.sock_loraw.send(data)
        self.sock_loraw.close()

    def sendSinc(self):

        self.sock_loraw = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        # set the LoRaWAN data rate
        self.sock_loraw.setsockopt(socket.SOL_LORA, socket.SO_DR, 3)
        # make the socket non-blocking
        self.sock_loraw.setblocking(False)

        data='OK'
        self.sock_loraw.send(data)
        time.sleep(6)

        rx, port = self.sock_loraw.recvfrom(256)

        if rx:
            print('Received: {}, on port: {}'.format(rx, port))
        self.sock_loraw.close()
