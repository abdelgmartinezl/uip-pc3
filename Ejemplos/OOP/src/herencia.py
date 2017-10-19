from abc import abstractmethod

class Vehiculo(object):
    precio_base = 0.0
    llantas = 0

    def __init__(self, kilometros, marca, modelo, anio, vendido):
        self.kilometros = kilometros
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.vendido = vendido

    def precio_venta(self):
        if self.vendido is not None:
            return 0.0
        return 5000 * self.llantas

    def precio_compra(self):
        if self.vendido is None:
            return 0.0
        return self.precio_base - (.10 * self.kilometros)

    @abstractmethod
    def tipo_vehiculo(self):
        pass


class Carro(Vehiculo):
    precio_base = 5000
    llantas = 4

    def tipo_vehiculo(self):
        return 'carro'


class Camion(object):
    precio_base = 8000
    llantas = 18

    def tipo_vehiculo(self):
        return 'camion'