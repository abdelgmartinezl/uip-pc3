if __name__ == '__main__':
    canicas = {"rojo": 17, "verde": 6, "amarillo": 1}

    print("Yo tengo " + str(canicas['verde']) + " verdes.")

    try:
        print("Yo tengo" + str(canicas['azul']) + " azules.")
    except:
        print("No hay canicas azules.")

    nuevas = int(input("Cuantas canicas rojas compraste: "))
    canicas['rojo'] += nuevas
    print("Ahora tengo " + str(canicas['rojo']) + " rojas.")

    nuevo_color = input("Que color de canica compraste: ")
    nuevas = int(input("Cuantas canicas " + nuevo_color + " son: "))
    if nuevo_color in canicas.keys():
        canicas[nuevo_color] += nuevas
    else:
        canicas[nuevo_color] = nuevas
    print(canicas)

    for color in canicas.keys():
        print(color)

    print("En total son " + str(sum(canicas.values())) + " canicas.")