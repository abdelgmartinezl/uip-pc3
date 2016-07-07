class Gato:
    __nombre = ""

    def __init__(self, n):
        self.__nombre = n

    def setNombre(self, n):
        self.__nombre = n

    def getNombre(self):
        return self.__nombre

    def dormir(self):
        print("Los gatos no duermen.")