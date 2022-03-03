import xml.etree.ElementTree as ET
import cgi, cgitb
form = cgi.FieldStorage()
import string
import random
import os
import image

from datetime import date

today = date.today()

n=form.getvalue('number')
ad=form.getvalue('address')
dd= today.strftime("%d/%m/%Y")
capy = form.getvalue('capcap')
capupu = form.getvalue('ca')

image_info = image.ImageCaptcha(width=200, height=100)
def id_generator(size=5, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#appendxml
def write():
    id=0
    tree = ET.parse('customers.xml')
    root = tree.getroot()
    for type_tag in tree.findall('details'):
        id=id+1

    b = ET.SubElement(root, 'details')
    cid = ET.SubElement(b, 'cid')
    cid.text = str(id+1)
    email = ET.SubElement(b, 'email')
    email.text = ad
    num = ET.SubElement(b, 'pass')
    num.text = n
    date = ET.SubElement(b, 'date')
    date.text = dd
    
    b_xml=ET.tostring(root)

    with open("customers.xml", "wb") as f:
        f.write(b_xml)


a="""
    <head>
        <title></title>
        <link rel="stylesheet" href="StyleSheet.css" />
         <script type="text/javascript">

        function chk() {
            var phone = document.getElementById("p").value;
            var email = document.getElementById("E").value;
            var passw = document.getElementById("pis").value;

            if (phone == "") {
                alert("Invalid!");
            } else if (email == "") {
                alert("Invalid!");
            } else if (passw == "") {
                alert("Invalid!");
            } else {
                alert("Welcome!!");
            }

        }
    </script>
    </head>
    <body>
        <div class="signin">
        <form method ="post" action="signin.py" name='signin'>
            <p class="log">Sign Up</p>
            <div class="user"><input type="text" class="a" id="p" required/><label>Phone #</label></div>
            <div class="password"><input type="text" class="a" id="E" name="address" required/><label>Email</label></div>
            <div class="new"><input type="text" class="a" id="pis" name="number" required/><label>Password</label></div>
           <div id='verify'><input type="text" class="a" name="capcap"required/><label>Enter Text</label></div>
            
"""

b="""
 <div class="sbuts"> <input type="submit" name="submit_button" value=Submit /></div>
        </div>
        </form>
    </body>
"""

if not n and not ad:
    captcha_text = id_generator()
    source = image_info.generate(captcha_text)
    image_info.write(captcha_text, captcha_text +'Captcha.png')
    print("Content-Type: text/html\n")
    print(a)
    print("<img src="+"'"+captcha_text+"Captcha.png"+"' class='captcha' />")
    print("<input class='auto-style4' type='hidden' name='ca' value='"+captcha_text+"' required />")
    print(b)
    

elif capupu == capy:
    print("Content-Type: text/html\n")
    c="""
        <head>
        <title></title>
        <link rel="stylesheet" href="StyleSheet.css" />
        <script type ="text/javascript">
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
        <form name="login" action='signin.py'>
        <p class="log">Login</p>
        <div class="user"><input type="text" class="a"  id="user"/><label>username</label></div>
         <div class="password"><input type="text" class="a" id="pass" /><label>password</label></div>
        <div id="sign"><p>New Here?</p> <a href="signin.py" class="links" target="B">Sign up</a></div>
        <div class="buts"><button onclick ="check()">Login</button></div>
        </form>
        </div>
    </body>
    """
    print(c)
    write()
    os.remove(capy+"Captcha.png")
    

elif capupu != capy:
    os.remove(capupu +'Captcha.png')
    captcha_text = id_generator()
    source = image_info.generate(captcha_text)
    image_info.write(captcha_text, captcha_text +'Captcha.png')
    print("Content-Type: text/html\n")
    print(a)
    print("<img src="+"'"+captcha_text+"Captcha.png"+"' class='captcha' />")
    print("<input type='hidden' name='ca' value='"+captcha_text+"' required />")
    print(b)



    


    
    



