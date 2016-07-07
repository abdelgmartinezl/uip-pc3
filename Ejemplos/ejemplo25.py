import pymysql

db = pymysql.connect("192.168.56.2","pepito","pepito","test")

cursor = db.cursor()

email = input("Introduce el email: ")
sql  = "SELECT * FROM users WHERE email = '%s'" % (email)

try:
	cursor.execute(sql)
	resultado = cursor.fetchall()
	for fila in resultado:
		id = fila[0]
		email = fila[1]
		password = fila[2]
		print(id, email, password)
except:
	print("Error: no se obtuvo data")

db.close()

