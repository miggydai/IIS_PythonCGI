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
delete = form.getvalue('delete')

if delete == "1" and pid!= "":
    file = "mother.xml"
    xmlTree=ET.parse(file)
    root = xmlTree.getroot()
    for o in root.findall('product'):
        pID = o.find('pid').text
        if pID == pid:
            root.remove(o)
            print("Content-Type: text/html\n")
            print("<meta http-equiv='refresh' content='0; url=page.py'/>")
    xmlTree.write(file,encoding="UTF-8", xml_declaration=True)


DOMTree = xml.dom.minidom.parse("mother.xml")
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
mother = collection.getElementsByTagName("product")
print("<table class='myTable table table-bordered table-striped'>")
print("<thead><tr class='g'><td>Product ID</td><td>Product Category</td><td>Product Name</td> <td>Picture</td> <td>Product Price</td><td>Quantity</td><td>Date</td><td> </td></tr></thead>")
for m in mother:
    print("<tr class='hr'>")
    PID = m.getElementsByTagName('pid')[0]
    print("<td>"+PID.childNodes[0].data + "</td>")

    cat = m.getElementsByTagName('cat')[0]
    print("<td>"+cat.childNodes[0].data + "</td>")

    name = m.getElementsByTagName('name')[0]
    print("<td>"+name.childNodes[0].data + "</td>")

    pic=m.getElementsByTagName('pic')[0]
    print("<td><img src ='"+pic.childNodes[0].data+"' width='100' height='100' /></td>")

    price = m.getElementsByTagName('price')[0]
    print("<td>"+price.childNodes[0].data + "</td>")

    quan = m.getElementsByTagName('quan')[0]
    print("<td>"+quan.childNodes[0].data + "</td>")

    date = m.getElementsByTagName('date')[0]
    print("<td>"+date.childNodes[0].data + "</td>")

    print("<td>" + "<a href=page.py?delete=" + "1" + "&pid=" + PID.childNodes[0].data + ">delete</a>" + "</td>")

    print("</tr>")
print("</table>")
print("</body>")