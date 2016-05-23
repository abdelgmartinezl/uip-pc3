# Autor: Abdel G. Martinez L.
#
# Instrucciones: Dada una lista de numeros positivos, retornar el numero mas grande de la lista

def find_max(L):
    max = 0
    for x in L:
        if x > max:
            max = x
    return max

if __name__ == '__main__':
    L = (17, 20, 29, 16)
    result = find_max(L)
    print(result)
