# CLASE 7
# Autor: Abdel G. Martinez L.
#
# Instrucciones: Explicacion de herencia

class Padre(object): # define clase Padre
   # Atributo publico y privado, respectivamente
   atributoPadre = 100
   __contador = 0

   # Constructor
   def __init__(self):
      print("Llamando al constructor del padre")

   # Metodos publicos
   def metodoPadre(self):
      print('Llamando al metodo del padre')

   def setAtributo(self, attr):
      Padre.atributoPadre = attr

   def miMetodo(self):
      print('Llamando al otro metodo del padre')

   def getAtributo(self):
      print("Atributo (Padre): ", Padre.atributoPadre)

   def contar(self):
       self.__contador += 1
       print(self.__contador)

class Hijo(Padre): # define clase Hijo, herencia
   # Constructor
   def __init__(self):
      print("Llamando al constructor del hijo")

   # Metodos publicos
   def metodoHijo(self):
      print('Llamando al metodo del hijo')

   def miMetodo(self):
      print('Llamando al otro metodo del hijo')

if __name__ == '__main__':
    c = Hijo()          # instancia de la clase Hijo
    c.metodoHijo()      # llamado al metodo del hijo
    c.metodoPadre()     # llamado al metodo del padre
    c.setAtributo(200)  # llamado al metodo del padre
    c.getAtributo()     # llamado al metodo del padre
    c.miMetodo()        # llamado al metodo del hijo, no del padre
    c.contar()          # llamado al atributo privado
