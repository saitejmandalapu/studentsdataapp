import sqlite3,cgi
print("Content-Type:text/html\r\n\r\n")

conn=sqlite3.connect("mydatadb.db")
cur=conn.cursor()
form=cgi.FieldStorage()
emp_id=form.getvalue("emp_id")
emp_name=form.getvalue("emp_name")
department=form.getvalue("department")
print(emp_id,emp_name,department)
sql="update emplyee SET emp_id='"+emp_id+"' ,emp_name='"+emp_name+"' ,department='"+department+"' where emp_id="+emp_id
print(sql)
try:
	rs=cur.execute(sql)
	
except Exception as e:
	print("Exception ")
	print(e)
else:
	conn.commit()
	print("Updated  Succesfully")
conn.close()
cur.close()
