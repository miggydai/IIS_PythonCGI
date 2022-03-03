from http import cookies
import cgi, cgitb
from xml.dom.minidom import parse
import xml.dom.minidom
import os

form = cgi.FieldStorage()

name = form.getvalue('name')
passw = form.getvalue('pass')

DOMTree = xml.dom.minidom.parse("customers.xml")
collection = DOMTree.documentElement
customers = collection.getElementsByTagName("details")

auth = "False"

for c in customers:
    cid = c.getElementsByTagName('cid')[0]
    CID = cid.childNodes[0].data

    email = c.getElementsByTagName('email')[0]
    uname = email.childNodes[0].data

    password = c.getElementsByTagName('pass')[0]
    upass = password.childNodes[0].data

    if name == uname and passw == upass:
        expires = 60*60
        mycookie = cookies.SimpleCookie()
        mycookie['cid'] = CID
        mycookie['Name'] = uname
        mycookie["Color"] = "red"
        mycookie["email"] = uname
        mycookie["pics"] = "haha.jpg"
        mycookie["email"]["expires"] = expires
        print(mycookie)

        print("Content-type:text/html\n")
        print("<meta http-equiv='refresh' content='0; url=http://localhost/index.py'/>")
        auth="True"

if name != uname and passw != upass and name != None:
    auth="False"
    print("Content-type:text/html\n")
else:
    auth="NA"

print("Content-type:text/html\n")
a="""
<head>
    <title></title>
    <link rel="stylesheet" href="StyleSheet.css" />
    <script type ="text/javascript">

        function openWin(){
            myWindow = window.open('http://127.0.0.1:8080/login','name','width=600,height=600')

        }
         
        function check() {
            var user = document.getElementById("user").value;
            var pass = document.getElementById("pass").value;

            if (user == "") {
                alert("Invalid!!");
            } else if (pass == "") {
                alert("Invalid!!");
            } else {
                alert("Welcome");
            }

        }
    </script>
</head>
<body>
    <div class="login">
    <form name="login" action="login.py" method="post">
        <p class="log">Login</p>
        <div class="user"><input type="text" class="a" name="name" id="user"/><label>username</label></div>
         <div class="password"><input type="text" class="a" name ="pass" id="pass" /><label>password</label></div>
        <div id="sign"><p>New Here?</p> <a href="signin.py" class="links" target="B">Sign up</a></div>
        <div class="gmail"><img src="google-signin-button.png"  onclick=openWin()> </div>
        <div class="buts"><input type = "submit" value ="Login" id="submit" /></div>
        </form>
    </div>
</body>
"""
print(a)
if auth == "False":
    print("Customer not found :(" )
