def isPalindromicNumber(num: int) -> bool:
    """
    Determina sin un numero es palindromico
    :param num: Numbero entero a evaluar
    :type num: int
    :return: Verdadero si es numero palindromico; Falso si no es numero palindromico
    :rtype: bool
    """
    try:
        if type(num) != int:
            raise TypeError("(Tipo incorrecto) Tipo <int> esperado.")

        source = [int(n) for n in str(num)]
        clone = source[:]
        clone.reverse()

        return source == clone
    except TypeError as error:
        print(error.with_traceback())


if __name__ == '__main__':
    """
    -- Determinar numero palindromico --

    Leer un numero entero e imprimir si es numero palindromico.

    Un numero es palindromico, si sus digitos se mantiene lo mismo si es invertido.
    En otras palabras es simetrico [https://es.wikipedia.org/wiki/Capic%C3%BAa]

    NOTA: Ejemplo utiliza interpretador de Python 3.x.x
    """
    try:
        number = int(input("Digite un numero: "))
    except:
        raise

    truthiness = "es" if isPalindromicNumber(number) else "no"

    print("%d %s numero Palindromo." % (number, truthiness))
