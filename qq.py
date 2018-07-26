#!f:/python.exe
 
print("Content-Type: text/html")

print("""
  """)
print('''
<html>
<head>
<style>
.form{  font-family:Arial, Helvetica, sans-serif;
        position: absolute;
	    right: 0;
	    width:40%;
	    margin: 20px;
	    max-width: 100px;
	    padding: 16px;
	    background-color: white;

}
font{
font-family:Arial, Helvetica, sans-serif;
color:black;
font-size: 1.875em;
}
h4{
font-family:Arial, Helvetica, sans-serif;
color:993333;
font-size:200%;
}
input[type=numeric],select{
    width: 30%;
    padding: 15px;
    margin: 5px 0 22px 0;
    border: none;
    background:#ddd;
    font-family:Arial, Helvetica, sans-serif;
}
.btn {
    background-color:663333;
    color: white;
    padding: 16px 20px;
    border: none;
    cursor: pointer;
    width: 20%;
    opacity: 0.9;
    border-radius: 5px;
}

.btn:hover {
    opacity: 1;
}
</style>
</head>
<body>
<font>Please provide the information of quantity of food left with you.We will send the message to the organizations along with your address and quantity of food left with you.</font>
<form action='foodinfo.py'>
<label>Number of chapatis:</label><br>
<input type='numeric' placeholder='Left chapatis' name='chapati' required><br>
<label>quantity of dal(in Kg's):</label><br>
<input type='numeric' placeholder='dal quantity' name='dal' required><br>
<label>quantity of rice(in Kg's):</label><br>
<input type='numeric' placeholder='rice quantity' name='rice' required><br>
<label>quantity of vegetables(in Kg's):</label><br>
<input type='numeric' placeholder='vegetable quantity' name='vegi' required><br>
<button type="submit" class="btn">send sms</button>
</form>
</body>
</html>
''')  
