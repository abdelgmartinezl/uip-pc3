class Cliente(object):
    def __init__(self, nombre, saldo=0.0):
        self.nombre = nombre
        self.saldo = saldo

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise RuntimeError("Cantidad superior al saldo disponible.")
        self.saldo -= cantidad
        return self.saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        return self.saldo