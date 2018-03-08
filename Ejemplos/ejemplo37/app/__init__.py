"""Este modulo ejecuta metodos que empiecen con s"""

def sumar(a, b):
    """ Esta funcion suma dos operandos
        :param a: Operando a
        :param b: Operando b
        :type a: int
        :type b: int
        :return: Retorna la suma de a y b
    """
    return a + b

def saludar(nombre):
    """ Esta funcion sale a saludar, basado en el nombre
    :param nombre: Nombre
    :type nombre: String
    """
    print("Saludo, " + nombre)

if __name__ ==  "__main__":
    n = input("Nombre: ")
    saludar(n)
    a = int(input("Num1: "))
    b = int(input("Num2: "))
    print(sumar(a,b))
