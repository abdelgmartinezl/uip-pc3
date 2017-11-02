
import re

patron = '[0-7]'
palabras = ['1', '15', '7']

for palabra in palabras:
    if re.match(patron, palabra):
        print("La palabra " + palabra + " cumple.")
    else:
        print("La palabra " + palabra + " no cumple.")

patron = '.[a-z]sa'
palabras = ['casa', 'cesa', 'cosa', 'tasa']

for palabra in palabras:
    if re.match(patron, palabra):
        print("La palabra " + palabra + " cumple.")
    else:
        print("La palabra " + palabra + " no cumple.")

patron = '[A-Za-z][6-9a-z].\.exe'
palabras = ['1', '15', '7']

for palabra in palabras:
    if re.match(patron, palabra):
        print("La palabra " + palabra + " cumple.")
    else:
        print("La palabra " + palabra + " no cumple.")