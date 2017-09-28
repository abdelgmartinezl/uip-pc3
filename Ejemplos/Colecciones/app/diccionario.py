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