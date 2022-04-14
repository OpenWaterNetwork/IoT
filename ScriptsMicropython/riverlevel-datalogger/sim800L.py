import time
import pycom
import os
from machine import RTC
from machine import Timer
from machine import UART
import struct
from binascii import hexlify

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
        print(gprsdataread, len(gprsdataread))

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
            #ser_gprs.write("AT+SAPBR=3,1,\"USER\",\"movistar\"\r\n") #movistar
            #readGPRSdata()
            #ser_gprs.write("AT+SAPBR=3,1,\"PWD\",\"movistar\"\r\n") #movistar
            #readGPRSdata()
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

    def send_GPRS_POST(self, datos):
        contRetrans = 0
        maxRetrans = 5
        float_retransmit=True
        gprsdataread=''
        flagTrans1=0

        self.__ser_gprs.write("AT+HTTPTERM")
        self.__ser_gprs.write("\r\n")
        self.readGPRSdata()
        self.__ser_gprs.write("AT+HTTPINIT")
        self.__ser_gprs.write("\r\n")
        self.readGPRSdata()
        self.__ser_gprs.write("AT+HTTPPARA=\"CID\",1\r\n")
        self.readGPRSdata()
        self.__ser_gprs.write("AT+HTTPPARA=\"URL\"," +"\""+"http://api.thingspeak.com/update"+"\""+"\r\n")
        self.readGPRSdata()
        self.__ser_gprs.write("AT+HTTPPARA=\"CONTENT\"," +"\""+"application/x-www-form-urlencoded"+"\""+"\r\n")
        self.readGPRSdata()
        datos_enviar = datos.replace('+','%2B')
        http_data = "api_key=IANS5HS4PBO289IM&field1="+ datos_enviar
        print(http_data)
        self.__ser_gprs.write("AT+HTTPDATA=1000,10000\r\n")
        time.sleep(2)
        self.__ser_gprs.write(http_data)
        time.sleep(0.5)
        self.readGPRSdata()
        self.readGPRSdata()
        self.__ser_gprs.write("AT+HTTPACTION=1\r\n")
        self.readGPRSdata()
        time.sleep(2)
        gprsdataread=readGPRSdata()

        while (str(gprsdataread).find("HTTPACTION: 1,200")==-1):
            if (str(gprsdataread).find("HTTPACTION: 1,200")==-1):
                if contRetrans == maxRetrans:
                    print("Forzar reinicio de GPRS para retransmision")
                    #dataSave("log",("Forzar reinicio de GPRS para retransmision "+generals.gprsdataread))
                    float_retransmit= False
                    break

                contRetrans = contRetrans + 1;
                print("Retransmision # " + str(contRetrans))
                #dataSave("log",("Retransmision # " + str(contRetrans) + " " + generals.gprsdataread))
                flagTrans1=0
                self.__ser_gprs.write("AT+HTTPACTION=1\r\n")
                self.readGPRSdata()
                time.sleep(2)
                self.readGPRSdata()

        if (str(gprsdataread).find("HTTPACTION: 1,200") >= 0):
            flagTrans1=1

        ser_gprs.write("AT+HTTPTERM\r\n")
        self.readGPRSdata()

        self.__ser_gprs.write("AT+SAPBR=0,1\r\n")
        time.sleep(2)
        self.readGPRSdata()

        return float_retransmit

    def GPRS_MQTT_CONNECT(self,device_id,mqttserver,user, password,port,topic,msg_pub):

        contRetrans = 0
        float_retransmit=True
        end_gprsAT=bytearray(b"\x1a")
        keepalive = 0
        lw_topic = None
        lw_msg = None
        lw_qos = 0
        lw_retain = False
        clean_session=True

    #--connect
        msg = bytearray(b"\x10\0\0\x04MQTT\x04\x02\0\0")
        msg[1] = 10 + 2 + len(device_id)
        msg[9] = clean_session << 1

        if user is not None:
            msg[1] += 2 + len(user) + 2 + len(password)
            msg[9] |= 0xC0
        if password is not "":
            msg[1] +=  2 + len(password)
        if keepalive:
            assert keepalive < 65536
            msg[10] |= keepalive >> 8
            msg[11] |= keepalive & 0x00FF
        if lw_topic:
            msg[1] += 2 + len(lw_topic) + 2 + len(lw_msg)
            msg[9] |= 0x4 | (lw_qos & 0x1) << 3 | (lw_qos & 0x2) << 3
            msg[9] |= lw_retain << 5

        len_user = struct.pack("!H", len(user))
        user_hex= bytearray(user)
        len_device_id=struct.pack("!H", len(device_id))
        device_id_hex=bytearray(device_id)
        #pkt_connect=msg+len_device_id+device_id_hex+len_user+user_hex+end_gprsAT

        pkt_connect=msg+len_device_id
        pkt_connect_hex= hexlify(pkt_connect, " ")

        print(hex(len(pkt_connect)), hexlify(pkt_connect, " "))

    #-Publish
        retain=False
        qos=0

        pkt = bytearray(b"\x30\0")
        pkt[0] |= qos << 1 | retain
        sz = 2 + len(topic) + len(msg_pub)
        if qos > 0:
            sz += 2
        assert sz < 2097152
        i = 1
        while sz > 0x7f:
            pkt[i] = (sz & 0x7f) | 0x80
            sz >>= 7
            i += 1
        pkt[i] = sz
        len_topic_msg_pub = struct.pack("!H", len(topic))
        topi_hex= bytearray(topic)
        msg_pub_hex=bytearray(msg_pub)
        #pkt_publish = pkt + len_topic_msg_pub + topi_hex + msg_pub_hex+end_gprsAT
        pkt_publish = pkt + len_topic_msg_pub

        pkt_publish_hex = hexlify(pkt_publish, " ")

        print(hex(len(pkt_publish)), hexlify(pkt_publish, " "))

    #- GPRS
        try:

            self.__ser_gprs.write("AT+CSTT=\"internet.claro.com.ec\",\"\",\"\"\r\n")
            self.readGPRSdata()

            self.__ser_gprs.write("AT+CIICR\r\n")
            self.readGPRSdata()

            self.__ser_gprs.write("AT+CIFSR\r\n")
            self.readGPRSdata()

            self.__ser_gprs.write("AT+CIPSTART=\"TCP\",\""+mqttserver+"\",\""+str(port)+"\"\r\n")
            self.readGPRSdata()
            self.readGPRSdata()

            time.sleep(2)

            self.__ser_gprs.write("AT+CIPSEND\r\n")
            self.readGPRSdata()
            time.sleep(1)
            self.__ser_gprs.write(pkt_connect)
            self.__ser_gprs.write(device_id)
            self.__ser_gprs.write(len_user)
            self.__ser_gprs.write(user)
            self.__ser_gprs.write(end_gprsAT)
            self.readGPRSdata()

            time.sleep(2)
            self.__ser_gprs.write("AT+CIPSEND\r\n")
            self.readGPRSdata()
            time.sleep(1)
            self.__ser_gprs.write(pkt_publish)
            self.__ser_gprs.write(topic)
            self.__ser_gprs.write(msg_pub)
            self.__ser_gprs.write(end_gprsAT)
            self.readGPRSdata()


        except Exception as e:
            print("Error network connecting")
            float_retransmit=False

        time.sleep(1)

        return float_retransmit

    def TCP_connected(self,mqttserver,port):

        try:

            self.__ser_gprs.write("AT+CSTT=\"internet.claro.com.ec\",\"\",\"\"\r\n")
            self.readGPRSdata()

            self.__ser_gprs.write("AT+CIICR\r\n")
            self.readGPRSdata()

            self.__ser_gprs.write("AT+CIFSR\r\n")
            self.readGPRSdata()

            self.__ser_gprs.write("AT+CIPSTART=\"TCP\",\""+mqttserver+"\",\""+str(port)+"\"\r\n")
            self.readGPRSdata()
            self.readGPRSdata()

        except Exception as e:
            print("Error network connecting")
            float_retransmit=False

    def TCP_send(self,pkg_transmit):

        time.sleep(2)
        self.__ser_gprs.write("AT+CIPSEND\r\n")
        self.readGPRSdata()
        time.sleep(1)
        self.__ser_gprs.write(pkg_transmit)

    def TCP_send_append(self,pkg_append):
        self.__ser_gprs.write(pkg_append)

    def TCP_end_send(self):

        end_gprsAT=bytearray(b"\x1a")
        self.__ser_gprs.write(end_gprsAT)
        self.readGPRSdata()

###-- GPRS in sleep mode to reduce power consumption.

    def GPRS_sleep(self):
        self.__ser_gprs.write("AT+CSCLK=1\r\n")
        gprsdataread=self.readGPRSdata()
        time.sleep(2)
