if __name__ == '__main__':
    """
    Problema -

    Construya un programa que permita al usuario ingresar una frase o palabras iterativamente.
    EL programa debe cumplir con los siguientes requerimientos:

    a) Contar la cantidad de ocurrencias de la palabra clave "agua" y "fuego" contenida dentro de la frase o palabras
       por cada iteracion.
    b) Continuar hasta que el usuario escriba "salir".
    c) Imprimir en pantalla un resume breve, preferible dict, de las cantidad de ocurrencias.

    Ejemplo -

    1) Desea saber cuantas veces la palabra "agua" se repite en "me gusta el agua fria mas que el agua caliente".
    El resultado es { 'agua': 2 }.

    2) Desea saber cuantas veces la palabra "fuego" se repite en "el fuegofuego es esencial. sin el fuego no existimos".
    El resultado es { 'fuego': 1 } porque "fuegofuego" es compuesto, no individual.
    """

    result = {
        'agua': 0,
        'fuego': 0
    }
    ask = ''

    while not ask.lower() == 'salir':
        ask = input('> ')

        result['agua'] = result.get('agua') + ask.lower().count('agua')
        result['fuego'] = result.get('fuego') + ask.lower().count('fuego')

    print(result)
