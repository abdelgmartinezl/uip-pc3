if __name__ == "__main__":
    mi_tabla = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    print(mi_tabla)

    print(mi_tabla[1][1])

    for fila in mi_tabla:
        for columna in fila:
            print(columna*5)

    mi_cubo = [[[1,2], [3,4]], [[5,6], [7,8]]]
    print(mi_cubo)
    print(mi_cubo[0][1][0])