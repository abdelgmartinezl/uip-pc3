# Soy un comentario
print('''VENDESOFT 1.0
         *************
         El mejor software para registrar ventas...
         Y no tienes que pagar ningun centavo!
      ''')

while True:
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

    opcion = input("Desea continuar (S/N)?")
    if opcion == 'N' or opcion == 'n':
        break