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

    