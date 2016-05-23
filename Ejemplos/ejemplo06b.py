# Autor: Abdel G. Martinez L.
#
# Instrucciones: Simular un cliente de un banco

class Cliente(object):
    """
    Representacion de un cliente del Banco ABC con una
    cuenta de ahorros.

    Atributos:
        nombre: Una cadena que representa el nombre del cliente
        balance: Un flotante que lleva registro de su saldo actual
    """

    def __init__(self, nombre):
        """Retorna el objeto Cliente con su nombre."""
        self.nombre = nombre

    def establecer_balance(self, balance=0.0):
        """Establecer el balance inicial del cliente."""
        self.balance = balance

    def mostrar_balance(self):
        return self.balance

    def retirar(self, cantidad):
        """Retorna el balance remanente luego del retiro"""
        if cantidad > self.balance:
            raise RuntimeError('Cantidad mayor que saldo disponible')
        self.balance -= cantidad
        return self.balance

    def depositar(self, cantidad):
        """Retorna el balance remanente luego del deposito"""
        self.balance += cantidad
        return self.balance
