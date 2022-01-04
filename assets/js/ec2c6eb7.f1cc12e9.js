(window.webpackJsonp=window.webpackJsonp||[]).push([[43],{112:function(e,t,a){"use strict";a.r(t),a.d(t,"frontMatter",(function(){return o})),a.d(t,"metadata",(function(){return i})),a.d(t,"toc",(function(){return c})),a.d(t,"default",(function(){return b}));var n=a(3),r=a(7),l=(a(0),a(121)),o={},i={unversionedId:"buildsensornodes/sensors-and-comm",id:"buildsensornodes/sensors-and-comm",isDocsHomePage:!1,title:"Sensors and communication protocols",description:"Technical Characteristics",source:"@site/docs/buildsensornodes/sensors-and-comm.md",sourceDirName:"buildsensornodes",slug:"/buildsensornodes/sensors-and-comm",permalink:"/IoT/docs/buildsensornodes/sensors-and-comm",editUrl:"https://github.com/OpenWaterNetwork/IoT/blob/documentation/docs/buildsensornodes/sensors-and-comm.md",version:"current",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Sensor node registration on TTN",permalink:"/IoT/docs/buildsensornodes/wseb"},next:{title:"Topic 1",permalink:"/IoT/docs/thingsboardiotplaftorm/topic1"}},c=[{value:"Electrical",id:"electrical",children:[]},{value:"CPU",id:"cpu",children:[]},{value:"Memory",id:"memory",children:[]},{value:"LoRa",id:"lora",children:[]},{value:"WiFi",id:"wifi",children:[]},{value:"Bluetooth",id:"bluetooth",children:[]},{value:"GPRS",id:"gprs",children:[]},{value:"Power Supply",id:"power-supply",children:[]},{value:"MB7388 HRXL-MaxSonar-WRMLT Sensor",id:"mb7388-hrxl-maxsonar-wrmlt-sensor",children:[]},{value:"Hardware component description.",id:"hardware-component-description",children:[{value:"River Level Sensor",id:"river-level-sensor",children:[]}]},{value:"Start-up",id:"start-up",children:[{value:"Mododos de funcionamiento.",id:"mododos-de-funcionamiento",children:[]},{value:"Run mode - Active console.",id:"run-mode---active-console",children:[]},{value:"Run mode - Inactive console,",id:"run-mode---inactive-console",children:[]}]},{value:"M\xe9todos de configuraci\xf3n.",id:"m\xe9todos-de-configuraci\xf3n",children:[{value:"Real time clock (RTC) ds3231",id:"real-time-clock-rtc-ds3231",children:[]},{value:"Temperature and humidity sensor DHT11",id:"temperature-and-humidity-sensor-dht11",children:[]},{value:"MB7388 HRXL sensor DHT11",id:"mb7388-hrxl-sensor-dht11",children:[]},{value:"LoRaWan",id:"lorawan",children:[]}]},{value:"Create a docs version",id:"create-a-docs-version",children:[]},{value:"Add a Version Dropdown",id:"add-a-version-dropdown",children:[]},{value:"Update an existing version",id:"update-an-existing-version",children:[]}],s={toc:c};function b(e){var t=e.components,o=Object(r.a)(e,["components"]);return Object(l.b)("wrapper",Object(n.a)({},s,o,{components:t,mdxType:"MDXLayout"}),Object(l.b)("p",null,"Technical Characteristics"),Object(l.b)("p",null,"The central processing unit of the equipment is the Lopy4 development board. The most relevant features were taken from ",Object(l.b)("a",{parentName:"p",href:"https://docs.pycom.io/datasheets/development/lopy4/#datasheet"},"Lopy 4 datasheet"),"."),Object(l.b)("h3",{id:"electrical"},"Electrical"),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},"Input voltage: 3.5 - 4.2V"),Object(l.b)("li",{parentName:"ul"},"Output voltage: 3.3V, 1.2 A."),Object(l.b)("li",{parentName:"ul"},"Max Input sink current - GPIO: 12mA"),Object(l.b)("li",{parentName:"ul"},"Input leakage current: 50nA"),Object(l.b)("li",{parentName:"ul"},"Max Output source current: 12mA")),Object(l.b)("h3",{id:"cpu"},"CPU"),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},"Xtensa\xae dual\u2013core 32\u2013bit LX6 microprocessor(s), up to 600 DMIPS"),Object(l.b)("li",{parentName:"ul"},"Hardware floating point acceleration"),Object(l.b)("li",{parentName:"ul"},"Python multi\u2013threading"),Object(l.b)("li",{parentName:"ul"},"An extra ULP\u2013coprocessor that can monitor GPIOs and the ADC channels and it can control most of the internal peripherals during deep\u2013sleep mode while only consuming ~25uA")),Object(l.b)("h3",{id:"memory"},"Memory"),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},"RAM: 520KB + 4MB"),Object(l.b)("li",{parentName:"ul"},"External flash: 8MB")),Object(l.b)("h3",{id:"lora"},"LoRa"),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},"Frequency Range: 137\u20131020MHz"),Object(l.b)("li",{parentName:"ul"},"Spreading factor: 6 \u2013 12"),Object(l.b)("li",{parentName:"ul"},"Effective Bitrate: 0.018 \u2013 37.5 kpbs"),Object(l.b)("li",{parentName:"ul"},"Sensitivity: \u2013111 to \u2013148 dBm")),Object(l.b)("h3",{id:"wifi"},"WiFi"),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},"802.11b/g/n 16mbps.")),Object(l.b)("h3",{id:"bluetooth"},"Bluetooth"),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},"Low energy and classic"),Object(l.b)("li",{parentName:"ul"},"Compliant with Bluetooth v4.2 BR/EDR and BLE"),Object(l.b)("li",{parentName:"ul"},"+12 dBm transmitting power"),Object(l.b)("li",{parentName:"ul"},"Standard HCI based on SDIO/SPI/UART specification")),Object(l.b)("h3",{id:"gprs"},"GPRS"),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},"Supports command including 3GPP TS 27.007, 27.005 and SIMCOM enhanced AT Commands."),Object(l.b)("li",{parentName:"ul"},"Working Voltage: 3.5~4.2V"),Object(l.b)("li",{parentName:"ul"},"Quad-band 850/900/1800/1900MHz"),Object(l.b)("li",{parentName:"ul"},"Send and receive GPRS data (TCP/IP, HTTP, etc.)"),Object(l.b)("li",{parentName:"ul"},"Low current consumption - 1mA in sleep mode.")),Object(l.b)("h3",{id:"power-supply"},"Power Supply"),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},"Lithium battery 3.7V 5000mAh. ")),Object(l.b)("h3",{id:"mb7388-hrxl-maxsonar-wrmlt-sensor"},"MB7388 HRXL-MaxSonar-WRMLT Sensor"),Object(l.b)("p",null,"The MB7388 HRXL-MaxSonar-WRMLT sensor is a cost-effective solution for applications that requiere accurate distance detection. The main technical features are taken from ",Object(l.b)("a",{parentName:"p",href:"https://www.maxbotix.com/documents/HRXL-MaxSonar-WR_Datasheet.pdf"},"HRXL-MaxSonar- WR Series"),"."),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},"Low cost ultrasonic rangefinder."),Object(l.b)("li",{parentName:"ul"},"Detection out to 10-meters"),Object(l.b)("li",{parentName:"ul"},"Resolution of 1-mm"),Object(l.b)("li",{parentName:"ul"},"Distance sensor 50-cm to 10-meters"),Object(l.b)("li",{parentName:"ul"},"Operating voltage of 2.7V to 5.5V"),Object(l.b)("li",{parentName:"ul"},"Nominal current draw of 2.3mA (peak ~49mA) at 3.3V.")),Object(l.b)("h2",{id:"hardware-component-description"},"Hardware component description."),Object(l.b)("h3",{id:"river-level-sensor"},"River Level Sensor"),Object(l.b)("p",null,"El hardware est\xe1 integrado en un Placa de Circuito Impreso (PCB), el mismo tiene como componente principal el m\xf3dulo de desarrollo Lopy4, encargado de realizar las tareas de control, almacenamiento y transmisi\xf3n. "),Object(l.b)("p",null,"Los dem\xe1s perifericos con los que cuenta el dispositivo (RTC ds3231, FTDI Basic, DHT22 y MB7388 HRXL-MaxSonar-WRMLT sensor) est\xe1n conectados a la mencionada Unidad Central de Procesamiento (Lopy4). "),Object(l.b)("p",null,"Adem\xe1s del PCB mencionado anteriormente, el dispositivo cuenta con una bateria de Litio de 3.7V, para alimentar la placa."),Object(l.b)("h4",{id:"lopy4-connections"},"Lopy4 connections."),Object(l.b)("p",null,"La tarjeta Lopy4 cuenta con 28 pines, entre los cuales est\xe1n los pines de alimentaci\xf3n y una salida de 3.3V, la disposici\xf3n de los mismos podemos observar en la figura a continuaci\xf3n. Tambi\xe9n se detalla la conexi\xf3n de pines con los perifericos."),Object(l.b)("table",null,Object(l.b)("thead",{parentName:"table"},Object(l.b)("tr",{parentName:"thead"},Object(l.b)("th",{parentName:"tr",align:null},Object(l.b)("img",{alt:"fig:Lopy4pinConnections",src:a(184).default})))),Object(l.b)("tbody",{parentName:"table"},Object(l.b)("tr",{parentName:"tbody"},Object(l.b)("td",{parentName:"tr",align:null},"Lopy4 pin connections.")))),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},"P0: Rx P1: Tx. Comunicaci\xf3n UART con el FTDI Basic."),Object(l.b)("li",{parentName:"ul"},"P2: Pin de Arranque, para actualizar el firmware."),Object(l.b)("li",{parentName:"ul"},"P3: Tx P4: Rx. Comunicaci\xf3n UART con el SIM 800L."),Object(l.b)("li",{parentName:"ul"},"P8: Pin de Arranque para el SIM 800L."),Object(l.b)("li",{parentName:"ul"},"P9: SDA P10: SDL. Comunicaci\xf3n I2C con el RTC ds3231."),Object(l.b)("li",{parentName:"ul"},"P11: Pulse Width Output Sensor."),Object(l.b)("li",{parentName:"ul"},"P12: Pin 4- Ranging Start/Stop Sensor."),Object(l.b)("li",{parentName:"ul"},"P20: Pin de control de modo de funcionamieto."),Object(l.b)("li",{parentName:"ul"},"P21: Pin de control de fuente de los sensores."),Object(l.b)("li",{parentName:"ul"},"P22: Pin de lectura del nivel de tensi\xf3n de Bater\xeda."),Object(l.b)("li",{parentName:"ul"},"P23: Pin de lectura de se\xf1al del sensor DHT22. ")),Object(l.b)("h4",{id:"dht22"},"DHT22"),Object(l.b)("p",null,"El sensor de temperatura y humedad interno, est\xe1 conectado a un pin digital del MCU, configurado como entrada, tambi\xe9n se conecta una resistencia de pull up a la salida de la se\xf1al, ver la siguiente figura."),Object(l.b)("table",null,Object(l.b)("thead",{parentName:"table"},Object(l.b)("tr",{parentName:"thead"},Object(l.b)("th",{parentName:"tr",align:null},Object(l.b)("img",{alt:"fig:DHT22pinconnections",src:a(185).default})))),Object(l.b)("tbody",{parentName:"table"},Object(l.b)("tr",{parentName:"tbody"},Object(l.b)("td",{parentName:"tr",align:null},"DHT22 pin connections.")))),Object(l.b)("h4",{id:"ftdi-basic"},"FTDI BAsic"),Object(l.b)("p",null,"El m\xf3dulo se conecta al MCU a trav\xe9s del protocolo UART y comparte la misma referencia de GND."),Object(l.b)("h4",{id:"rtc-ds3231"},"RTC Ds3231"),Object(l.b)("p",null,"Est\xe9 periferico se conecta al MCU a trav\xe9s del protocolo I2C, se utilizan dos resistencia de pull up en los pines de comunicaci\xf3n (ver la figura a continuaci\xf3n), adem\xe1s cuenta con una pila peque\xf1a que lo alimenta en caso de corte de energ\xeda."),Object(l.b)("table",null,Object(l.b)("thead",{parentName:"table"},Object(l.b)("tr",{parentName:"thead"},Object(l.b)("th",{parentName:"tr",align:null},Object(l.b)("img",{alt:"fig:DS3231PinCon",src:a(186).default})))),Object(l.b)("tbody",{parentName:"table"},Object(l.b)("tr",{parentName:"tbody"},Object(l.b)("td",{parentName:"tr",align:null},"RTC DS3231 pin connections")))),Object(l.b)("h4",{id:"mb7388-hrxl-maxsonar-wrmlt"},"MB7388 HRXL-MaxSonar-WRMLT"),Object(l.b)("p",null,"El sensor est\xe1 conectado al MCU por intermedio de los puertos GPIO digitales, para realizar la lectura y el control del mismo; utiliza dos conectores de tipo bornera para facilitar su integraci\xf3n en la placa electr\xf3nica."),Object(l.b)("table",null,Object(l.b)("thead",{parentName:"table"},Object(l.b)("tr",{parentName:"thead"},Object(l.b)("th",{parentName:"tr",align:null},Object(l.b)("img",{alt:"fig:BornerPinCon",src:a(187).default})))),Object(l.b)("tbody",{parentName:"table"},Object(l.b)("tr",{parentName:"tbody"},Object(l.b)("td",{parentName:"tr",align:null},"Header for MB7388 sensor pin connections.")))),Object(l.b)("h2",{id:"start-up"},"Start-up"),Object(l.b)("p",null,"En esta secci\xf3n se presenta la puesta en marcha del dispositivo, se describe los comandos necesarios para la configuraci\xf3n. "),Object(l.b)("p",null,"En la siguiente figura se observa una vista 3D del dispositivo IoT LoRa Gateway con cada uno de sus componentes, que se detallan a continuaci\xf3n:"),Object(l.b)("table",null,Object(l.b)("thead",{parentName:"table"},Object(l.b)("tr",{parentName:"thead"},Object(l.b)("th",{parentName:"tr",align:null},Object(l.b)("img",{alt:"fig:RLS_3d",src:a(188).default})))),Object(l.b)("tbody",{parentName:"table"},Object(l.b)("tr",{parentName:"tbody"},Object(l.b)("td",{parentName:"tr",align:null},"IoT LoRa River Level Sensor Datalogger")))),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},"U1: GPRS module SIM800L."),Object(l.b)("li",{parentName:"ul"},"U2: Lopy 4."),Object(l.b)("li",{parentName:"ul"},"U3: RTC DS3231."),Object(l.b)("li",{parentName:"ul"},"J1: Temperature and humidity sensor DHT22."),Object(l.b)("li",{parentName:"ul"},"P1: Power In connector."),Object(l.b)("li",{parentName:"ul"},"H1: Jumper conector - boot mode selector."),Object(l.b)("li",{parentName:"ul"},"H2: usb to serial converter."),Object(l.b)("li",{parentName:"ul"},"S1: Operating mode selector button"),Object(l.b)("li",{parentName:"ul"},"B2: Header - Power sensor."),Object(l.b)("li",{parentName:"ul"},"B1: Header - Signals sensor.")),Object(l.b)("p",null,"Para comenzar la configuraci\xf3n del Gateway, es necesario descargar el software para gesti\xf3n y programaci\xf3n seg\xfan lo indicado en la pagina de ",Object(l.b)("a",{parentName:"p",href:"https://docs.pycom.io/gettingstarted/software/"},"Documentos de Pycom Lopy 4"),'. Se puede trabajar con las 2 opciones tanto el software "ATOM" como tambi\xe9n "Visual Studio Code".'),Object(l.b)("p",null,"En caso de usar Windows es necesario descargar los drivers del conversor Usb-serial desde la p\xe1gina de ",Object(l.b)("a",{parentName:"p",href:"https://ftdichip.com/drivers/vcp-drivers/"},"FTDI Chip - VCP"),", de esta manera se tiene el puerto COM correspondiente."),Object(l.b)("p",null,"Una vez se han instalado los componentes de software, conecte la placa a la alimentaci\xf3n a trav\xe9z de P1 y a una PC con un cable micro USB para uso de datos, a trav\xe9z de P2."),Object(l.b)("p",null,"La placa tiene un led que indica el arranque normal del sistema y el modo en que se encuentra funcionando. La secuencia inicia con el led de color rojo encendido por 1 segundo, lo que quiere decir que la placa entra en modo de espera (Modo de configuraci\xf3n)."),Object(l.b)("table",null,Object(l.b)("thead",{parentName:"table"},Object(l.b)("tr",{parentName:"thead"},Object(l.b)("th",{parentName:"tr",align:null},Object(l.b)("img",{alt:"fig:usbConnect",src:a(189).default})))),Object(l.b)("tbody",{parentName:"table"},Object(l.b)("tr",{parentName:"tbody"},Object(l.b)("td",{parentName:"tr",align:null},"USB connection.")))),Object(l.b)("h3",{id:"mododos-de-funcionamiento"},"Mododos de funcionamiento."),Object(l.b)("p",null,"En el modo de configuraci\xf3n el sistema est\xe1 a la espera de ejecutar alg\xfan comando. Al cargar el software por primera vez, el sistema entrar\xe1 en este modo y se encender\xe1 un LED ROJO como indicador."),Object(l.b)("p",null,"El sistema realiza autom\xe1ticamente el siguiente proceso:"),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},"Env\xeda el paquete de sincronizaci\xf3n por LoRa y espera por a respuesta del Gateway."),Object(l.b)("li",{parentName:"ul"},"Si obtiene la respuesta del gateway, sincroniza el tiempo del RTC DS3231."),Object(l.b)("li",{parentName:"ul"},"Si no obtiene respuesta del gateway, obtiene el tiempo del RTC DS3231."),Object(l.b)("li",{parentName:"ul"},"Espera la ejecuci\xf3n del comando.")),Object(l.b)("p",null,"Para configurar primero debemos ejecutar el siguiente comando, este se encarga de sincronizar la hora del dispositivo (NODO) con la del GAteway y actualizarla en el RTC DS3231."),Object(l.b)("pre",null,Object(l.b)("code",{parentName:"pre",className:"language-python:"},"SincNodefromGateway()\n")),Object(l.b)("p",null,"El dispositivo debe permanecer en este modo de funcionamiento para sincronizar la hora y la fecha del nodo. Una vez sincronizado, se puede enviar los paquetes por lorawan, ejecutando los siguientes comandos:"),Object(l.b)("pre",null,Object(l.b)("code",{parentName:"pre",className:"language-python:"},"joinLoraWan()\ndataSendLoraWan()\n")),Object(l.b)("p",null,"Para entrar en el modo de ejecuci\xf3n, se ejecuta el siguiente comando. "),Object(l.b)("pre",null,Object(l.b)("code",{parentName:"pre",className:"language-python:"},"runModeOutConsole()\n")),Object(l.b)("h3",{id:"run-mode---active-console"},"Run mode - Active console."),Object(l.b)("p",null,"Este es el modo en el que el dispositivo permanecer\xe1 constantemente en funcionamiento. El dispositivo realizar\xe1 los siguientes pasos:"),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},"Sincronizaci\xf3n de fecha y hora, a trav\xe9s del RTC DS3231."),Object(l.b)("li",{parentName:"ul"},"Iniciaci\xf3n de la alarma para la transmisi\xf3n de paquetes."),Object(l.b)("li",{parentName:"ul"},"Se activa alarma."),Object(l.b)("li",{parentName:"ul"},"Se adquiere datos de los sensores y se almacena."),Object(l.b)("li",{parentName:"ul"},"Se une a la red lorawan y transmite los paquetes."),Object(l.b)("li",{parentName:"ul"},"Entra en modo de reposo profundo.\n")),Object(l.b)("h3",{id:"run-mode---inactive-console"},"Run mode - Inactive console,"),Object(l.b)("p",null,"Este es el modo en el que el dispositivo permanecer\xe1 constantemente en funcionamiento. El dispositivo realizar\xe1 los siguientes pasos:"),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},"Sincronizaci\xf3n de fecha y hora, a trav\xe9s del RTC DS3231."),Object(l.b)("li",{parentName:"ul"},"Desabilita la consola."),Object(l.b)("li",{parentName:"ul"},"Iniciaci\xf3n de la alarma para la transmisi\xf3n de paquetes."),Object(l.b)("li",{parentName:"ul"},"Se activa alarma."),Object(l.b)("li",{parentName:"ul"},"Se adquiere datos de los sensores y se almacena."),Object(l.b)("li",{parentName:"ul"},"Se une a la red lorawan y transmite los paquetes."),Object(l.b)("li",{parentName:"ul"},"Entra en modo de reposo profundo.")),Object(l.b)("h2",{id:"m\xe9todos-de-configuraci\xf3n"},"M\xe9todos de configuraci\xf3n."),Object(l.b)("h3",{id:"real-time-clock-rtc-ds3231"},"Real time clock (RTC) ds3231"),Object(l.b)("p",null,"The external real time clock (RTC) ds3231 is the one that will keep the system synchronized in time and date, due to an independent battery. The methods for synchronization are presented below."),Object(l.b)("pre",null,Object(l.b)("code",{parentName:"pre",className:"language-python:"},"ds3231.ds1307init_sinc(None)\n")),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},"Synchronizes the external real-time clock (ds3231) with the internal\ntime (lopy 4)."),Object(l.b)("li",{parentName:"ul"},"Response: (year, day, month, hour, minute, second, millisecond,\nNone)")),Object(l.b)("pre",null,Object(l.b)("code",{parentName:"pre",className:"language-python:"},"get_time_ds3231(None)\n")),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},"Obtains the date and time from the external real-time clock\n(ds3231)."),Object(l.b)("li",{parentName:"ul"},"Response: (year, day, month, hour, minute, second, millisecond,\nNone)")),Object(l.b)("pre",null,Object(l.b)("code",{parentName:"pre",className:"language-python:"},"ds3231.sinc_RTC_from_ds3231(None)\n")),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},"Synchronizes the internal clock (lopy 4) with the time of the\nexternal real-time clock (ds3231)."),Object(l.b)("li",{parentName:"ul"},"Response: (year, day, month, hour, minute, second, millisecond,\nNone)")),Object(l.b)("h3",{id:"temperature-and-humidity-sensor-dht11"},"Temperature and humidity sensor DHT11"),Object(l.b)("p",null,"The sensor reading is carried out by the following method:"),Object(l.b)("pre",null,Object(l.b)("code",{parentName:"pre",className:"language-python:"},"result = th.read(None)\n")),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},"Response: result.temperature"),Object(l.b)("li",{parentName:"ul"},"Response: result.humidity")),Object(l.b)("h3",{id:"mb7388-hrxl-sensor-dht11"},"MB7388 HRXL sensor DHT11"),Object(l.b)("p",null,"The sensor reading is carried out by the following method:"),Object(l.b)("pre",null,Object(l.b)("code",{parentName:"pre",className:"language-python:"},"    level = level_data(None)\n")),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},"Response: level")),Object(l.b)("h3",{id:"lorawan"},"LoRaWan"),Object(l.b)("pre",null,Object(l.b)("code",{parentName:"pre",className:"language-python:"},"    joinLoraWan() \n")),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},"Configura los par\xe1metros necesarios de la red LoraWan y se une al servidor."),Object(l.b)("li",{parentName:"ul"},"Respuesta: joined ")),Object(l.b)("pre",null,Object(l.b)("code",{parentName:"pre",className:"language-python:"},"    dataSendLoraWan() \n")),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},"Adquiere los datos de los sensores, los almacena y los transmite por LoRaWan"),Object(l.b)("li",{parentName:"ul"},"Response: (dataTempInt, dataHumInt, dataLevel)")),Object(l.b)("h2",{id:"create-a-docs-version"},"Create a docs version"),Object(l.b)("p",null,"Release a version 1.0 of your project:"),Object(l.b)("pre",null,Object(l.b)("code",{parentName:"pre",className:"language-bash"},"npm run docusaurus docs:version 1.0\n")),Object(l.b)("p",null,"The ",Object(l.b)("inlineCode",{parentName:"p"},"docs")," folder is copied into ",Object(l.b)("inlineCode",{parentName:"p"},"versioned_docs/version-1.0")," and ",Object(l.b)("inlineCode",{parentName:"p"},"versions.json")," is created."),Object(l.b)("p",null,"Your docs now has 2 versions:"),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},Object(l.b)("inlineCode",{parentName:"li"},"1.0")," at ",Object(l.b)("inlineCode",{parentName:"li"},"http://localhost:3000/docs/")," for the version 1.0 docs"),Object(l.b)("li",{parentName:"ul"},Object(l.b)("inlineCode",{parentName:"li"},"current")," at ",Object(l.b)("inlineCode",{parentName:"li"},"http://localhost:3000/docs/next/")," for the ",Object(l.b)("strong",{parentName:"li"},"upcoming, unreleased docs"))),Object(l.b)("h2",{id:"add-a-version-dropdown"},"Add a Version Dropdown"),Object(l.b)("p",null,"To navigate smoothly across versions, add a version dropdown."),Object(l.b)("p",null,"Modify the ",Object(l.b)("inlineCode",{parentName:"p"},"docusaurus.config.js")," file:"),Object(l.b)("pre",null,Object(l.b)("code",{parentName:"pre",className:"language-js",metastring:'title="docusaurus.config.js"',title:'"docusaurus.config.js"'},"module.exports = {\n  themeConfig: {\n    navbar: {\n      items: [\n        // highlight-start\n        {\n          type: 'docsVersionDropdown',\n        },\n        // highlight-end\n      ],\n    },\n  },\n};\n")),Object(l.b)("p",null,"The docs version dropdown appears in your navbar:"),Object(l.b)("p",null,Object(l.b)("img",{alt:"Docs Version Dropdown",src:a(135).default})),Object(l.b)("h2",{id:"update-an-existing-version"},"Update an existing version"),Object(l.b)("p",null,"It is possible to edit versioned docs in their own folder:"),Object(l.b)("ul",null,Object(l.b)("li",{parentName:"ul"},Object(l.b)("inlineCode",{parentName:"li"},"versioned_docs/version-1.0/hello.md")," updates ",Object(l.b)("inlineCode",{parentName:"li"},"http://localhost:3000/docs/hello")),Object(l.b)("li",{parentName:"ul"},Object(l.b)("inlineCode",{parentName:"li"},"docs/hello.md")," updates ",Object(l.b)("inlineCode",{parentName:"li"},"http://localhost:3000/docs/next/hello"))))}b.isMDXComponent=!0},121:function(e,t,a){"use strict";a.d(t,"a",(function(){return d})),a.d(t,"b",(function(){return m}));var n=a(0),r=a.n(n);function l(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function o(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function i(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?o(Object(a),!0).forEach((function(t){l(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):o(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function c(e,t){if(null==e)return{};var a,n,r=function(e,t){if(null==e)return{};var a,n,r={},l=Object.keys(e);for(n=0;n<l.length;n++)a=l[n],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(e);for(n=0;n<l.length;n++)a=l[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var s=r.a.createContext({}),b=function(e){var t=r.a.useContext(s),a=t;return e&&(a="function"==typeof e?e(t):i(i({},t),e)),a},d=function(e){var t=b(e.components);return r.a.createElement(s.Provider,{value:t},e.children)},u={inlineCode:"code",wrapper:function(e){var t=e.children;return r.a.createElement(r.a.Fragment,{},t)}},p=r.a.forwardRef((function(e,t){var a=e.components,n=e.mdxType,l=e.originalType,o=e.parentName,s=c(e,["components","mdxType","originalType","parentName"]),d=b(a),p=n,m=d["".concat(o,".").concat(p)]||d[p]||u[p]||l;return a?r.a.createElement(m,i(i({ref:t},s),{},{components:a})):r.a.createElement(m,i({ref:t},s))}));function m(e,t){var a=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var l=a.length,o=new Array(l);o[0]=p;var i={};for(var c in t)hasOwnProperty.call(t,c)&&(i[c]=t[c]);i.originalType=e,i.mdxType="string"==typeof e?e:n,o[1]=i;for(var s=2;s<l;s++)o[s]=a[s];return r.a.createElement.apply(null,o)}return r.a.createElement.apply(null,a)}p.displayName="MDXCreateElement"},135:function(e,t,a){"use strict";a.r(t),t.default=a.p+"assets/images/docsVersionDropdown-dda80f009a926fb2dd92bab8faa6c4d8.png"},184:function(e,t,a){"use strict";a.r(t),t.default=a.p+"assets/images/Lopy4SCHRLS-1e9ab52bd78d0fc907b9fb200862438c.PNG"},185:function(e,t,a){"use strict";a.r(t),t.default="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKwAAAFACAYAAAAhwJeVAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAABgzSURBVHhe7Z2xcty2Gkb9Mn4Lv4SfQa/gB0jjF8i4TqMmrdo0nkmZUZMuqtJpbpHmjqrMLXR9VvvZv2GABAmQS2i/M4PZJQiAIHH4E+SuVm+ejRkIC2uGwsKaobCwZigsrBkKC2uGwsKaobCwZigs7E48Pj49f/r0xw/p9vbP54eHf86lXri/f/yuDMu5/Lu7v37IS5PqgspS7+np33PuC+of/eH9UbGwO4EEHz/+/vzmzU/P79798lUo3itP4iLWzc3dKZ9XScdrbAPx1AavHz78dlrHK8vv3/96Kg+UVf7btz+f6khatst2VIc20pPoKFjYnUEGxIggIvmIJImUJ1kjMZ+2SnXIR0QgcgryKae8uA6QVvWOhoXdGURJhQUiIOt4hVph4+U7V4f1JEktkFL9SKOpIu0RsbA7UxJWUU+RTfLpMh5TKqXICVuCaF6aq7JNnThHw8LuTElYYJ0i25bCsl5z2xROnKNGV7CwO1MSthRhc/K1CMt2OAnSKYJA5KPecIGF3ZmSsGvnsJEaYbnBKsn6+fPfh5YVLOzO5ISVaDxqElPyrRWW7UZZ4xwWWWM9ypXEviQWdieQY+o5LPNGCYI4TA3I51Ui8Zo+hxWlOoJpAHW1Xd5rrko71NE6UnzEdiQs7E4gbBRCiUt0ehlGtlgmChvzU2Hjuigs7cd1sQxS5tbFto+EhTVDYWHNUFjYSt58OVJOfVILjdWvg9xBd2pLa2moej20HmTzDQu7Axa2HxZ2ByxsPyzsDljYfljYHbCw/bCwO2Bh+2Fhd8DC9sPC7oCF7YeF3QEL2w8LuwMWth8WdgcsbD8s7A5Y2H5Y2B2wsP2wsDtgYfthYXfgaMLe3Nw8f/z48fnh4eGcMw4WdgeOJuzjI3+M+PFLn9o69fTE35l9Oi/tg4XdgaMJK96/f39+t5z7+/vnd+/eWdjXyFGFXSrb58+fnz98+PD89u3bL/vz5pQs7Cuk9SBvxZxsXPLv7u5OkkpQEstEWE8JXimtB3kNzFHnmCqDqBKUiKqbNEQlXYrWY2lhK2g9yGuIEXEqlUBOIinz1Ciohb0CWg/yGlojrOCyf3t7e3oUxuWfyBuF5YnDnljYHVh7kBEDUWJEJOpd6vmpoi59QtyaOazKEKm1D7znJFjDl+qntBYLW8Gag4wQzB0lBvAa89fS44MD9WNKWPqLnOlJFqcb2rdaLOwOLD3IDCIylAZTIiwdbFHzwQFliPBTUlNmSli2MRVJWTcXoVMs7A4sPchEr7kIynqei7Yw9cEBIiF0zTy3RM0HE0T7JVjYHVh6kJFlLnqyfml0Spmqz7rWpwE1si89ISzsDqwRtoatha1h6ilBTRtL98HC7sAaYeceF9XMH+eYKkPbRNipxJRkqg/cWM1RUyZiYXdgjbB6BDSVpmTJlc+lErTNHHQqceO3ZR9yUHxhle9oqHo9LD3ISNA6h+0RYWuYujls7UMOC7sDrQf5EtScNJfAwu7AqMLyyGnuw4W5x2+9sbA7sPQg94huSy+1KYjIPLXUDv3jhmlu6qCpC/NdzVl5749mD8zSg8wAx5uSUpoa9Fx5pbmPVEsgHyIjqtqaaofyyEl5fzQ7EEsPMhLkBpJoJ1F4rDTFVITlkVhNdATKImn8Eo6eDsw91qIP/mh2QFoPMvJyeUYWXpdGpRJTH4tyQuQu48gbT5ap58X0dQ5/NHtAWg4yl08u4UizNBrNMdUe0ZPtImq8nOtDgxpq5tE1ZSIWdgfWHmSiGaIiztzd+hpqZNEfHpIka62wNSeYpwQHZM1BRiZk5ZKZmwKQNzXYUzJyGefyviS6sT3qEHGpp6nAVB+QfI6aMhELuwNLDzJiaO44laZkyZVXWvuUQMS7/LV9iGkJFF9Y5Tsaql4PSw8yEiDtFC0RthdMDVr7sLSfFnYH1gg7ClNPCbbAwu5A60GGpWL0FolpABF1yc3f3FViDRZ2B5YeZGTT3bgEYb6ovBpxuFmL5Utp7pku0Z55JtvXVwqZA9fISD220ZOlxzLFwlaw9CDrcRZJd9G8RxglxJmSLS2vpGe6anuqDdYjfhqtWSZ/bv6pmzvaQfC5k6OGL90+pbVY2AqWHmSEQMgYRdOIxjrELpFbF0+EqbpAHxB8CtanMkdidKW/iIvkLVF36bFMsbAVLD3IyFkzqEtuzpAFUdMToQR9mPurXNbPiZ9ClKUOsq+JuhZ2B5Ye5BoRGejackiKrES3WkFqT4YlJ00EaTU9WcLSY5nSUPV6WHqQGcypSy1QZi4CEkk1BciVndrGFsKyPcqrT0TZpRGa40hai4WtYM1BnoqGTBfm5peIIDF4T500TX1TCrFK9ZRYPyWsbso4WdiW+kP+3AlZguNIWouFrWDNQWZAdSceBWEuyqV0bh6KGEwFELuUKFMCEefqs35KWAlKYl/ofyt0eaLbszRUvR5aDrIkRRAGvfZGhfJzTAlUK9dUOURF6LXRNIeF3YHWg7yGHtGsFU0JemJhd+ASwr5WLOwOWNh+WNgdsLD9sLA7YGH7YWF3wML2w8LugIXth4XdAQvbDwu7Axa2HxZ2ByxsPyzsDljYfljYHdBBduqX1tJQ9XrIHfBlSd96yq2rTWvbUL1SytUppTV18mktDVVNLRroFta2MVVnaXtr+9CTy279Sugx0C1t5OqtaaulD7247NavhB4D3dJGrt6atlr60IvLbv1K6DHQLW2k9VraWVu3F5fd+pXQY6Bb2kjrtbSztm4vLrv1K6HHQLe2Eeuubae1Dz247NavhB4D3dqG6ra20VK/B5fd+pXQY6Bb21Dd1jZa6vfgslu/EnoMdGsbR+hDDyzsDhxBliP0oQcWdgeOIMsR+tADC7sDR5DlCH3ogYXtgH6KqPQLKUeQZa4+fdd+lGjtQw8s7Er4uSH9Zqt+q4rfzOL3qtJBTwea9cojpeVpN/3trbSNpZTq80Nv9Juk/aBc7sfsWvvQAwu7AgZSP6SWDirysS7+PGZuoCnDb23lfhSOPASKEbtVllx9fg4pd4KxT/oxuUhrH3pgYVfAQE/96p+EFulAsx5Zp0AiIq1YIwvi64TI1aeP6QkXYR/jb3yt6UNvLOwKkG1qoCH+hmo60MiYRrUc8RcMl8rCtmP0TOsj8tyPvbGPrSdNbyzsCqaiq4hS5mSZ+/VtiFG4RhYk5ec8qafypT7E/k0R9zVt4xJY2BW0CgtzbSBezeUY+SlLNFUZIrOmLRbWnCKYBryU9MvbkBtoREMsIm2cXpCPJPFSDGkbSMqNmfLpE5LGyzztqu20fuzjVFoa5bfGwq5Aj3+mEjIx4FAaaGRCzigekTJGVpG2QT2WESoKHyNiJK1P3+KjrKkk0jYugYVdQU6oFCIlCXoMdK4NRKUvSKubvFphY/+miPua68PeWNgdSAc6XqprmZMFWZGWqIlktK/LOszVr6FHG61Y2BVIglrSgaY+kVBCTSWxRBb9m6KaaQkgO5LTJ1Ip8i7pw1ZY2BUggwZ3KpVkIb80f1RZEjdWIm2jhqk+CKIy+dzkqd/Mo0mpuGv60BsLu4KSsFG4eLeeDnRp/og0lEPmOVm0LbZbIk490vpAH9lmbnqikyquy7WxNxZ2BYpaEaKhBjT9UGBuoJFCz1HTu36RtoGwuX6UyPWBbU7BNKE1yvfGwjaCXIqMCMB8MGVqoImkWh/lSEnbmIqsOdL6yD61PRGfB6dtXAIL2wByKjJOCVQaaCIY+bn5IkT50zZqhCXSl+aw5NdE6LidtI1LYGFXwmBrAHMDj2z/+e//TknltAwxKkusNFGm1EZ6g1ZKpfraxhwIW2rjEljYFSgykrhxYVDTxFy0NNCIwjLSzaVSG2xjDk6EUn36QPtpv9M01YdLYGFXwCDOPdpivSKYBlqQT5k5ODFE2kZN/UiuD3P7QKKMSNu4BBZ2BfFGpARTAs1B04EuPdaaIm2Dk0YnRIm4nbR+7N8UcRtpG5fAwq5gThTx7VL60ymtuZSmdbSMsMhDFMyBjMyPVT7tA083co/PcpTauAQWtgNEsZzEPQY6rTPVBpLyqIrLuKKhyqd9oL8l2VNKbVwCC7sCbrSIcCTmmQw+ciiP9P0D95eB3gJOFralx2vqB/1CSJ1IaR/UZ6Y3uZMtx5b7UYuFXYGeEiAuUY0B18ArxXnuFgONpHx0KkmJqvQrfiQcL/tpH+ijbup4pT5tTk0TttiPpVjYFSAFAy5y88HvH9r3H2iip0SN2y5d5mv6QLTmREv3T2yxH0uxsCuIUawEA76lsICoio6K9i3CCtpVBFcUhq32YwkWdgU1NysM+LdHStsPNLIirSRDujUnjdrRVGPrqc1SLOwKEEIy5kAWbnzE3gPNdISoi7wlYRGTJFRHoipiR/bejxwWdiUMKIOcgiBRFLjUQM89JdBUQjdverpQ4lL7EbGwDSAEg61HWQx6KitcaqCJ9CRI+0Af1V/2I42mOS61HxEL2wF9cFAa9D0Gmu0v6QNl4/y0hj32Yw4LuwNbDTTRE+l0OScRMfkQASEjaR8QuyaqRrbajyVY2B3YYqCRFTG5nOuyL5BV37MVPfqwxX4sxcLuwBYDzc3R1OM1CS169GGL/ViKhd2BLQY6/YQrR3w01aMPW+zHUizsDmwx0FPRVehGDHr0YYv9WMqrF/anLzckpEuyxUBb2FfKaxWWKYGELCWmBLxCjz5ssR9LsbA7sMVA6zHWVIofYvTowxb7sRQLuwNbDPTUR6iCDzR6fgFni/1YioXdgUMMdIc+HGI/zq+vgpycFvaFHn04xH6cX18FFrZMjz4cYj/Or68CC1umRx8OsR/n11eBhS3Tow+H2I/z66vAwpbp0YdD7Mf5dThq5czl7c0hBrpDHw6xH+fXIv88PDzf3dx8Hfhf378/5f3+8eUvR//49Onrul/evXv+N3whI64jpctKP799+/zbhw+ndmtR3Uht3t4cYqA79OEQ+3F+zYJADDZyPp2/9cMrciFZRDKyLoLAiCz+/vz5VI5XYP1fd3en9mL+HJQlRWrz9uYQA92hD4fYj/PrDyASA010zUGkjSAsslIHASOx7OP9/akMrxG2J2lroFxatjavlvQ3pNb+ptQhBrpDHw6xH+fXH0A6Brr2Mo2wSChpY70aYeHP29vTupooSzlSpDavFgv7PYfYj/PrD2jeWouE1RQgzmdrhdU62kpJxUuXYSqvNWmwWtIl6dGHQ+zH+fUHkIyBStFcVUniSVhgnss6zWct7Eu6JD36cIj9OL/+gMTMXZ7TGyeIwoLKMLXoMSUgnyTSZajNq6XXlOAIvHphFSXTR1WQky4VFni6QLkaYXXTlT59ENQhiXQZavNqsbDfc2hhQTdeSBsFU37M4/Kfi4zUjcKm0RlRaU9PCGpv8ihLitTmXSNXISwgkO78lZCQ6KnIG9el808itR6NaZqRJmRlG3rWW4PqRmrzrpGrEbYH6ZSiB7Vy5vKuEQt7YWrlzOVdIxb2wtTKmcu7RizsAbGwZSzsAbGwZSzsAbGwZSzsAbGwZSzsAbGwZSzsIFjYFyzsIFjYFyzsIFjYFyzsIFjYFyzsIFjYFyzsK4Uv6iz51tha2M4WXwoqcTXC8p3XXErh4Mf1+l5rmk/K5cWUfic2lyeQi/W9Bp/v6aZfkeyNvmZJv/fiaoTV33aReB+X+Z6rohFC8T1ZrdMPbZCftsFA6b3W8Z1Y3usVkDCWSf/6gS9+k6ftsjwC+n6xhV1O1ZRA0kT0VwekKBHLuQhFfUnMQPH3WyKtoz+TIU9t86ovegMnSmxDfw+2x+W8B/TVwi5ntbCgSCkRYUpY5SNVFCuto4FMB5Qy6kdusJdKoLKp5LllysYkVJYrSW7aovLxpAYLu44mYYGop4gIDARRUAOlxGU7JzKUJE/hxCiVQwjaScUoQX90EumEY/7KvsRtsC/kUZb2SbzXVIdEfa3X36qxXmWpz/v0JLWwy2kWVgMleK8Bjon8VmHTOWyEKUpNG4Ao9EmoHq+xL5JO29R60JSIfdV6iQuIqxNBJ1MUNF3eGgt7RjIK3ufEoVwuH0p1IsxRFb1SEKL0G2A5iHRsk+iZXsZjPxEq7lu6TLl4XNJlIWHjPrJsYZfTJKwGIsqSDoyIIqSU6gikmnoCQF1FuVp0+WfbupGDtJ+s0xSHdbEs5eJxSZepw7HRdmK7LFvY5TQJy+ClB74kH/Vz+VCqA1vISnnVoe9xH9J+so+61KfbYjkel7hMn5nCKIKn+5get625GmE5qEQIEu9JXJ4VNSQTA0nUIo+oooEiX20wgHGQSnUEy8ii7ZIop5sX1lFf6+iL5o1TUBaxqKtIy7ZIvGcd29Cy2iepj6ynnOqyrGjKMu+1v/SLfOTXNtln+hpPgC25GmEZlFwiWkgcYJDieomT5pNEqQ4wkAx6XE/SJRkJ0nUkBJmD7VJOERGBgO2rHdqnD1pWQkLKxe3nliWtTjC2pf1TORLl9uBVC/uaflOqBUXDlHhpPzoaO8lGWjuWFnYjFEFLqfYyrAhP9FRdomRO4qPCuEVZW6RrqduL2SlB3Emn15WWsrZeTyzsFaelrK3XE89hXzlR0DQtZW29nljYVw7jFiVtka6lbi9mpwTmddAqK1hYsxtv3vCPRdqG28Ka3bCwZigsrBkKC2uGwsKaobCwZigsrBkKC2uGwsKaobCwZigsrBkKC2uGwsKaocDVRl8trNkPC2uGwsKaRdzfP34d8Jjevfvl+fb2z3Opb3z8+PvXMrn1S7GwZjFPT/+eBvzTpz++Ln/48Nsp7+7ur1MeICiCg0R/ePjntLwWC2tWEYWFx8enH/JSWE+5FiysWUWUk6h5c3N3ystFUCRlvacE37CwO6NBV0LGXPSMc96p6FuLhE3TEtSfS7Kwy6YVCfj5899f35dgjovQlOsZZS2sqSZKqicBczdU3Ji9f//reWkdOVlJS7CwV0gUlgjKYy3SFJRH7jXkJCWtwcJeGXqsFeUjupJHBM1FWvIQeu1TglZJIxb2ikg/OIiXeM1Tla9nsySeEsxNGaaIwrZKqz5dEgt7JfQQ18KaXUmlXSquhTUXwcKawxMljWkJFtZsTk5S0hosrNmcVkkjFvZK4Xls/DphhOetfFAQ1/NIjDwlffWQMjE/RxQ2pjVY2CsEsUoDz/PWt29/Pn2wwPNXnscCgupbXbxGYdXW3CdhOWlJSyj1e08Wdtm0wpde9B2CFD40iJEVeSUnr9TRMlCWOkTsJVhYswjJF2EqQF6Uj2hMRIVUWNYt/X5BFNXCmmpywubykFIf4Wo9EZqpQozENbSIKizsldIiLNMEXmuF7SGqYLtpH/fGwl6AFmF51ZdjaqYEFtY0k5MzN4dFyPikgPW8gr7hxRx36qbLwppmcsLC0qcE+jMbvi8796TAwppVIJyeqRJB4xez43NY5F3yHFbtlbCwZhXIxtxUKf1LgpZPukglLKwZCgtrhsLCmqGwsGYoLKwZCv9kvBkKC2uGwsKaobCwZigsrBkKC2uGwsKaobCwZigsrBkKC2uGwsKaobCwZigsrBmC//z3f6ckYbW8BgtrNsfCmiGRsC1YWLMbPWSzsGZzvk0JXmTzlMAcGgtrhqSHbBbW7IaFNUNhYc1QWFgzFBbWDIWFNUNhYc1QWFgzFBbWDIWFNUNhYc1QtMqm+q3ttGJhr4RUuB7pEljYKyEnXGu6BBbWVHEEWcHCmmouLStYWFONhTVDYWHNUFhYMxQW1gyFhTVDYWHNUFhYMxQW1gyFhTVDYWHNUFhYMwQ9f5+rFQtrZrGwZkgk7CWxsKYaC2uGQFOAn968OSVPCcyhsbBmSCTsJbGwphoLa4bCwpqhsLBmKCysGQoLa4bCwpqhsLBmKCysGQoLa4bCwpqhsLDmkEjMtWlLLKz5jpyAS9OWWFgzFBbWDIWFvWJ+//jx62X8z9vbc26eUtlf37//mk96vL8/r3l+/uPTp6/5vO+Bhb1SkE5y8YpU/zw8nJZT5sqynry/P38+53zjtw8fZk+GJVhYcwLhnh4fz0vT5Mr+/Pbt8193d+elb/SKrMLCXjmId3dzUxUFp8qSh7SRf5+eshK3YGGvGF3eSXORcK4scrJOUwdA1tqoXYuFvXIQTXPQuSg7V5b5KjdhguXeWFhzIpVtilJZRWGiKjdlvacDYGHNCS7zPLqqYaos81iEJhGRe2NhzSka/vLuXdV8c66spgxbTAfAwl4pCIVYJO7843NVZCRfl/Spsim6+dpiOgAW1gyFhTVDYWHNUFhYMxDPz/8H8qGsl2mEAV8AAAAASUVORK5CYII="},186:function(e,t,a){"use strict";a.r(t),t.default=a.p+"assets/images/ds3231SCH-c6b4bc4cca8ee47d6f7245f878d5c258.PNG"},187:function(e,t,a){"use strict";a.r(t),t.default=a.p+"assets/images/BornerconRLS-3c531cf811f6efd1b51fa18421e1c9f0.PNG"},188:function(e,t,a){"use strict";a.r(t),t.default=a.p+"assets/images/RiverLevelSensorDatalogger_3d_borner-cb72f352888ac5e072b4bbc713c5048b.PNG"},189:function(e,t,a){"use strict";a.r(t),t.default=a.p+"assets/images/usbConnect-8bcba4b8475ef0c74d46975a0fa2eb0e.PNG"}}]);