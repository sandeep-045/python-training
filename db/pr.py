import mysql.connector 
dbc = mysql.connector.connect(host="localhost",user="root",password="12345678",database="practice")

dbcursor=dbc.cursor()

query="select * from student;"

dbcursor.execute(query)

for i in dbcursor.fetchall():
	print(i[0])

dbc.close()