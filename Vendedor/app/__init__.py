# Soy un comentario
print('''VENDESOFT 1.0
         *************
         El mejor software para registrar ventas...
         Y no tienes que pagar ningun centavo!
      ''')

ventas_globales = 0.0
lista_vendedores = []

while True:
    registro = {}
    nombre = input("\nNombre: ") # Dale pue
    while True:
        try:
            venta_mensual = float(input('Venta Mensual: '))
            break
        except:
            print("Tas metiendo demencia... Vivo!")

    if venta_mensual > 100_000.00:
        print("Eres un vendedor estrella!!!")
    elif venta_mensual > 90000.00:
        print("Te falta poco para la meta...")
    elif venta_mensual > 50000:
        print("Sobreviviste :)")
    elif venta_mensual > 0.00:
        print("Larga a vender mas :@")
    else:
        print("Que haces aqui? DESPEDIDO!")

    registro["nombre"] = nombre
    registro["venta"] = venta_mensual
    lista_vendedores.append(registro)
    ventas_globales += venta_mensual

    opcion = input("Desea continuar (S/N)?")
    if opcion == 'N' or opcion == 'n':
        break

print("\nLista de Vendedores: ")
for x in lista_vendedores:
    print(str("- " + x["nombre"]))
print("Ventas Globales:", str(ventas_globales))