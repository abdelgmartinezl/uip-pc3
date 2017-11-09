def division(dividendo, divisor):
    """
    Funcion Division

    Este es un ejemplo de documentacion utilizando
    DocString. Esto simplemente agarra dos numeros
    y los divide. Al final de la funcion, se retorna
    el resultado.

    :param dividendo: dividendo de la operacion
    :type dividendo: float
    :param divisor: divisor de la operacion
    :type divisor: float
    :return: resultado de la division
    :raises ZeroDivisionError: cuando divisor = 0

    .. note:: Esta funcion acepta tambien :class:`int`.

    .. warning:: ``divisor=0`` va a causar ZeroDivisionError!

    Example::

        resultado = division(x,y)

    """
    return dividendo / divisor

if __name__ == "__main__":
    print("Divide y Venceras")
    d1 = float(input("Dividendo: ")) #: d1 dividendo
    d2 = float(input("Dividisplasor: ")) #: d2 divisor
    r = division(d1, d2) #: r resultado
    print(str(d1) + "/" + str(d2) + "=" + str(r))