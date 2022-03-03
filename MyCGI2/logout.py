from http import cookies
import cgi, cgitb
import os

name = ""
email = ""
pics = ""

if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    mycookie=cookies.SimpleCookie()
    mycookie.load(cookie_string)
    try:
        name=mycookie['Name'].value
        email = mycookie['email'].value
        pics = mycookie['pics'].value
        
    except KeyError:
        name = ""
        email = ""


expire = 0
mycook = cookies.SimpleCookie()

mycook['Name'] = name
mycook['email'] = email
mycook['pics'] = pics
mycook['Name']['expires'] = expire
mycook['email']['expires'] = expire
mycook['pics']['expires'] = expire

print(mycook)
print("Content-Type: text/html\n")
print("<script>window.location.replace('http://localhost/index.py');</script>")