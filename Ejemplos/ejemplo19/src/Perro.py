class Perro:
    nombre = ""
    raza = ""

    def __init__(self, n, r):
        self.nombre = n
        self.raza = r
    
    def comer(self):
        print("El perro esta comiendo.")

    def dormir(self):
        print("Zzzz....")