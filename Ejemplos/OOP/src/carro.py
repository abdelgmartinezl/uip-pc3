class Carro(object):
    __llantas = 4

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @staticmethod
    def pitar():
        print("Zgschhfd Zgschhfd")
    
    def checar_llantas(self):
        return self.__llantas

if __name__ == '__main__':
    camaro = Carro('Chevrolet', 'Camaro')
    #print(camaro.__llantas)
    #print(Carro.llantas)
    camaro.pitar()
    Carro.pitar()
    print(camaro.checar_llantas())
    #print(Carro.checar_llantas())