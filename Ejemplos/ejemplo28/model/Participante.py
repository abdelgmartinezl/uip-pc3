class Participante:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def mostrar(self):
        print("Nombre: " + self.nombre + " (" + str(self.edad) + ")")
        print("Sexo: " + self.sexo)