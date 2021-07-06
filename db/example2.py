import mysql.connector as mc

dbcon=mc.connect(host="localhost",user="root",password="12345678",database="practice")

dbcursor=dbcon.cursor()

dbcursor.execute("SELECT * FROM gym	;")

for i in dbcursor.fetchall():
	print(*i,sep="\t\t")
