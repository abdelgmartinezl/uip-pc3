
import re

patron = 'ra(..|...)ta'
palabras = ['ratata', 'rapero', 'raqueta', 'rata']

for palabra in palabras:
    if re.match(patron, palabra):
        print("La palabra " + palabra + " cumple.")
    else:
        print("La palabra " + palabra + " no cumple.")