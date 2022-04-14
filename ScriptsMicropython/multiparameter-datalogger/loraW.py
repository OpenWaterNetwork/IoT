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

        self.dev_addr = struct.unpack(">l", ubinascii.unhexlify('260BF23D'))[0]
        self.nwk_swkey = ubinascii.unhexlify('38E3C9E456A44A36296B54BBE76DB983')
        self.app_swkey = ubinascii.unhexlify('7620C451A9D99707290654BDF6980DED')

        # remove all the channels
        for channel in range(0,72):
            self.loraw.remove_channel(channel)

        # set all channels to the same frequency (must be before sending the OTAA join request
        for channel in range(8,16):
            self.loraw.add_channel(channel, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=3)

        # set the 3 default channels to the same frequency (must be before sending the join request)
        #self.loraw.add_channel(8, frequency=903900000, dr_min=0, dr_max=3)
        #self.loraw.add_channel(1, frequency=903900000, dr_min=0, dr_max=3)
        #self.loraw.add_channel(2, frequency=903900000, dr_min=0, dr_max=3)

        # join a network using ABP (Activation By Personalization)
        self.loraw.join(activation=LoRa.ABP, auth=(self.dev_addr, self.nwk_swkey, self.app_swkey))

        # wait until the module has joined the network
        while not self.loraw.has_joined():
            time.sleep(2.5)
            print('Not yet joined...')

        print('Joined')

    def sendData(self, rain, t_int, h_int, t_ext, h_ext,t_18b20,s_rad,h_soil0,h_soil1,h_soil2,h_soil3,volt_node):

        self.sock_loraw = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        # set the LoRaWAN data rate
        self.sock_loraw.setsockopt(socket.SOL_LORA, socket.SO_DR, config.LORA_NODE_DR)
        # make the socket non-blocking
        self.sock_loraw.setblocking(False)

        print('Sending:')
        print (h_ext)
        data = struct.pack(">H",rain) + struct.pack(">H",t_int) + struct.pack(">H",h_int) + struct.pack(">H",t_ext) + struct.pack(">H",h_ext) + struct.pack(">H",t_18b20) + struct.pack(">H",s_rad) + struct.pack(">H",h_soil0) + struct.pack(">H",h_soil1) + struct.pack(">H",h_soil2) + struct.pack(">H",h_soil3) + struct.pack(">H",volt_node)
        print(data)

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
