if __name__ == '__main__':
    # ganadores = ['Petra', 'Juana', 'Calixtra', 'Toribia']
    # listaloca = ['Susana', 12, True, ['S', 'T', 'D']]
    # print(ganadores[2])
    # print(listaloca[0])
    # print(listaloca[3][2])
    # print(ganadores)
    # print(len(ganadores))
    # print(ganadores[1:3])
    # print(listaloca[:3])
    # otralista = listaloca[:1] + ganadores
    # print(otralista)
    # otra = input('Quien se lo ganó: ')
    # ganadores.append(otra)
    # ganadores.insert(4, otra)
    # print(ganadores)
    # for g in ganadores:
    #     print(g)

    # abc = [1, 2, 3]
    # abc.insert(1, 4)
    # print(abc)
    # abc[1] = 5
    # print(abc)
    # abc.append(6)
    # print(abc)
    # del abc[3]
    # print(abc)

    # vacia = []
    # num = int(input('Cuantos nombres? '))
    # for n in range(num):
    #     nombre = input("Nombre  " + str(n) + ':')
    #     vacia.append(nombre)
    # print(vacia)

    # tupla1 = ('Petra', 'tiene', 'plata')
    # tupla2 = tupla1[0:2]
    # print(tupla1)
    # print(tupla2)
    # del tupla1
    # # print(tupla1)
    # print(tupla2)
    # print("WOLOLO")

    css = {'Dundunsua': ['Ranguliao!', 'Hermanito...']}
    css['Dundunsua'].append('No te tire!')
    css['Viejito que se rie'] = "Ranguliao se llama ese pelao"
    print(css)
    del css['Viejito que se rie']
    print(css)

    if 'Dundunsua' not in css:
        print("Cristo te ama")
    else:
        print("Tirate pue!")