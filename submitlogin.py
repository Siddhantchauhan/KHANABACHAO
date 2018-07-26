#!f:/python.exe
import pymysql
import cgi
print("Content-Type: text/html")
print("""
  """)
 

req=cgi.FieldStorage()
db=pymysql.connect(host='localhost',user='root',password='123',db='hackathon')

cmd=db.cursor()
loginid=req.getvalue("lid");
password=req.getvalue("psw");

q="select * from caterer where loginid='{}' and password = '{}'".format(loginid,password)

cmd.execute(q)
r=cmd.fetchall()
if ( r[0][1]==password) :
  db.commit()
  print('''
  <html>
  <head>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <style>
  body{
  background:url('Food-wastage1.jpg');
  margin:0;  
  }
  .header a,.dropdown{
  top:0;
  float: right;
  text-align: center;
  padding:16px;
  background: rgba(0, 0, 0, 0); /* Black background with transparency */
  text-decoration: none;
  font-size: 150%;
  color:666666	;
  font-family:Arial, Helvetica, sans-serif;
  overflow:hidden;
  }
  .header a:hover,.dropdown:hover .dropbtn {
  color: 999999;
  }

  .header a.active {
  background-color: #4CAF50;
  color: white;
  }
  .footer{
   position: fixed;
   left: 0;
   bottom: 0;
   width: 100%;
   text-align:center;

   }
  .footer font{
  float:left;
  right:100px;
  font-size:300%;
  color:666666;
  font-family:Arial, Helvetica, sans-serif;
  }
  .content{
    position: absolute;
    background: rgba(0, 0, 0, 0.2); /* Black background with transparency */
    color: #f1f1f1;
    tp:30%;
    left:30%;
    right:30%;
    bottom:30%;
    font-size:300%;
    color:666666;
  }
  .dropdown .dropbtn {
    font-size:100%;
    border: none;
    outline: none;
    color:666666;
    background-color:inherit;
    font-family:inherit;
    top:0;
	float: right;
    text-align: center;
    padding:0;

  }
  .dropdown-content {
    display: none;
    position: absolute;
    background-color:rgba(0, 0, 0, 0.2);
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
  }
  .dropdown-content a {
    float: none;
    color: black;
    text-decoration: none;
    display: block;
    text-align: left;
    font-size:50%;
    padding:16px;

  }
  .dropdown-content a:hover {
    background-color: #ddd;
  }

  .dropdown:hover .dropdown-content {
    display: block;
  }
  .profile{
  top:14%;
  bottom:14%;
  left:10%;
  right:10%;
  background-color:white;
  opacity:0.6;
  position: absolute;
  }
  .profile a,button{
  background-color: black;
    border: none;
    widht:50%;
    color: white;
    padding: 15px ;
    float:right;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    left:10%;
    }
  .profile a:hover {
    background-color: grey;
    color:white;
  }
  </style>
  </head>
  <body>
  <div class='header'>
  <a href='#'>About</a>
  <a href='front.py'>Home</a>
  <a href='login.py'>Login</a>
  <div class="dropdown">
    <button class="dropbtn">Signup
    </button>
    <div class="dropdown-content">
      <a href="signin.py">caterer</a>
      <a href="orgsignin.py">organization</a>
    </div>
  </div>
  </div>
  <div class='profile'>
  <font style='font-family:Arial, Helvetica, sans-serif' color=black size=+5>Welcome '''+r[0][2]+'''</font>
  <a href='predict.py' target='screen'>Predict quantity</a>
  <a href='foodinfo.py' target='screen'>food left?</a>
  <a href='login.py'>Logout</a>
  <iframe name='screen' width=98% height=80%></iframe>
  </div>
  <div class='footer'>
  <font>follow us on:</font>
  <i class="fa fa-facebook-square" style="font-size:48px;color:333399"></i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <i class="fa fa-instagram" style="font-size:48px;color:FF6699"></i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <i class="fa fa-twitter" style="font-size:48px;color:3399FF"></i>


  </div>
  </body>
  </html>
  ''')
else:
    print('<h>INVALID LOGINID/PASSWORD</h>')
    print("<a href='login.py'>LOGIN AGAIN</a>")







 













