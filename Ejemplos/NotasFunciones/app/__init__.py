notas = []


def menu():
    print("\nSISTEMA DE NOTAS\n")
    print("1. Ingresar nota")
    print("2. Cambiar nota")
    print("3. Ver notas")
    print("4. Estado final")
    print("5. Salir")
    while True:
        try:
            opcion = int(input("\nOPCION > "))
        except:
            opcion = -1
        if opcion < 1 or opcion > 5:
            print("Opcion invalida")
        else:
            return opcion
            break


def orquestar(o):
    if o == 1:
        ingresar()
    elif o == 2:
        cambiar()
    elif o == 3:
        ver()
    elif o == 4:
        calcular()
    else:
        exit(0)


def ingresar():
    while True:
        try:
            nota = int(input("\nDigite la nota: "))
        except:
            nota = -1
        if nota < 0 or nota > 100:
            print("Nota invalida")
        else:
            notas.append(nota)
            break


def ver():
    print("\nNOTAS")
    for nota in notas:
        print(nota)


def cambiar():
    i = 1
    print("\nNOTAS")
    for nota in notas:
        print(str(i) + ". " + str(nota))
        i = i + 1
    while True:
        try:
            c = int(input("\nDigite el numero de nota a cambiar: "))
        except:
            c = -1
        if c < 0 or c > len(notas):
            print("Numero invalido")
        else:
            break
    while True:
        try:
            n = int(input("Digite la nueva nota: "))
        except:
            n = -1
        if n < 0 or n > 100:
            print("Nota invalida")
        else:
            break
    notas[c-1] = n


def calcular():
    final = 0
    for nota in notas:
        final += nota
    promedio = final/len(notas)
    print("Tu promedio es " + str(promedio))

    if promedio > 90:
        print("A")
    elif promedio > 80:
        print("B")
    elif promedio > 70:
        print("C")
    else:
        print("F")


if __name__ == "__main__":
    while True:
        orquestar(menu())
