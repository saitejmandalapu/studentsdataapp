import sqlite3,cgi
print("Content-Type:text/html\r\n\r\n")
conn=sqlite3.connect("mydatadb.db")
cur=conn.cursor()
form=cgi.FieldStorage()
emp_id=form.getvalue("emp_id")
query="select * from emplyee where emp_id="+emp_id
try:
	cur.execute(query)
except Exception as e:
	print(e)
else:
	for record in cur:
		pass
	html='''<html>
	<body>
	<form action="update.py" method="PUT">
	<input type="text" value="%s" name="emp_id"><br/>
	<input type="text" value="%s" name="emp_name"><br/>
	<input type="text" value="%s" name="department"><br/>
	<input type="submit" value="Update" >
	</form>
	</body>
	</html>'''%(str(record[0]),record[1],record[2])
	print(html)
finally:
	conn.close()
	cur.close()
