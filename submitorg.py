#!f:/python.exe
import pymysql
import cgi
print("Content-Type: text/html")
print("""
  """)
 

req=cgi.FieldStorage()
db=pymysql.connect(host='localhost',user='root',password='123',db='hackathon')

cmd=db.cursor()
address=req.getvalue("add");
opincode=req.getvalue("pcd");
oname=req.getvalue("oname");
phone=req.getvalue("cno");
q="insert into organization values('{}',{},{},'{}')".format(oname,opincode,phone,address)

cmd.execute(q)
db.commit()
print("fd")


import serial
import time
class Mobile:
    def Config(self):
        self.ser = serial.Serial('COM3', 9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout =5, xonxoff=False, rtscts=False)
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
        time.sleep(1)
   
Finalnumber=str(phone)
M = Mobile()
M.Config()
M.Message(str(Finalnumber), "Your mobile number has been successfully linked to your account.")





print('    <meta http-equiv="refresh" content="0;url=http://localhost/front.py" />')


 












