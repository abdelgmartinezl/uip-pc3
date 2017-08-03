"""
Este es el modulo para chotiar 
a la gente de la UIP
"""

class Hola(object):
    """
    Esta es la clase Hola que permite chotiar
    """

    def __init__(self, nombre):
        """
        Este es el metodo constructor de la clase.
        Crea un nueva instancia de :class:`Hola`
        :param nombre: nombre para el saludo
        :type nombre: str
        """
        self.nombre = nombre

    def saludar(self):
        """
        Este es el metodo para chotiar a la gente.
        Usa el atributo nombre y lo imprime.
        """
        print("Hola, %s" % self.nombre)

    def getNombre(self):
        """
        Este el metodo para enviar el valor del nombre.
        :return: nombre usado en el saludo 
        """
        return self.nombre