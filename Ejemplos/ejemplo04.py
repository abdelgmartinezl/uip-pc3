# CLASE 6
# Autor: Abdel G. Martinez L.
#
# Instrucciones: Simular un directorio telefonico

def imprimirNumero(numeros):
    print("Numeros Telefonicos:")
    for k, v in numeros.items():
        print("Nombre:", k, "\tNumero:", v)
    print()

def agregarNumero(numeros, nombre, numero):
    numeros[nombre] = numero

def buscarNumero(numeros, nombre):
    if nombre in numeros:
        return "El numero es " + numeros[nombre]
    else:
        return nombre + " no se encontro."

def borrarNumero(numeros, nombre):
    if nombre in numeros:
        del numeros[nombre]
    else:
        print(nombre," no se encontro.")

def cargarNumeros(numeros, archivo):
    in_file = open(archivo, "rt")
    while True:
        in_line = in_file.readline()
        if not in_line:
            break
        in_line = in_line[:-1]
        nombre, numero = in_line.split(",")
        numeros[nombre] = numero
    in_file.close()

def guardarNumeros(numeros, archivo):
    out_file = open(archivo, "wt")
    for k, v in numeros.items():
        out_file.write(k + "," + v + "\n")
    out_file.close()

def mostrarMenu():
    print('1. Imprimir numeros')
    print('2. Agregar un numero')
    print('3. Eliminar un numero')
    print('4. Buscar un numero')
    print('5. Cargar numeros')
    print('6. Guardar numeros')
    print('7. Salir')
    print()

if __name__ == '__main__':
    directorio_telefonico = {}
    opcion_menu = 0
    while True:
        mostrarMenu()
        try:
            opcion_menu = int(input("Indica una opcion (1-7): "))
        except:
            print("Opcion no valida")
        else:
            if opcion_menu == 1:
                imprimirNumero(directorio_telefonico)
            elif opcion_menu == 2:
                print("Agregar nombre y telefono")
                nombre = input("nombre: ")
                phone = input("numero: ")
                agregarNumero(directorio_telefonico, nombre, phone)
            elif opcion_menu == 3:
                print("Eliminar nombre y telefono")
                nombre = input("nombre: ")
                borrarNumero(directorio_telefonico, nombre)
            elif opcion_menu == 4:
                print("Buscar numero")
                nombre = input("nombre: ")
                print(buscarNumero(directorio_telefonico, nombre))
            elif opcion_menu == 5:
                archivo = input("Archivo a cargar: ")
                cargarNumeros(directorio_telefonico, archivo)
            elif opcion_menu == 6:
                archivo = input("Archivo a guardar: ")
                guardarNumeros(directorio_telefonico, archivo)
            elif opcion_menu == 7:
                break
            else:
                print("Opcion no valida")
                mostrarMenu()

    print("Hasta luego!")
