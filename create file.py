import sqlite3,cgi
print("Content-Type:text/html\r\n\r\n")
conn=sqlite3.connect("mydatadb.db")
cur=conn.cursor()
query="create table emplyee(emp_id integer,emp_name text,department text)"
try:
	cur.execute(query)
except Exception as e:
	print(e)
else:
	conn.commit()
	print("created successfully")
finally:
	conn.close()
	cur.close()
