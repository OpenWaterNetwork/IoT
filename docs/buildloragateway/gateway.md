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

#################### Uart for console communication ############################
################################################################################

uart = UART(0, baudrate=115200)
os.dupterm(uart)

#########################  Disable WIFI ########################################
################################################################################

wlan = WLAN(mode=WLAN.STA)
wlan.init(mode=WLAN.AP, ssid='gateway-station', auth=(WLAN.WPA2,'gateway-station'), channel=7, antenna=WLAN.INT_ANT)
wlan.deinit()

####################### File to be run first ###################################
################################################################################
machine.main('main.py')

```

It is possible to edit versioned docs in their respective folder:

- `versioned_docs/version-1.0/hello.md` updates `http://localhost:3000/docs/hello`
- `docs/hello.md` updates `http://localhost:3000/docs/next/hello`
