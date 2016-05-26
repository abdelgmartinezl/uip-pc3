total = 0
cont1 = 0
while True:
    nota = int(input("Calificacion (negativo para salir): "))
    if nota < 0:
        break
    cont1 += 1
    total = total + nota
if cont1 != 0:
    promedio = total / cont1
else:
    promedio = 0
if promedio >= 91:
    print("Saca A",promedio)
elif promedio >= 81:
    print("Saca B",promedio)
elif promedio >= 71:
    print("Saca C",promedio)
else:
    print("#TeQuedaste\a",promedio)
