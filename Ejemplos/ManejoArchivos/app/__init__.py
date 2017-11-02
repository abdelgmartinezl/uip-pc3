import re

if __name__ == "__main__":
    dias = open('dias.txt', 'r')
    try:
        ciao = open('adios.txt', 'x')
    except FileExistsError:
        ciao = open('adios.txt', 'w')
    #print(dias.read()) # Imprime todo
    #print(dias.readline()) # Imprime linea por linea (lunes)
    #print(dias.readline()) # Imprime linea por linea (martes)
    #print(dias.readlines())
    for dia in dias.readlines():
        patron = "Miercoles"
        if re.match(patron, dia):
            print("Vamos pa lante")
            ciao.write("Ciao")

    ciao.close()
    dias.close()