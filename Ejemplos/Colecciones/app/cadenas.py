if __name__ == "__main__":
    palabra_magica = "abracadabra, alakazam"

    print(len(palabra_magica))
    print(palabra_magica.index("k"))
    print(palabra_magica[6])
    print(palabra_magica[3:5])

    letra = input("Ingrese una letra: ")
    if letra in palabra_magica:
        print(palabra_magica.index(letra))

    letras = list(palabra_magica)
    print(letras)

    lista_letras = ['a', 'b', 'u', 'e', 'l', 'a']
    viejo = "".join(lista_letras)
    print(viejo)