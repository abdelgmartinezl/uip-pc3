# Autor: Abdel G. Martinez L.
# Hacer un programa que lea 5 numeros
# y los ordene de forma descendente

for x in range(1,4):
    num = int(input("Numero " + str(x) +": "))
    if x == 2:
        md = num
    if x == 1:
        mx = num
    elif num > mx:
        md = mx
        mx = num
    elif num > md:
        mn = md
        md = num
    else:
        mn = num
print(mx,md,mn)