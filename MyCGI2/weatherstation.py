import cgi, cgitb
import mysql.connector
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4
import matplotlib.pyplot as plt5
import matplotlib.pyplot as plt6
from datetime import datetime

form = cgi.FieldStorage()

now = datetime.now()

date_time = now.strftime("%m/%d/%Y, %H:%M %p");

maximum = 59;

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="AyayaMeg0521!",
  database="arduino" 
)

xAxis = []
yAxis = []

mycursor = mydb.cursor()

mycursor.execute("select * from weatherdata;")
myresult = mycursor.fetchall()

noDupe = []

for x in range(len(myresult)):
        if myresult[x] not in noDupe:
            noDupe.append(myresult[x])        

for row in noDupe:
        time1 = row[6]
        time2 = time1.strftime("%H:%M:%S")
        time3 = time2[6:]
        tempC = row[4]
        yAxis.append(float(tempC))
        if time3 not in xAxis:
            xAxis.append(int(time3))
        if maximum in xAxis:
            xAxis.clear()
            yAxis.clear()

fig = plt.figure()

axl = fig.add_subplot(1,1,1)

axl.clear()

axl.plot(xAxis, yAxis, 'g-', label='Celsius')

plt.axis([0, 60, 0, 100])

axl.axhspan(0, 30, facecolor="white", alpha=0.5)
axl.axhspan(30, 35, facecolor="green", alpha=0.5)
axl.axhspan(35, 45, facecolor="yellow", alpha=0.5)
axl.axhspan(45, 60, facecolor="orange", alpha=0.5)
axl.axhspan(60, 100, facecolor="red", alpha=0.5)

plt.title("Temperature Weather Station")
plt.ylabel("Celsius", fontweight="bold")
plt.xlabel(date_time, fontweight="bold")

plt.legend()
plt.savefig("celcius.png")

print("Content-Type: text/html\n")
    
a = """
    <head>
        <title></title>
        <link rel="stylesheet" href="StyleSheet.css"/>
        <script type="text/javascript" src="script.js"></script>
        <script>
            
        </script>
        <style>
            .tempGraph {
                
            }
            .tempDesc {
                position: relative;
                left: 700px;
                bottom: 400px;
            }
                    
            .humGraph {
                
            }
            .humDesc {
                position: relative;
                left: 700px;
                bottom: -200px;
            }
            
            .apGraph {
                
            }
            .apDesc {
                position: relative;
                left: 700px;
                bottom: -1200px;
            }
            
            .wsGraph {
                
            }
            .wsDesc {
                position: relative;
                left: 700px;
                bottom: -1600px;
            }
            
            .wlGraph {
                
            }
            .wlDesc {
                position: relative;
                left: 700px;
                bottom: -700px;
            }
        </style>
    </head>
    <body>
        <div class="tempGraph">
            <img src="temperature.png">
        </div>
        <div class="tempDesc">
    """
print(a)

if int(noDupe[-1][4]) >= 30 and int(noDupe[-1][4]) < 35:
        print("<p>Caution: Heat Warning</p>")
elif int(noDupe[-1][4]) >= 35 and int(noDupe[-1][4]) < 45:
        print("<p>Caution: Medium Heat Warning</p>")
elif int(noDupe[-1][4]) >= 45 and int(noDupe[-1][4]) < 60:
        print("<p>Caution: Excessive Heat Warning</p>")
elif int(noDupe[-1][4]) >= 60 and int(noDupe[-1][4]) < 101:
        print("<p>Caution: Extreme Heat Warning</p>")
else:
        print("<p>Caution: Cold Weather!</p>")
b ="""
</div>
</body>
"""
print(b)