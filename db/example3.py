import mysql.connector as mc

dbcon=mc.connect(host="localhost",user="root",password="12345678",database="practice")

dbcursor=dbcon.cursor() # pass buffered=True as positional argument if it does not work:

# dbcursor.execute("use practice;")
# dbcursor.execute("select * from gym order by id desc;")
# dbcursor.execute("select * from gym where name like 's%';")
dbcursor.execute("select * from gym group by age;")

print(*dbcursor.fetchall(),sep="\n")
