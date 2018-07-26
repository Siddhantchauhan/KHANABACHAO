#!f:/python.exe
print("Content-Type: text/html")

print("""
  """)

import random
import serial
import time
import pymysql
import pandas as pd
import os
import cgi
class Mobile:
    def Config(self):
        self.ser = serial.Serial('COM3', 9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout =5, xonxoff=False, rtscts=False)

    def Message(self,phone,msg):
        
        self.ser.write("AT\r".encode())
        time.sleep(1)
        self.ser.write("AT+CMGF=1\r".encode())
        time.sleep(1)
        self.ser.write(("AT+CMGS=\"{}\"\r".format(phone)).encode())
        time.sleep(2)
        self.ser.write(("{}{}\r".format(msg,chr(26))).encode())
        time.sleep(1)

req=cgi.FieldStorage()

db = pymysql.connect(host= 'localhost', user = 'root', password = '123', db = 'hackathon')
cur = db.cursor()
loginid=str(req.getvalue('id'))
query = "Select * from caterer where loginid='"+str(loginid)+"';"
cur.execute(query)
for i in cur:
    catererinfo=i
    pincode=i[3]


query = "Select * from organization where opincode="+str(pincode)+ ";"
cur.execute(query)
z=[]
for i in cur:
    z=z+[i]
final=random.choice(z)
Finalnumber=int(final[2])
print('message sent')

M = Mobile()
M.Config()
M.Message(str(Finalnumber), "This is a an auto-generated message")
#M.Call(8871076854)
