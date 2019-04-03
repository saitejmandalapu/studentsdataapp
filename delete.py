import sqlite3,cgi
print("Content-Type:text/html\r\n\r\n")
conn=sqlite3.connect("mydatadb.db")
cur=conn.cursor()
form=cgi.FieldStorage()
emp_id=form.getvalue("emp_id")
query="delete from emplyee where emp_id="+emp_id
try:
	cur.execute(query)
except Exception as e:
	print(e)
else:
	conn.commit()
	print("deleted successfully")
finally:
	conn.close()
	cur.close()
