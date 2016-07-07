from src.Perro import Perro
import src.Gato

if __name__ == "__main__":
    lassie = Perro("Lassie", "Bulldog")
    lassie.comer()
    lassie.dormir()
    print(lassie.nombre + " es una "+ lassie.raza)

    misifus = src.Gato.Gato("Misifus")
    misifus.dormir()
    print("Mi gato se llama " + misifus.getNombre())