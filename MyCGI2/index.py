from http import cookies
import cgi, cgitb
import os

form = cgi.FieldStorage()
logout= form.getvalue('logout')

#if statement logout
if logout == "yes":
    expires=0
    mycookie = cookies.SimpleCookie()
    mycookie['cid'] = ""
    mycookie['Name'] = ""
    mycookie['Color'] = ""
    mycookie['email'] = ""
    mycookie['pics'] = ""
    mycookie['cid']['expires']=expires
    mycookie['email']['expires']=expires
    print(mycookie)
    print("Content-Type: text/html\n")
    print("<meta http-equiv='refresh' content='0; url=http://localhost/index.py' />")
else:
    print("Content-Type: text/html\n")
    
name = ""
email = ""
pics= ""
cid = ""
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
        
        
    except KeyError:
        name = ""
        email = ""
        pics = ""
#else:
    #print("Content-Type: text/html\n")
    #print(a+notlogin+defaultPic+a2)

a="""
<head>
    <title></title>
     <link rel="stylesheet" href="StyleSheet.css" />
     <script src="jquery-3.6.0.min.js"></script>
     <script>
       function resizeIframe() {
                var myFrame = $("iframe");
                myFrame.contents().find('#submit').click(function() {
                $("iframe").on("load", function () {
                    location.reload();
                    );
                });
            }
     </script>
</head>
<body>
     <div class="header">
"""

        # <div id="link"> <a href="login.html" class="links" target="B">Login</a> <a href="signin.py" class="links" target="B">Register</a> </div>
        #
        #  <img src="haha.jpg" width="50px" height="50px" align="right"/>

a2="""
          <div>
              <a href="index.py"><img src="me.jpg" id="image"></a>
              <div class="center"><input type="text"  /><label>search product</label></div>
              <img src="shop.png" class="right" usemap="#shop">

             <map name="shop">
             <area shape="rect" coords="31,57,415,411" href="cart.py" target="B">
             </map>

          </div>
          
      </div>
      <div>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <iframe src ="bottom.html" name="B" height="300%" width="100%" frameborder="0" scrolling="no" onload="resizeIframe()" ></iframe>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>

      </div>
      
</body>
"""

a3="""
 <div>
              <a href="index.py"><img src="me.jpg" id="image"></a>
              <div class="center"><input type="text"  /><label>search product</label></div>
              <img src="shop.png" class="right" usemap="#shop">

             <map name="shop">
             <area shape="rect" coords="31,57,415,411" href="cart.py" target="B">
             </map>

          </div>
          
      </div>
      <div>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <iframe src ="bottom.html" name="B" height="300%" width="100%" frameborder="0" scrolling="no" ></iframe>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>

      </div>
      
</body>

"""
myPic="<img src='meme.jpg' width='50px' height='50px' align='right'/>"
defaultPic="<img src='haha.jpg' width='50px' height='50px' align='right'/>"
customer="""
 <div id="link"> <a href="MyOrders.py" class="links" target="B">MyOrders</a> <a href="/index.py?logout=yes" class="links" target="B">Logout</a> Welcome Customer</div>
"""
admin="""
 <div id="link"> <a href="stockin.py" class="links" target="B">StockIn</a>  <a href="orders.py" class="links" target="B">Orders</a>  <a href="customers.py" class="links" target="B">Customers</a>  <a href="/index.py?logout=yes" class="links" target="B">Logout</a> Welcome Admin Megs</div>
"""

notlogin="""
  <div id="link"> <a href="login.py" class="links" target="B">Login</a> <a href="signin.py" class="links" target="B">Register</a> </div>
"""
#print("Content-Type: text/html\n")
if email:
    if cid == "1":
        print(a+admin+myPic+a2)        
    else:
        print(a+customer+defaultPic+a2)
else:
    print(a+notlogin+defaultPic+a2)