from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("customers.xml")
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
customers = collection.getElementsByTagName("details")
print("<table class='myTable table table-bordered table-striped'>")
print("<thead><tr class='g'><td>Customer  ID</td><td>Email</td><td>Password</td><td>Date Registered</td></tr></thead>")
for c in customers:
    print("<tr class='hr'>")

    cid = c.getElementsByTagName('cid')[0]
    print("<td>"+cid.childNodes[0].data + "</td>")

    email = c.getElementsByTagName('email')[0]
    print("<td>"+email.childNodes[0].data + "</td>")

    num = c.getElementsByTagName('pass')[0]
    print("<td>"+num.childNodes[0].data + "</td>")

    date = c.getElementsByTagName('date')[0]
    print("<td>"+date.childNodes[0].data + "</td>")

    print("</tr>")
print("</table>")
print("</body>")