class Participante:
    __nombre = ""
    __edad = 0
    __sexo = ""

    def __init__(self, nombre, edad, sexo):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo

    def mostrar(self):
        print("Nombre: " + self.__nombre + " (" + str(self.__edad) + ")")
        print("Sexo: " + self.__sexo)

    def get_sexo(self):
        return self.__sexo

    def get_edad(self):
        return self.__edad