class Vehiculo(object):
    precio_base = 0.0

    def __init__(self, llantas, kilometros, marca, modelo, anio, vendido):
        self.llantas = llantas
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


class Carro(Vehiculo):
    def __init__(self, llantas, kilometros, marca, modelo, anio, vendido):
        self.llantas = llantas
        self.kilometros = kilometros
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.vendido = vendido
        self.precio_base = 5000


class Camion(object):
    def __init__(self, llantas, kilometros, marca, modelo, anio, vendido):
        self.llantas = llantas
        self.kilometros = kilometros
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.vendido = vendido
        self.precio_base = 8000