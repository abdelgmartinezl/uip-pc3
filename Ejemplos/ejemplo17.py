def b2tc(number: int):
    """
    Funcion devuelve el complemento de un numero entero el cual se define como "inversion de todos los bits".
    :param number: numero entero
    :type number: int
    :return: cadena conforme a resultado inverso de bit (XOR)
    :rtype: str
    """
    b2int = int(bin(number)[2:])  # [2:] excluir `0b`
    xor = ['0' if b == '1' else '1' for b in str(b2int)]  # comprehension list

    return ''.join(xor)


if __name__ == '__main__':
    """
    -- Complemento a 2's --

    Leer un numero entero, convertir a binario e imprimir complemento a 2's de la conversion rapida.

    La conversion rapida comprende invertir todo los bits de un numero entero. En el sistema binario
    se conoce como operacion XOR.

    La conversion rapida es relativamente sencilla,
    1ro. convertir a binario
    2do. invertir bits

    Tome en cuenta que este ejemplo NO ES la implementacion adecuada del metodo sino,
    comprender un poco el uso de "comprehension list".

    Fuente (https://es.wikipedia.org/wiki/Complemento_a_dos)
    """

    num = 0

    print("INGRESE NUMERO ENTERO")

    try:
        num = int(input("R: "))
    except ValueError as ex:
        raise RuntimeError("<EXCEPCION> Tipo de dato invalido") from ex

    print("\nNUMERO ENTERO %d\n2b: %d\ncomplemento 2b: %s" % (num, int(bin(num)[2:]), b2tc(num)))
