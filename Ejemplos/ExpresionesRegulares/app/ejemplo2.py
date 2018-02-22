import re

if __name__ == '__main__':
    palabra1 = 'xopa'
    palabra2 = 'sopa'
    palabra3 = 'ropa'

    # if re.match(palabra1, palabra2):
    #     print('Opa')
    # else:
    #     print('Nah!')

    if re.match('....', palabra1):
        print('Opa Opa!')
    else:
        print("NO sirve")

    if re.match('\.png', '.png'):
        print("Imagen PNG")

    extensiones = ['doc', 'xls', 'ppt', 'mp3', 'flv']
    for tipo in extensiones:
        if re.match('doc|xls|ppt', tipo):
            print("Billete para Microsoft")
        elif re.match('mp3', tipo):
            print("Billete para Spotify")
        else:
            print("Habla!")

    palabras = ['rata', 'rampa', 'rasca', 'chino']
    for p in palabras:
        if re.match('r(..|...|....)a', p):
            print(p)