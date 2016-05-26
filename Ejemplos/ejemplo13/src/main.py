# Autor: Abdel Martinez
# Se ingresara 5 calificaciones, se calcula
# su promedio y se identifica la letra final

total = 0

for x in range(1,6):
    nota = int(input("Calificacion: "))
    total = total + nota
promedio = total / 5
if promedio >= 91:
    print("Saca A",promedio)
elif promedio >= 81:
    print("Saca B",promedio)
elif promedio >= 71:
    print("Saca C",promedio)
else:
    print("#TeQuedaste\a",promedio)