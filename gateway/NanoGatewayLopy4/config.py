""" LoPy LoRaWAN Nano Gateway configuration options """

import machine
import ubinascii

WIFI_MAC = ubinascii.hexlify(machine.unique_id()).upper()
# Set  the Gateway ID to be the first 3 bytes of MAC address + 'FFFE' + last 3 bytes of MAC address
GATEWAY_ID = WIFI_MAC[:6] + "FFFE" + WIFI_MAC[6:12]

SERVER = 'router.eu.thethings.network'
PORT = 1700

NTP = "pool.ntp.org"
NTP_PERIOD_S = 3600

WIFI_SSID = 'HUAWEI_P9_9ED4' # 'my-wifi'
WIFI_PASS = 'my_password' # my-wifi-password
# WIFI_SSID = 'AndroidAP Jan' # 'my-wifi'
# WIFI_PASS = 'oocx1748' # my-wifi-password
# WIFI_SSID = 'Crest Safari Lodge Garden' # 'my-wifi'
# WIFI_PASS = 'welcome@crest'
# my-wifi-password# IMPORTANT: In case of a firewall UDP port 1700 needs to be opened

# for EU868
LORA_FREQUENCY = 868100000
LORA_GW_DR = "SF7BW125" # DR_5
LORA_NODE_DR = 5

# for US915
# LORA_FREQUENCY = 903900000
# LORA_GW_DR = "SF10BW125" # DR_0
# LORA_NODE_DR = 0
