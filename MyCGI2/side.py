from xml.dom.minidom import parse
import xml.dom.minidom
from http import cookies
import xml.etree.ElementTree as ET
import datetime
from datetime import date
import xml.dom.minidom
import cgi, sys, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

print('Content-type: text/html')
sys.path.insert(0, os.getcwd())

pid = form.getvalue('prodid')
cat = form.getvalue('pcat')
Name = form.getvalue('pname')
price = form.getvalue('pp')
quan = form.getvalue('q')
message = None
auth = "False"
if 'filename' in form:
    fileitem = form['filename']
    fn = os.path.basename(fileitem.filename)
    open(fn, 'wb').write(fileitem.file.read())
    message = 'The file "' + fn + '" was uploaded successfully'
    auth="True"
    if pid!="" and Name!= "" and auth=="True":
        id=0

        tree = ET.parse("mother.xml")
        root = tree.getroot()
        for type_tag in tree.findall('product'):
            id= id +1
        b = ET.SubElement(root, 'product')

        custpid = ET.SubElement(b, 'pid')
        custpid.text = pid

        custpname = ET.SubElement(b, 'name')
        custpname.text = Name

        custpcat = ET.SubElement(b, 'cat')
        custpcat.text = cat

        picture = ET.SubElement(b, 'pic')
        picture.text = fn

        custprice = ET.SubElement(b, 'price')
        custprice.text = price

        custquan = ET.SubElement(b, 'quan')
        custquan.text = quan

        custdate = ET.SubElement(b, 'date')
        custdate.text = str(date.today())


        b_xml=ET.tostring(root)

        with open("mother.xml", "wb") as f:
            f.write(b_xml)
        
    
else:
    message = 'No file was uploaded'

a="""
<title></title>
     <link rel="stylesheet" href="StyleSheet.css" />
</head>
<body>
    <form enctype = "multipart/form-data" action = "side.py" method = "post">
    <div class="stock">
        <p class="log">Stock In</p>
        <div id="pid"><input type="text" class="a" name="prodid"/><label>Product ID</label></div>
         <div id="category"><input type="text" class="a" name="pcat" /><label>Product Category</label></div>
        <div class="prod"><input type="text" class="a" name="pname" /><label>Product Name</label></div>
        <div class="prodi"><input type="text" class="a" name="pp"/><label>Product Price</label></div>
        <div class="last"><input type="text" class="a" name="q" /><label>Quantity</label></div>
        <p class="file"><input type="file" name="filename" /></p>
        <div class="submit"><input type="submit" value="Upload" name=action /></div>
        </form>
</body>
"""
#print("Content-Type: text/html\n")
print(a)

