
import re

patron = '[0-7]'
palabras = ['1', '15', '7']

for palabra in palabras:
    if re.match(patron, palabra):
        print("La palabra " + palabra + " cumple.")
    else:
        print("La palabra " + palabra + " no cumple.")

patron = '\\\[a-z]sa'
palabras = ['casa', 'cesa', 'cosa', 'tasa', '\\asa']

for palabra in palabras:
    if re.match(patron, palabra):
        print("La palabra " + palabra + " cumple.")
    else:
        print("La palabra " + palabra + " no cumple.")

patron = '[A-Za-z][6-9a-z].\.exe'
palabras = ['A7a.exe', 'tns.exe', 'X1..exe']

for palabra in palabras:
    if re.match(patron, palabra):
        print("La palabra " + palabra + " cumple.")
    else:
        print("La palabra " + palabra + " no cumple.")

patron = '\d\w\w\w\d\.exe'
palabras = ['1aaa1.exe', '10aa1.exe', '11111.exe', '1,,,1.exe']

for palabra in palabras:
    if re.match(patron, palabra):
        print("La palabra " + palabra + " cumple.")
    else:
        print("La palabra " + palabra + " no cumple.")

patron = '[A-Z][a-z]+\s[A-Z](\.|[a-z]+)'
palabras = ['Abdel M.', 'Abdel M', 'Abdel Martinez', 'Abdulah Ramadahzunzo.']

for palabra in palabras:
    if re.match(patron, palabra):
        print("La palabra " + palabra + " cumple.")
    else:
        print("La palabra " + palabra + " no cumple.")