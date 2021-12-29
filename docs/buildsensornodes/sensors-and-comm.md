# Sensors and communication protocols

River Level Sensor
------------------

### Technical Characteristics

The central processing unit of the equipment is the Lopy4 development board. The most relevant features were taken from [Lopy 4 datasheet](https://docs.pycom.io/datasheets/development/lopy4/#datasheet).

The MB7388 HRXL-MaxSonar-WRMLT sensor is a cost-effective solution for applications that requiere accurate distance detection. The main technical features are taken from [HRXL-MaxSonar- WR Series](https://www.maxbotix.com/documents/HRXL-MaxSonar-WR_Datasheet.pdf).

#### Electrical

- Input voltage: 3.5 - 4.2V
- Output voltage: 3.3V, 1.2 A.
- Max Input sink current - GPIO: 12mA
- Input leakage current: 50nA
- Max Output source current: 12mA

#### CPU
- Xtensa® dual–core 32–bit LX6 microprocessor(s), up to 600 DMIPS
- Hardware floating point acceleration
- Python multi–threading
- An extra ULP–coprocessor that can monitor GPIOs and the ADC channels and it can control most of the internal peripherals during deep–sleep mode while only consuming ~25uA

#### Memory
- RAM: 520KB + 4MB
- External flash: 8MB

#### LoRa

- Frequency Range: 137–1020MHz
- Spreading factor: 6 – 12
- Effective Bitrate: 0.018 – 37.5 kpbs
- Sensitivity: –111 to –148 dBm

#### WiFi
- 802.11b/g/n 16mbps.

#### Bluetooth
- Low energy and classic
- Compliant with Bluetooth v4.2 BR/EDR and BLE
- +12 dBm transmitting power
- Standard HCI based on SDIO/SPI/UART specification

#### GPRS
- Supports command including 3GPP TS 27.007, 27.005 and SIMCOM enhanced AT Commands.
- Working Voltage: 3.5~4.2V
- Quad-band 850/900/1800/1900MHz
- Send and receive GPRS data (TCP/IP, HTTP, etc.)
- Low current consumption - 1mA in sleep mode.

#### Power Supply
- Lithium battery 3.7V 5000mAh. 

#### MB7388 HRXL-MaxSonar-WRMLT Sensor

- Low cost ultrasonic rangefinder.
- Detection out to 10-meters
- Resolution of 1-mm
- Distance sensor 50-cm to 10-meters
- Operating voltage of 2.7V to 5.5V
- Nominal current draw of 2.3mA (peak ~49mA) at 3.3V.

### Hardware component description.

El hardware está integrado en un Placa de Circuito Impreso (PCB), el mismo tiene como componente principal el módulo de desarrollo Lopy4, encargado de realizar las tareas de control, almacenamiento y transmisión. 

Los demás perifericos con los que cuenta el dispositivo (RTC ds3231, FTDI Basic, DHT22 y MB7388 HRXL-MaxSonar-WRMLT sensor) están conectados a la mencionada Unidad Central de Procesamiento (Lopy4). 

Además del PCB mencionado anteriormente, el dispositivo cuenta con una bateria de Litio de 3.7V, para alimentar la placa.

#### Lopy4 connections.

La tarjeta Lopy4 cuenta con 28 pines, entre los cuales están los pines de alimentación y una salida de 3.3V, la disposición de los mismos podemos observar en la figura a continuación. También se detalla la conexión de pines con los perifericos.

|![fig:Lopy4pinConnections](img/Lopy4SCHRLS.PNG)|
|-----------|
|Lopy4 pin connections.|

- P0: Rx P1: Tx. Comunicación UART con el FTDI Basic.
- P2: Pin de Arranque, para actualizar el firmware.
- P3: Tx P4: Rx. Comunicación UART con el SIM 800L.
- P8: Pin de Arranque para el SIM 800L.
- P9: SDA P10: SDL. Comunicación I2C con el RTC ds3231.
- P11: Pulse Width Output Sensor.
- P12: Pin 4- Ranging Start/Stop Sensor.
- P20: Pin de control de modo de funcionamieto.
- P21: Pin de control de fuente de los sensores.
- P22: Pin de lectura del nivel de tensión de Batería.
- P23: Pin de lectura de señal del sensor DHT22. 

#### DHT22
El sensor de temperatura y humedad interno, está conectado a un pin digital del MCU, configurado como entrada, también se conecta una resistencia de pull up a la salida de la señal, ver la siguiente figura.

|![fig:DHT22pinconnections](img/dht22SCH.PNG)|
|-----------|
|DHT22 pin connections.|

#### FTDI BAsic

El módulo se conecta al MCU a través del protocolo UART y comparte la misma referencia de GND.

#### RTC Ds3231

Esté periferico se conecta al MCU a través del protocolo I2C, se utilizan dos resistencia de pull up en los pines de comunicación (ver la figura a continuación), además cuenta con una pila pequeña que lo alimenta en caso de corte de energía.

|![fig:DS3231PinCon](img/ds3231SCH.PNG)|
|-----------|
|RTC DS3231 pin connections|


## Create a docs version

Release a version 1.0 of your project:

```bash
npm run docusaurus docs:version 1.0
```

The `docs` folder is copied into `versioned_docs/version-1.0` and `versions.json` is created.

Your docs now has 2 versions:

- `1.0` at `http://localhost:3000/docs/` for the version 1.0 docs
- `current` at `http://localhost:3000/docs/next/` for the **upcoming, unreleased docs**

## Add a Version Dropdown

To navigate smoothly across versions, add a version dropdown.

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

## Update an existing version

It is possible to edit versioned docs in their own folder:

- `versioned_docs/version-1.0/hello.md` updates `http://localhost:3000/docs/hello`
- `docs/hello.md` updates `http://localhost:3000/docs/next/hello`
