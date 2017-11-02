
import re

patron = 'p.|c|java|rb|php|js'
palabras = ['jpg', 'ps', 'rb', 'py', 'exe', 'js']

for palabra in palabras:
    if re.match(patron, palabra):
        print("La palabra " + palabra + " cumple.")
    else:
        print("La palabra " + palabra + " no cumple.")