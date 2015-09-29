# CLASE 4
# Autor: Abdel G. Martinez L.
#
# Instrucciones: Crear programa donde el usuario adivine un numero previamente dado.

intentos = 0
numero = 17 
nombre = input("NOMBRE: ")

print("Bueno, {0}, pienso en numero entre 1 y 20.".format(nombre))

while intentos < 6:
    chance = int(input("NUMERO: "))

    intentos += 1

    if chance < numero:
        print('Muy bajo.')

    if chance > numero:
        print('Muy alto.')

    if chance == numero:
        break

if chance == numero:
    print("Buen trabajo, {0}. Adivinastes en {1} intentos.".format(nombre, intentos))
else:
    print("No. El numero que estaba pensando era {0}.".format(numero))
