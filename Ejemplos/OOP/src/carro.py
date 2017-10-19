class Carro(object):
    llantas = 4

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @staticmethod
    def pitar():
        print("Zgschhfd Zgschhfd")

if __name__ == '__main__':
    camaro = Carro('Chevrolet', 'Camaro')
    print(camaro.llantas)
    print(Carro.llantas)
    camaro.pitar()
    Carro.pitar()