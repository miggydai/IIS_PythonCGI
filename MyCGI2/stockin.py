print("Content-Type: text/html\n")
print("<body>")
a="""
<iframe src ="side.py" name="C" height ="20000" width ="20%" frameborder="0" ></iframe>
<iframe src ="page.py" name="D" height ="20000" width ="75%" frameborder="0" ></iframe>
"""
print(a)
print("</body>")