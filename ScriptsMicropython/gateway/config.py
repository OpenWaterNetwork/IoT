""" LoPy Nano Gateway configuration options """

import machine
import ubinascii

WIFI_MAC = ubinascii.hexlify(machine.unique_id()).upper()

# Set  the Gateway ID to be the first 3 bytes of MAC address + 'FFFE' + last 3 bytes of MAC address
GATEWAY_ID = WIFI_MAC[:6] + "FFFE" + WIFI_MAC[6:12]

SIM = 'internet.claro.com.ec'
SIM_USER = ''
SIM_PASS = ''
NTP = "162.159.200.123" #inocar 190.15.128.72 #NTP pool: 162.159.200.1

SERVER = 'nam1.cloud.thethings.network'
PORT = 1700

## for EU868
#LORA_FREQUENCY = 868100000
#LORA_GW_DR = "SF12BW125" # DR_0
#LORA_NODE_DR = 0

## for US915      904500000
LORA_FREQUENCY = 904500000
LORA_GW_DR = "SF9BW125" # DR_1
LORA_NODE_DR = 1

## for EU433
#LORA_FREQUENCY = 433375000
#LORA_GW_DR = "SF12BW125" # DR_0
#LORA_NODE_DR = 0

## for CN470
#LORA_FREQUENCY = 486300000
#LORA_GW_DR = "SF11BW125" # DR_1
#LORA_NODE_DR = 1

##Time frequency sampling
TIME_FREQ_SAMPLING = 30
