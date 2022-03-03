from http import cookies
import cgi, cgitb

form = cgi.FieldStorage()

pics = form.getvalue('pics')
name = form.getvalue('name')
email = form.getvalue('email')

expires = 60*60;
mycookie = cookies.SimpleCookie()

mycookie["Name"] = name
mycookie["email"] =  email
mycookie["pics"] =  pics
mycookie["email"]['expires']= expires

print (mycookie)
print( "Content-type:text/html\n");
print( "<script>window.close();</script>");

