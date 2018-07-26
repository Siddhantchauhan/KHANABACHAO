#!f:/python.exe
print("Content-Type: text/html")
print("""
  """)
import pymysql
import cgi

 

req=cgi.FieldStorage()
db=pymysql.connect(host='localhost',user='root',password='123',db='hackathon')

cmd=db.cursor()
loginid=req.getvalue("lgid");
address=req.getvalue("hadd");
password=req.getvalue("pwd");
pincode=req.getvalue("pcd");
name=req.getvalue("hname");
cphone=req.getvalue("cno")
q="insert into caterer values('{}','{}','{}',{},'{}',{})".format(loginid,password,name,pincode,address,cphone)
cmd.execute(q)
db.commit()

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
   
Finalnumber=str(cphone)
M = Mobile()
M.Config()
M.Message(str(Finalnumber), "Your mobile number has been successfully linked to your account as a Caterer.")



print('''  <meta http-equiv="refresh" content="0;url=http://localhost/login.py" />''')


 












