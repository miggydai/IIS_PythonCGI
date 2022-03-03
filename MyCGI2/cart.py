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

tree = ElementTree()
tree.parse('orders.xml')


form = cgi.FieldStorage()

pid = form.getvalue('pid')
quantity = form.getvalue('quan')
cancel = form.getvalue('cancel')



if cancel == "1" and pid !="":
    file3 ="orders.xml"
    xmlTree3=ET.parse(file3)
    root = xmlTree3.getroot()
    for o in root.findall('customer'):
        pID = o.find('pid').text
        c = o.find('cid').text
        if cid == c and pID == pid:
            root.remove(o)
            print("Content-Type: text/html\n")
            print("<meta http-equiv='refresh' content='0; url=cart.py'/>")
    xmlTree3.write(file3, encoding="UTF-8", xml_declaration=True)

elif quantity != "" and pid!="":
    file = "orders.xml"
    xmlTree = ET.parse(file)
    rootElement = xmlTree.getroot()
    for element in rootElement.findall('customer'):
        if element.find('quan').text == quantity and element.find('pid').text==pid and element.find('status').text == "cart":
            element.find('status').text ="pending"
    xmlTree.write(file, encoding="UTF-8",xml_declaration= True)

    file2="mother.xml"
    xmlTree2 = ET.parse(file2)
    rootElement2 = xmlTree2.getroot()
    for elementt in rootElement2.findall('product'):
        if elementt.find('pid').text == pid:
            elementt.find('quan').text = str(int(elementt.find('quan').text) - int(quantity))
            print("Content-Type: text/html\n")
            print("<meta http-equiv='refresh' content='0; url=cart.py'/>")
    xmlTree2.write(file2, encoding="UTF-8", xml_declaration= True)






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
print("<p style='text-align:center;'>Shopping Cart</p>")
print("<table class='myTable table table-bordered table-striped'>")
print("<thead><tr class='g'><td>Customer ID</td><td>Product ID</td><td>Product Category</td><td>Product Name</td><td>Product Price</td><td>Quantity</td><td>Date Ordered</td><td>Checkout</td><td>  </td></tr></thead>")
for o in order:
    status = o.getElementsByTagName('status')[0]
    cID = o.getElementsByTagName('cid')[0]
    if status.childNodes[0].data =="cart" and cID.childNodes[0].data==cid:
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

        print("<td>" + "<a href=cart.py?quan=" + quan.childNodes[0].data + "&pid=" + PID.childNodes[0].data + ">checkout</a>" + "</td>")
        print("<td>" + "<a href=cart.py?cancel=" + "1" + "&pid=" + PID.childNodes[0].data + ">cancel</a>" + "</td>")

        print("</tr>")

print("</table>")
print("</body>")
