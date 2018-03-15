import calculadora
import unittest

class TestSumar(unittest.TestCase):
    def test_suma_enteros(self):
        resultado = calculadora.sumar(5, 7)
        self.assertEqual(resultado, 12)

    def test_suma_flotantes(self):
        resultado = calculadora.sumar(5.5, 2)
        self.assertEqual(resultado, 7.5)
    
    def test_suma_cadenas(self):
        resultado = calculadora.sumar('xo','pa')
        self.assertEqual(resultado, 'xopa')

if __name__ == '__main__':
    unittest.main()