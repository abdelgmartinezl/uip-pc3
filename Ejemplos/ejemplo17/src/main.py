from calculadora import suma,resta

x = int(input("Introduce numero 1: "))
y = int(input("Introduce numero 2: "))

r1 = suma(x,y)
print("La suma fue " + str(r1))

r2 = resta(x,y)
print("La resta fue " + str(r2))