if __name__ == "__main__":
    palabra_magica = "abracadabra, alakazam"

    print(len(palabra_magica))
    print(palabra_magica.index("k"))
    print(palabra_magica[6])
    print(palabra_magica[3:5])

    letra = input("Ingrese una letra: ")
    if letra in palabra_magica:
        print(palabra_magica.index(letra))