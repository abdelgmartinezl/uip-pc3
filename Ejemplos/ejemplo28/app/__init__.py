from model.Participante import Participante

if __name__ == "__main__":
    listaParticipantes = []
    while (True):
        print("\n\nASISTENCIA EVENTO")
        print("1. Ingresar participante")
        print("2. Ver estadisticas")
        print("3. Ver todos los participantes")
        print("4. Salir")
        try:
            opc = int(input("OPCION> "))
        except:
            opc = 0

        if opc == 1:
            print("\nINGRESAR PARTICIPANTE")
            nombre = input("Nombre: ") #FALTA VALIDAR
            while (True):
                try:
                    edad = int(input("Edad: "))
                except:
                    edad = 0
                if edad > 0:
                    break
                else:
                    print("ERROR :: Edad no valida")
            while (True):
                sexo = input("Sexo(M/F): ").upper()
                if sexo == "M" or sexo == "F":
                    break
                else:
                    print("ERROR :: Sexo no valido")
            participante = Participante(nombre, edad, sexo)
            listaParticipantes.append(participante)
        elif opc == 2:
            print("\nVER ESTADISTICAS")
        elif opc == 3:
            print("\nVER TODOS")
            for p in listaParticipantes:
                p.mostrar()
        elif opc == 4:
            break
        else:
            print("ERROR")