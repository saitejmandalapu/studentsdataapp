import sqlite3,cgi
print("Content-Type:text/html\r\n\r\n")

conn=sqlite3.connect("mydatadb.db")
cur=conn.cursor()
form=cgi.FieldStorage()
emp_id=form.getvalue("emp_id")
emp_name=form.getvalue("emp_name")
department=form.getvalue("department")
print(emp_id,emp_name,department)
sql="insert into emplyee values('"+emp_id+"','"+emp_name+"','"+department+"')"
print(sql)
try:
        #cur.execute("create table emp(emp_id integer,emp_name text,department text)")
        rs=cur.execute(sql)
except Exception as e:
        print("Exception")
        print(e)
else:
        conn.commit()
        print("succesfully inserted")
conn.close()
cur.close()
