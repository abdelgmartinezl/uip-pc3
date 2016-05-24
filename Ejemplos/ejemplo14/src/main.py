# Autor: Abdel G. Martinez L.
# Hacer un programa que lea 5 numeros
# y los ordene de forma descendente

num1 = int(input("Numero 1: "))
mx = num1
num2 = int(input("Numero 2: "))
if num2 > mx:
    mx = num2
    md = num1
else:
    md = num2
num3 = int(input("Numero 3: "))
if num3 > mx:
    mn = md
    md = mx
    mx = num3
elif num3 > md:
    mn = md
    md = num3
else:
    mn = num3
print(mx,md,mn)