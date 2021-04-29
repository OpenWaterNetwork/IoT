---
sidebar_position: 1
---

# Gateway

En este documento por una parte, se describe las caracteristicas técnicas de hardware, así como también se detalla los componentes del dispositivo. Por otra parte, se indican los metodos de programación y los comandos de configuración del dispositivo concentrador de datos meteorológicos (Iot-LoRa-Gateway). Cabe mencionar que el producto es compatible con dispositivos que cuenten con comunicación LoRa.

## Technical Characteristics

La unidad central de procesamiento del equipo es la tarjeta de desarrollo Lopy4, las caracteristicas de mayor relevancia fueron tomadas
de [Lopy 4 datasheet!](https://docs.pycom.io/datasheets/development/lopy4/#datasheet).

### Electrical

-   Input voltage: 3.5 - 4.2V
-   Output voltage: 3,3V, 1.2 A.
-   Max Input sink curren - GPIO: 12mA
-   Input leakage current: 50nA
-   Max Output source current: 12mA

### CPU

-   Xtensa® dual–core 32–bit LX6 microprocessor(s), up to 600 DMIPS
-   Hardware floating point acceleration
-   Python multi–threading
-   An extra ULP–coprocessor that can monitor GPIOs, the ADC channels
    and control most of the internal peripherals during deep–sleep mode
    while only consuming  25uA

### Memory

-   RAM: 520KB + 4MB
-   External flash: 8MB

### LoRa

-   Frequency Range: 137–1020MHz
-   Spreading factor: 6 – 12
-   Effective Bitrate: 0.018 – 37.5 kpbs
-   Sensitivity: –111 to –148 dBm

### WiFi

-   802.11b/g/n 16mbps.

### Bluetooth

-   Low energy and classic
-   Compliant with Bluetooth v4.2 BR/EDR and BLE
-   +12 dBm transmitting power
-   Standard HCI based on SDIO/SPI/UART specification

### GPRS

-   supports command including 3GPP TS 27.007, 27.005 and SIMCOM
    enhanced AT Commands.
-   Working Voltage: 3.5 4.2V
-   Quad-band 850/900/1800/1900MHz
-   Send and receive GPRS data (TCP/IP, HTTP, etc.)
-   low current consumption - 1mA in sleep mode.

### Power Supply

-   Lithium battery 3.7V 6000mAh.
-   MPPT charge controller for 3.7V lithium batteries.
-   Solar Panel 6V.

## Hardware component description.

El hardware está integrado en un Placa de Circuito Impreso (PCB), el mismo tiene como componente principal el módulo de desarrollo Lopy4, encargado de realizar las tareas de control, almacenamiento y transmisión. Los demás perifericos con los que cuenta el dispositivo (RTC ds3231, FTDI Basic, DHT22 y GPRS SIM800L) están conectados a la mencionada Unidad Central de Procesamiento (Lopy4).

Además del PCB mencionado anteriormente, el dispositivo cuenta con una bateria de Litio, un controlador de carga MPPT y un panel solar de 6V.

| ![](img/GatewayArchGen.png) |
|:--:| 
| *IoT LoRa Gateway Architecture* |

### Lopy4 connections

La tarjeta Lopy4 cuenta con 28 pines, entre los cuales están los pines de alimentación y una salida de 3.3V, la disposición de los mismos y su conexion con los distintos periféricos se detallana a continuación:

-   P0: Rx P1: Tx. Comunicación UART con el FTDI Basic.
-   P2: Pin de Arranque, para actualizar el firmware.
-   P3: Tx P4: Rx. Comunicación UART con el SIM 800L.
-   P8: Pin de Arranque para el SIM 800L.
-   P9: SDA P10: SDL. Comunicación I2C con el RTC ds3231.
-   P21: Pin de control de modo de funcionamieto.
-   P22: Pin de lectura del nivel de tensión de Batería.
-   P23: Pin de lectura de señal del sensor DHT22.

| ![](img/img/Lopy4SCH.PNG) |
|:--:| 
| *Lopy4 pin connections.* |

### Peripheral Connections

### DHT22

El sensor de temperatura y humedad interno, está conectado a un pin digital del MCU, configurado como entrada, también se conecta una resistencia de pull up a la salida de la señal, como en la siguiente figura:


![DHT22 pin connections.](img/dht22SCH.PNG "fig:")

### GPRS SIM800L

Este periferico utiliza el protocolo UART para conectarse al MCU y un pin digital para el control de arranque del mismo, como podemos observar en la figura a continuación. Está alimentado desde la batería de litio (3.7V - 4.2V).

![GPRS Sim800L pin connections.](img/Sim800LSCH.PNG "fig:")

### FTDI Basic

El módulo se conecta al MCU a través del protocolo UART y comparte la misma referencia de GND.

### RTC DS3231

Este periferico se conecta al MCU a través del protocolo I2C, se utilizan dos resistencia de pull up en los pines de comunicación (ver figura [fig:DS3231PinCon] ), además cuenta con una pila pequeña que lo alimenta en caso de corte de energía.

![RTC DS3231 pin connections.](img/ds3231SCH.PNG "fig:")

# Installation and Start-up

This section introduces the start-up of the device, gives a brief description of the software to be used and describes the commands required for configuration. A continuación se muestra una vita 3D del dispositivo LoRa Gateway IoT y un detalle de con cada uno de sus componetes:

-   U1: GPRS module SIM 800L
-   U2: Lopy 4
-   U3: RTC DS3231
-   J1: Temperature and humidity sensor DHT22
-   P1: Power In connector
-   H1: Jumper conector - boot mode selector.
-   H2: usb to serial converter.
-   S1: Operating mode selector button

![IoT LoRa Gateway Device](img/gateway_3d.PNG "fig:") 

## Start-up

Para comenzar la configuración del Gateway, es necesario descargar el software para gestión y programación según lo indicado en la pagina de [Documentos de Pycom Lopy4](https://docs.pycom.io/gettingstarted/software/). Se puede trabajar con las 2 opciones tanto el software “ATOM” como también “Visual Studio Code”.

En caso de usar Windows es necesario descargar los drivers del conversor Usb-serial desde la página de [FTDI Chip -VCP](https://ftdichip.com/drivers/vcp-drivers/) , de esta manera se tiene el puerto COM correspondiente.

Una vez se han instalado los componentes de software, conecte la placa a la alimentación a travéz de P1 y a una PC con un cable micro USB para uso de datos, a travéz de P2.

La placa tiene un led que indica el arranque normal de la placa y el modo en que se encuentra funcionando. La secuencia inicia con el led de color verde encendido por 3 segundos, lo que quiere decir que la placa entra en modo de espera (Modo de configuración).

![USB connection.](img/usbConnect.PNG "fig:") 

Ahora es necesario abrir el entorno de programación, para agregar el dispositivo COM y configuar el dispositivo gateway. A continuación se detallan los pasos a seguir:

-   Open Pymakr.

    ![Pymakr package opened.](img/openCOM_1.png "fig:") 

-   Open Global Settings.

    ![Open Global Settings.](img/openCOM_2.png "fig:")
    
-   Set the corresponding COM port, verify from the device manager.

    ![Set COM port.](img/openCOM_3.png "fig:") 
    
-   Open COM port from Connected Devices.

    ![Open COM port.](img/openCOM_4.png "fig:") 
    
    ![Console ready for configuration.](img/openCOM_5.png "fig:") 

Configuration Methods
---------------------

### System Operation

Como se mencionó en el apartado anterior, el led verde encendido por 3 segundos luego de conectar la placa, indica que está lsita la configuración. Para empezar el funcionamiento automatico del sistema se debe crear un archivo de configuración con el método detallado a continuación.

The system automatically resets and the next process begins:

-   Time and date synchronization.
-   Alarm initiation for packet transmission.
-   Send synchronization packet to the nodes.
-   Deep sleep mode until the data packet is sent back to the server,

When the sending time is reached, the system performs the following repetitive process:
-   Time and date synchronization.
-   Alarm initiation for packet transmission.
-   Send channel assignment packet.
-   Send data to the server.
-   Deep sleep mode until the data packet is sent back to the server,

```python:
configFile(stationNum, idStation, Url, NTPServer, frequencyTx)
```
-   stationNum: Number of nodes to be connected to the Gateway.
-   idStation: Gateway ID (240 - 255).
-   Url: Url for transmitting packets via http get.
-   NTPServer: NTP server IP.
-   frequencyTx: Packet Transmission Frequency in minutes.
-   Example: configFile(3, 250,
    “http://api.thingspeak.com/update?api\_key=XXXX&field1=”,“162.159.200.1”,
    5)

### GPRS SIM800L mobile connection

To configure the device, the first thing to consider is the time synchronization via Network time protocol (NTP) and the GPRS SIM 800L

The following are the methods for synchronization with the GPRS SIM 800L module.

```python:
sim800L.signalLevel(None)
```
-   Response: +CSQ: rssi, ber
    -   rssi
        -   0: -115 dBm or less
        -   1: -111 dBm
        -   2...30: -110... -54 dBm
        -   31: -52 dBm or greater
        -   99: not known or not detectable
    -   ber (in percent):
        -   0...7 As RXQUAL values in the table in GSM 05.08
        -   99 Not known or not detectable

```python:
sim800L.GPRS\_init(None)
```

-   Response: +SAPBR: cid, Status, IP\_Addr
    -   cid : Bearer profile identifier
    -   Status
        -   0 Bearer is connecting
        -   1 Bearer is connected
        -   2 Bearer is closing
        -   3 Bearer is closed
    -   IP\_Addr: IP address

```python:
sim800L.GPRS\_NTP(None)
```

-   Response: +SAPBR: cid, Status, IP\_Addr
    -   cid : Bearer profile identifier
    -   Status
        -   0 Bearer is connecting
        -   1 Bearer is connected
        -   2 Bearer is closing
        -   3 Bearer is closed
    -   IP\_Addr: IP address
-   Response: (year, day, month, hour, minute, second, millisecond,
    None)

### Real time clock (RTC) ds3231

The external real time clock (RTC) ds3231 is the one that will keep the
system synchronized in time and date, because it has an independent
battery. The methods for synchronization are presented below.


```python:
ds3231.ds1307init\_sinc(None)
```

-   Synchronizes the external real-time clock (ds3231) with the internal
    time (lopy 4).
-   Response: (year, day, month, hour, minute, second, millisecond,
    None)

```python:
get\_time\_ds3231(None)
```

-   Obtains the date and time from the external real-time clock
    (ds3231).
-   Response: (year, day, month, hour, minute, second, millisecond,
    None)

```python:
ds3231.sinc\_RTC\_from\_ds3231(None)
```
-   Synchronizes the internal clock (lopy 4) with the time of the
    external real-time clock (ds3231).
-   Response: (year, day, month, hour, minute, second, millisecond,
    None)

### Temperature and humidity sensor DHT11

The sensor reading is done by the following method:
```python:
result = th.read(None)
```

-   Response: result.temperature
-   Response: result.humidity

## Functionality and cost

Release a version 1.0 of your project:

```bash
npm run docusaurus docs:version 1.0
```

The `docs` folder is copied into `versioned_docs/version-1.0` and `versions.json` is created.

Your docs now have 2 versions:

- `1.0` at `http://localhost:3000/docs/` for the version 1.0 docs
- `current` at `http://localhost:3000/docs/next/` for the **upcoming, unreleased docs**

## Hardware (all the details needed to make it)

To navigate seamlessly across versions, add a version dropdown.

Modify the `docusaurus.config.js` file:

```js title="docusaurus.config.js"
module.exports = {
  themeConfig: {
    navbar: {
      items: [
        // highlight-start
        {
          type: 'docsVersionDropdown',
        },
        // highlight-end
      ],
    },
  },
};
```

The docs version dropdown appears in your navbar:

![Docs Version Dropdown](/img/tutorial/docsVersionDropdown.png)

## Scripts (the full scripts with some explanation)
Los scripts con los que cuenta el sistema se encuentran divididos en archivos .py que contienen las calses y los métodos para el correcto funcionamiento del sistema. Se encuentran divididos en los siguientes archivos:

### Boot.py

El primer archivo es el llamado boot.py, es el que arranca el sistema y en el se define:

- La comunicación serial para la consola de visualización y para subir los programas.
- Se desabilita el módulo WIFI para reducir el consumo energético.
- Se define el programa que arrancará a continuación de estás configuraciones.

```python:
import machine
import os
from machine import UART
from network import WLAN
from network import Server

###-- Uart for console communication.

uart = UART(0, baudrate=115200)
os.dupterm(uart)

###-- Disable WIFI.

wlan = WLAN(mode=WLAN.STA)
wlan.init(mode=WLAN.AP, ssid='gateway-station', auth=(WLAN.WPA2,'gateway-station'), channel=7, antenna=WLAN.INT_ANT)
wlan.deinit()

###-- File to be run first.

machine.main('main.py')

```
### sim800L.py

```python:
import time
import pycom
import os
from machine import RTC
from machine import Timer
from machine import UART

class SIM800L():
    
    def __init__(self):
        self.__ser_gprs = UART(1, baudrate=9600)
        self.__rtc = RTC()
        time.sleep(1.0)

####--- Method of reading the GPRS response to AT commands.

    def readGPRSdata(self):

        time.sleep(0.2)
        readData = False
        scape = False
        datos_gprs=True
        gprsdataread=''
        chrono = Timer.Chrono()
        chrono.start()

        while (datos_gprs == True):
            time.sleep(0.2)
            timeWait=chrono.read()

            if(self.__ser_gprs.any() > 0):
                gprsdataread= gprsdataread + str(self.__ser_gprs.readall())
                readData = True
                scape = False
                chrono.reset()
            elif readData == True:
                if scape == False:
                    scape = True
                    continue
            if(timeWait > 40 or scape == True):
                datos_gprs=False

        chrono.stop()
        chrono.reset()
        #print(gprsdataread, len(gprsdataread))

        return gprsdataread

###--- Method to check the GPRS band and configuration in "GSM850_MODE" mode.

    def bandGPRS(self):
        self.__ser_gprs.write("AT+CBAND?")
        self.__ser_gprs.write("\r\n")
        self.readGPRSdata()
        self.__ser_gprs.write("AT+CBAND=\"GSM850_MODE\"")
        self.__ser_gprs.write("\r\n")
        self.readGPRSdata()

###--- Verify GPRS signal.

    def signalLevel(self):
        self.__ser_gprs.write("AT+CSQ")
        self.__ser_gprs.write("\r\n")
        dataRead = self.readGPRSdata()

        arraydataread=str(dataRead).split("\\r\\n")
        print(arraydataread[1])
        comp=":0,0" in arraydataread[1]

        if (comp==True or arraydataread[1]=="ERROR"):
            return False

        return True

###-- Connect to the Internet to initiate communication.

    def GPRS_init(self):

        contRetrans = 0
        float_retransmit=True

        try:

            self.__ser_gprs.write("AT+SAPBR=0,1\r\n")
            time.sleep(2)
            self.readGPRSdata()

            self.__ser_gprs.write("AT+SAPBR=3,1,\"APN\",\"internet.claro.com.ec\"\r\n")
            self.readGPRSdata()

            self.__ser_gprs.write("AT+SAPBR=1,1\r\n")
            time.sleep(2)
            gprsdataread = self.readGPRSdata()

            self.__ser_gprs.write("AT+SAPBR=2,1\r\n")
            dataRead = self.readGPRSdata()

            arraydataread=str(dataRead).split("\\r\\n")
            print(arraydataread[1])
            comp="0.0.0.0" in arraydataread[1]

            if comp==True or arraydataread[1]=="ERROR":
                float_retransmit=False

        except Exception as e:
            print("Error network connecting")
            float_retransmit=False

        time.sleep(1)

        return float_retransmit

###-- Connect to the NTP server and match system time.

    def GPRS_NTP(self):
        float_retransmit=True
        try:
            self.__ser_gprs.write("AT+SAPBR=0,1\r\n")
            time.sleep(2)
            self.readGPRSdata()
            contRetrans = 0
            self.__ser_gprs.write("AT")
            self.__ser_gprs.write("\r\n")
            self.readGPRSdata()
            self.__ser_gprs.write("AT+CSQ")
            self.__ser_gprs.write("\r\n")
            self.readGPRSdata()
            self.__ser_gprs.write("AT+SAPBR=3,1,\"Contype\",\"GPRS\"\r\n")
            self.readGPRSdata()
            self.__ser_gprs.write("AT+SAPBR=3,1,\"APN\",\"internet.claro.com.ec\"\r\n")
            self.readGPRSdata()
            self.__ser_gprs.write("AT+SAPBR=1,1"+"\r\n")
            time.sleep(3)
            self.readGPRSdata()
            self.__ser_gprs.write("AT+SAPBR=2,1"+"\r\n")
            dataRead = self.readGPRSdata()
            arraydataread=str(dataRead).split("\\r\\n")
            print(arraydataread[1])
            
            comp="0.0.0.0" in arraydataread[1]
            if comp==True or arraydataread[1]=="ERROR":
                float_retransmit=False
            if float_retransmit==True:
                self.__ser_gprs.write("AT+CNTPCID=1"+"\r\n")
                self.readGPRSdata()
                self.__ser_gprs.write("AT+CNTP=\"162.159.200.1\",-20"+"\r\n")   ###-- Ip NTP server
                self.readGPRSdata()
                self.__ser_gprs.write("AT+CNTP"+"\r\n")
                self.readGPRSdata()
                #self.readGPRSdata()
                self.__ser_gprs.write("AT+CCLK?"+"\r\n")
                gprsdataread = self.readGPRSdata()
                NMEA1 = str(gprsdataread)
                #print(NMEA1)
                NMEA1_array = NMEA1.split("\\r\\n")
                #print(NMEA1_array)
                
                if(len(NMEA1_array)>2 and len(NMEA1_array[1].split(","))==2):
                    datos_fecha_hora= NMEA1_array[1].split(",")
                    #print(datos_fecha_hora[0])
                    seg_gprs=int(datos_fecha_hora[1][6:8])
                    min_gprs=int(datos_fecha_hora[1][3:5])
                    hora_gprs=int(datos_fecha_hora[1][0:2])
                    dia_gprs=int(datos_fecha_hora[0][14:16])
                    mes_gprs=int(datos_fecha_hora[0][11:13])
                    age_gprs=int(datos_fecha_hora[0][8:10])+2000
                    #print(hora_gprs,min_gprs,seg_gprs,dia_gprs,mes_gprs,age_gprs)
                    self.__rtc.init((age_gprs, mes_gprs, dia_gprs, hora_gprs, min_gprs, seg_gprs, 0, 0),source=RTC.INTERNAL_RC) #COnfig Clock
                    epoch_time=time.time()
                    tuple_time = time.gmtime(epoch_time+8)
                    self.__rtc.init(tuple_time)
                    print(self.__rtc.now())
                    pycom.heartbeat(False)
                    pycom.rgbled(0x007f00)
                    time.sleep(0.25)
                    pycom.heartbeat(False)
                    time.sleep(0.25)
                    pycom.rgbled(0x007f00)
                    time.sleep(0.25)
                    pycom.heartbeat(False)
                    time.sleep(1)
            else:
                print("THE TIME CANNOT BE SYNCHRONIZED")
                pycom.heartbeat(False)
                pycom.rgbled(0x7f0000)
                time.sleep(0.25)
                pycom.heartbeat(False)
                time.sleep(0.25)
                pycom.rgbled(0x7f0000)
                time.sleep(0.25)
                pycom.heartbeat(False)
                time.sleep(2)

        except Exception as e:

            print("Error NTP server connecting")
            float_retransmit=False
            
        self.__ser_gprs.write("AT+SAPBR=0,1\r\n")
        time.sleep(2)
        self.readGPRSdata()
        time.sleep(1)

        return float_retransmit

###-- Sending data to the server provided, via HTTP get.

    def send_GPRS(self,url_trasm):

        contRetrans = 0
        maxRetrans = 5
        float_retransmit=True
        gprsdataread=''
        flagTrans1=False

        self.__ser_gprs.write("AT+HTTPTERM")
        self.__ser_gprs.write("\r\n")
        self.readGPRSdata()
        self.__ser_gprs.write("AT+HTTPINIT")
        self.__ser_gprs.write("\r\n")
        self.readGPRSdata()
        self.__ser_gprs.write("AT+HTTPPARA=\"CID\",1\r\n")
        self.readGPRSdata()
        self.__ser_gprs.write("AT+HTTPPARA=\"URL\"," +"\""+url_trasm+"\""+"\r\n")
        self.readGPRSdata()
        self.__ser_gprs.write("AT+HTTPACTION=0\r\n")
        self.readGPRSdata()
        time.sleep(2)
        gprsdataread=self.readGPRSdata()

        print(gprsdataread)

        if (str(gprsdataread).find("HTTPACTION: 0,200")==-1):
            print("Send Failed ")
            flagTrans1=False

        if (str(gprsdataread).find("HTTPACTION: 0,200") >= 0):
            print("Send OK")
            flagTrans1=True

        self.__ser_gprs.write("AT+HTTPTERM\r\n")
        self.readGPRSdata()

        self.__ser_gprs.write("AT+SAPBR=0,1\r\n")
        time.sleep(2)
        self.readGPRSdata()

        return flagTrans1

###-- GPRS in sleep mode to reduce power consumption.

    def GPRS_sleep(self):
        self.__ser_gprs.write("AT+CSCLK=1\r\n")
        gprsdataread=self.readGPRSdata()
        time.sleep(2)

 ```

It is possible to edit versioned docs in their respective folder:

- `versioned_docs/version-1.0/hello.md` updates `http://localhost:3000/docs/hello`
- `docs/hello.md` updates `http://localhost:3000/docs/next/hello`
