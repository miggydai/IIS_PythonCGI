from xml.dom.minidom import parse
import xml.dom.minidom
from http import cookies
import cgi, cgitb
import os
import xml.etree.ElementTree as ET
import datetime
from datetime import date
import xml.dom.minidom

form = cgi.FieldStorage()

pid = form.getvalue('pid')
pcat = form.getvalue('cat')
pname = form.getvalue('pname')
price = form.getvalue('price')
quantity = form.getvalue('quantity')

cid=""
pics=""
name=""
email=""

if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    mycookie = cookies.SimpleCookie()
    mycookie.load(cookie_string)
    try:
        cid=mycookie['cid'].value
        pics=mycookie['pics'].value
        name = mycookie['Name'].value
        email = mycookie['email'].value
    except KeyError:
        pics=""
        name=""
        email=""

if cid == "":
    print("Content-Type: text/html\n")
    print("<meta http-equiv='refresh' content='0; url=login.py' />")

if pid != None and cid != "":
    DOMTree = xml.dom.minidom.parse('orders.xml')
    collection = DOMTree.documentElement
    orders = collection.getElementsByTagName("customer")

    auth = "False"

    for order in orders: #check if pid cid and status(cart) exists in orders

        custid = order.getElementsByTagName('cid')[0]
        cust_id = custid.childNodes[0].data

        custpid = order.getElementsByTagName('pid')[0]
        cust_pid = custpid.childNodes[0].data

        cust_stat = order.getElementsByTagName('status')[0]
        custStatus = cust_stat.childNodes[0].data

        if pid==cust_pid and cid==cust_id and custStatus=="cart":
            auth="True"
    
    if auth=="True":
        # append modify xml
        file = "orders.xml"
        xmlTree = ET.parse(file)
        rootElement = xmlTree.getroot()
        for element in rootElement.findall("customer"):
            if element.find('cid').text == cid and element.find('pid').text == pid and element.find('status').text == "cart":
                element.find('quan').text = str(int(element.find('quan').text) + int(quantity))
            
        xmlTree.write(file,encoding='UTF-8',xml_declaration=True)
        #append/modify xml
        print("Content-Type: text/html\n")
        print("<meta http-equiv='refresh' content='0; url=bottom.html' />")

    if auth =="False":
        id=0

        tree = ET.parse("orders.xml")
        root = tree.getroot()
        for type_tag in tree.findall('customer'):
            id= id +1
        b = ET.SubElement(root, 'customer')
        custid = ET.SubElement(b, 'cid')
        custid.text = cid

        custpid = ET.SubElement(b, 'pid')
        custpid.text = pid

        custpcat = ET.SubElement(b, 'cat')
        custpcat.text = pcat

        custpname = ET.SubElement(b, 'name')
        custpname.text = pname

        custprice = ET.SubElement(b, 'price')
        custprice.text = price

        custquan = ET.SubElement(b, 'quan')
        custquan.text = quantity

        custdate = ET.SubElement(b, 'date')
        custdate.text = str(date.today())

        custstatus = ET.SubElement(b, 'status')
        custstatus.text = "cart"

        b_xml=ET.tostring(root)

        with open("orders.xml", "wb") as f:
            f.write(b_xml)
        print("Content-Type: text/html\n")
        print("<meta http-equiv='refresh' content='0; url=bottom.html' />")
        


