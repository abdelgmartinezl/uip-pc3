
import re

patron = 'cas'
palabra1 = 'ccasa'

if re.match(patron, palabra1):
    print("La palabra1 " + palabra1 + " cumple.")
else:
    print("La palabra1 " + palabra1 + " no cumple.")