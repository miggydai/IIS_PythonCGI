from xml.dom.minidom import parse
import xml.dom.minidom
from xml.dom.minidom import parseString
from xml.etree.ElementTree import ElementTree
import cgi, cgitb
import xml.etree.ElementTree as ET
import os
from http import cookies

cid=""
pics=""
name=""
email=""

#cookies
if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    mycookie=cookies.SimpleCookie()
    mycookie.load(cookie_string)
    try:
        name = mycookie['Name'].value
        email = mycookie['email'].value
        pics = mycookie['pics'].value
        cid = mycookie['cid'].value
        #print("Content-Type: text/html\n")
        #print(a+admin)
        #print("<img src='"+pics+"' width='50px' height='50px' align='right'/>")
        #print(a2)
        
    except KeyError:
        name = ""
        email = ""
        pics = ""

form = cgi.FieldStorage()

pid = form.getvalue('pid')
cID = form.getvalue('cid')



if cID != "" and pid!="":
    file = "orders.xml"
    xmlTree = ET.parse(file)
    rootElement = xmlTree.getroot()
    for element in rootElement.findall('customer'):
        if element.find('cid').text == cID and element.find('pid').text==pid and element.find('status').text == "pending":
            element.find('status').text ="served"
    xmlTree.write(file, encoding="UTF-8",xml_declaration= True)



DOMTree = xml.dom.minidom.parse("orders.xml")
collection = DOMTree.documentElement
print("Content-Type: text/html\n")

a="""
<head>
    <title></title>
    <link rel="stylesheet" href="jquery.dataTables.min.css" />
    <style>
        .hr:hover {
    background-color:lightgreen;
}
        tr.g {
    background:repeating-linear-gradient(90deg,white 0%, green 100%);
}
    </style>
    <script type="text/javascript" src="jquery-3.6.0.min.js"></script>
    <script type="text/javascript" src="jquery.dataTables.min.js"></script>
     <script>
        $(document).ready(function () {
            $('.myTable').DataTable();
             });
        </script>
</head>
"""
print(a)
print("<body>")
order = collection.getElementsByTagName("customer")
print("<table class='myTable table table-bordered table-striped'>")
print("<thead><tr class='g'><td>Customer  ID</td><td>Product ID</td><td>Product Category</td><td>Product Name</td><td>Product Price</td><td>Quantity</td><td>Date Ordered</td><td>Status</td></tr></thead>")
for o in order:
    status = o.getElementsByTagName('status')[0]
    if status.childNodes[0].data =="pending":
        print("<tr class='hr'>")
        
        CID = o.getElementsByTagName('cid')[0]
        print("<td>"+CID.childNodes[0].data + "</td>")

        PID = o.getElementsByTagName('pid')[0]
        print("<td>"+PID.childNodes[0].data + "</td>")

        cat = o.getElementsByTagName('cat')[0]
        print("<td>"+cat.childNodes[0].data + "</td>")

        name = o.getElementsByTagName('name')[0]
        print("<td>"+name.childNodes[0].data + "</td>")

        price = o.getElementsByTagName('price')[0]
        print("<td>"+price.childNodes[0].data + "</td>")

        quan = o.getElementsByTagName('quan')[0]
        print("<td>"+quan.childNodes[0].data + "</td>") 

        date = o.getElementsByTagName('date')[0]
        print("<td>"+date.childNodes[0].data + "</td>")

        print("<td>" + "<a href=orders.py?cid=" + CID.childNodes[0].data + "&pid=" + PID.childNodes[0].data + ">served</a>" + "</td>")

        print("</tr>")

print("</table>")
print("</body>")
