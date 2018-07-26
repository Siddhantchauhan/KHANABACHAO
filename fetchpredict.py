#!F:/python.exe
print("Content-Type: text/html")
print("""
  """)
import pymysql
import cgi
from sklearn import neural_network as nn
import pandas as pd
from sklearn import model_selection as cv
from sklearn import preprocessing as pp
import pickle
import numpy as np
import matplotlib.pyplot as plt

req=cgi.FieldStorage()




scaler=open('scaler.pickle','rb')
scale=pickle.load(scaler)

normaliser=open('normaliser.pickle','rb')
norm=pickle.load(normaliser)

time=req.getvalue("ts");
adult=req.getvalue("ano");
weather=req.getvalue("wr");
ac=req.getvalue("ac");
child=req.getvalue("cno");
var=req.getvalue("var");
holiday=req.getvalue("hd");

x=[[adult,child,time,ac,var,weather,holiday]]
x=scale.transform(x)
x=norm.transform(x)



modeler=open('shadinn.pickle','rb')
model=pickle.load(modeler)
result=model.predict(x)
result=result[0].tolist()
sabzi=result[0]
dal=result[1]+10
chapati=result[2]
rice=result[3]


fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.bar([0], [dal],
        color='y')
ax1.bar([1], [sabzi],color='c')
ax1.bar([2], [rice],
        color='y')

ax1.set_ylabel('KGs')

ax1.set_yticks([20,40,60,80,100,120,140,160,180,200,220,240])
plt.xticks(range(0,4),['Dal','Sabzi','Rice','Chapati'])
ax2 = ax1.twinx()
ax2.bar([3], [chapati])
ax2.set_ylabel('In Numbers', color='r')
ax2.set_yticks(range(0,4000,200))
for tl in ax2.get_yticklabels():
    tl.set_color('r')
graphname=str(rice)+'.png'    
plt.savefig(graphname)
 

print('''
<html>
<head>



<div class='content'>
<img src="'''+graphname+'''" width="500px" height="400px" style="float:right;">
<h2>PREDICTED QUANTITY:</h2>

<h3>Sabzi:'''+str(int(sabzi))+''' kilograms</h3>
<h3>Daal:'''+str(int(dal))+'''  kilograms</h3>
<h3>Rice:'''+str(int(rice))+'''  kilograms</h3>
<h3>Chapati:'''+str(int(chapati))+'''  units</h3>

</div>




</head>
</html>
''')












 












