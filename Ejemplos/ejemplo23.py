import pymysql.cursors

conexion = pymysql.connect(host='192.168.56.2',
                          user='pepito',
                          password='pepito',
                          db='test',
                          cursorclass=pymysql.cursors.DictCursor)

try:
	with conexion.cursor() as cursor:
		sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
		cursor.execute(sql, ('webmaster@example.com', 'super-secreto'))
	conexion.commit()

	with conexion.cursor() as cursor:
		sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
		cursor.execute(sql, ('webmaster@example.com',))
		resultado = cursor.fetchone()
		print(resultado)
finally:
	conexion.close()
