class Cliente(object):
    __total_clientes = 0

    def __init__(self, nombre, saldo=0.0):
        self.nombre = nombre
        self.saldo = saldo
        Cliente.__total_clientes += 1

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise RuntimeError("Cantidad superior al saldo disponible.")
        self.saldo -= cantidad
        return self.saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        return self.saldo

if __name__ == '__main__':
    petra = Cliente('Petra Petrov', 1000.0)
    print("Quien es el mejor cliente?")
    print(petra.nombre + " con $" + str(petra.saldo))

    deposito = float(input("Cantidad a depositar: "))
    saldo = petra.depositar(deposito)

    print("El saldo provisional de " + petra.nombre + " es " + str(petra.saldo))

    retiro = float(input("Cantidad a retirar: "))
    try:
        petra.retirar(retiro)
    except RuntimeError as e:
        print(str(e))

    #print("El total de clientes es " + str(Cliente.__total_clientes))
    juan = Cliente('Juan Juan')
    #print("El total de clientes es " + str(Cliente.__total_clientes))
    jose = Cliente('Jose Jose', 150.0)
    #print("El total de clientes es " + str(Cliente.__total_clientes))
