if __name__ == "__main__":
    print(list(range(10)))
    print(list(range(1, 11)))
    print(list(range(1, 11, 2)))

    for x in range(2, 11, 2):
        if x == 8:
            print("Se lo ganó")