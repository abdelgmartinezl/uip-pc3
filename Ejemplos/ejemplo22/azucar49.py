class Azucar:
    def __init__(self, nombre, cantidad):
        """
        Crea una nueva instancia de Azucar.
        """
        self.__nombre = nombre
        self.__cantidad = cantidad

    def get_nombre(self):
        """
        Retorna el nombre de la azucar.
        Como es una metodo de solo lectura,
        utilizamos getter/setter.
        """
        return self.__nombre

    def get_cantidad(self):
        """
        Retorna la cantidad de azucar.
        """
        return self.__cantidad

    def set_nombre(self, nombre):
        """
        Establece el nombre de la azucar.
        Entrada: nombre  - una cadena cualquiera
        """
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        """
        Establece la cantidad de azucar.
        Entrada: cantidad - un numero cualquiera
        """
        self.__cantidad = cantidad


