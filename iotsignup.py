#!z:/python.exe
print("Content-Type: text/html")
print("""
  """) 
import pymysql
import cgi
import serial
import time
class Mobile:
    def Config(self):
        self.ser = serial.Serial('COM4', 9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout =5, xonxoff=False, rtscts=False)
    def Message(self,phone,msg):
        self.ser.write("AT\r".encode())
        a = self.ser.readline()
        a = a.decode()
        self.ser.write("AT\r".encode())
        time.sleep(1)
        self.ser.write("AT+CMGF=1\r".encode())
        time.sleep(1)
        self.ser.write(("AT+CMGS=\"{}\"\r".format(phone)).encode())
        time.sleep(2)
        self.ser.write(("{}{}\r".format(msg,chr(26))).encode())
        time.sleep(3)
        #else:
            #print("<b>ERROR</b>")

Finalnumber='8871076854'
#print('final number=',Finalnumber)
M = Mobile()
M.Config()
M.Message(str(Finalnumber), "Your mobile number has been successfully linked to your account.")
