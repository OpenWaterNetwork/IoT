""" LoPy Node configuration options """

import machine
import ubinascii

# Set  the Gateway ID to be the first 3 bytes of MAC address + 'FFFE' + last 3 bytes of MAC address
# GATEWAY_ID = WIFI_MAC[:6] + "FFFE" + WIFI_MAC[6:12]

WIFI_SSID = '' # 'my-wifi'
WIFI_PASS = '' # my-wifi-password

## for EU868
#LORA_FREQUENCY = 868100000
#LORA_GW_DR = "SF12BW125" # DR_5
#LORA_NODE_DR = 0

## for US915
LORA_FREQUENCY = 904500000
LORA_GW_DR = "SF9BW125" # DR_0
LORA_NODE_DR = 1

# for EU433
#LORA_FREQUENCY = 433375000
#LORA_GW_DR = "SF12BW125" # DR_5
#LORA_NODE_DR = 0

# for CN470
#LORA_FREQUENCY = 486300000
#LORA_GW_DR = "SF11BW125" # DR_5
#LORA_NODE_DR = 1

#Time frequency sampling
TIME_FREQ_SAMPLING = 30
