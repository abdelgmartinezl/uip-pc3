import sqlite3

con = sqlite3.connect('puntaje.sqlite')
c = con.cursor()

try:
    c.execute('CREATE TABLE puntuacion (id STRING PRIMARY KEY, puntos INTEGER);')
    con.commit()
except:
    print("Ya existe la tabla moh")

while True:
    print("1. Registrar puntos")
    print("2. Ver top 3")
    print("3. Salir")
    try:
        opcion = int(input("Opcion: "))
        if opcion == 1:
            id = input("ID: ")
            puntos = int(input("PUNTOS: "))
            c.execute('SELECT id FROM puntuacion WHERE id = {i};'.format(i=id))
            existe = c.fetchone()
            if len(existe) != 0:
                c.execute("UPDATE puntuacion SET puntos = {p} WHERE id = {i}".format(p=puntos
                                                                                     , i=id))
            else:
                c.execute('INSERT INTO puntuacion VALUES({i}, {p});'.format(i=id, p=puntos))
        elif opcion == 2:
            c.execute('SELECT id, puntos FROM puntuacion ORDER BY puntos DESC LIMIT 3;')
            top = c.fetchall()
            print(top)
            con.commit()
        elif opcion == 3:
            break
        else:
            print("Error: Opcion invalida")
    except:
        print("Error: Opcion invalida")

con.close()