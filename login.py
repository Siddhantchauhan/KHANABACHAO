#!f:/python.exe
 
print("Content-Type: text/html")
print("""
""")

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
  font-size: 200%;
  color:666666;
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
color:black;
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
    color:FFFFCC;
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
.form{  font-family:Arial, Helvetica, sans-serif;
        position: absolute;
	    right: 0;
	    top:30%;
	    margin: 20px;
	    max-width: 300px;
	    padding: 16px;
	    background-color: white;
	    opacity:0.8;

}
input[type=text], input[type=password] {
    width: 100%;
    padding: 15px;
    margin: 5px 0 22px 0;
    border: none;
    background: #f1f1f1;
}
input[type=text]:focus, input[type=password]:focus {
    background-color: #ddd;
    outline: none;
}
.btn {
    background-color:black;
    color: white;
    padding: 16px 20px;
    border: none;
    cursor: pointer;
    width: 100%;
    opacity: 0.9;
}

.btn:hover {
    opacity: 0.5;
}

</style>
</head>
<body>
<div class='header'>
<a href='about.py'>About</a>
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
<div class='content'>
<h3>"WASTING FOOD IS LIKE STEALING FROM THE POOR"</h3>
</div>
<div class='form'>
<h1>Login</h1>
<form action=submitlogin.py method='post'>
      <label for="email"><b>Login</b></label>
      <input type="text" placeholder="Login id" name="lid" required>

      <label for="psw"><b>Password</b></label>
      <input type="password" placeholder="Enter Password" name="psw" required>

      <button type="submit" class="btn">Login</button></form>
</form>
</div>
<div class='footer'>
<font>follow us on:</font>
<i class="fa fa-facebook-square" style="font-size:48px;color:333399	"></i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<i class="fa fa-instagram" style="font-size:48px;color:FF6699"></i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<i class="fa fa-twitter" style="font-size:48px;color:3399FF"></i>


</div>
</body>
</html>
''')

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
