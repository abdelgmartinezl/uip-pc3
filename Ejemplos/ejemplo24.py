import pymysql

con = pymysql.connect(host='192.168.56.2', user='pepito', passwd='pepito', db='test')
cur = con.cursor()
cur.execute("SELECT * FROM users")
print(cur.description)
print()

for fila in cur:
	print(fila)

cur.close()
con.close()
