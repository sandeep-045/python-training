import mysql.connector as mc

dbcon=mc.connect(host="localhost",user="root",password="12345678",database	="practice")


dbcursor=dbcon.cursor()

db.execute("select * from gym order by id ")

