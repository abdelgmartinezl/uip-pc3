import calculadora
import unittest

class TestSumar(unittest.TestCase):
    """
    Prueba la funcion de sumar de la libreria calculadora
    """

    def test_suma_enteros(self):
        """
        Prueba que la suma de dos enteros sea correcta
        """
        resultado = calculadora.sumar(5, 7)
        self.assertEqual(resultado, 12)
        self.assert

    def test_suma_flotantes(self):
        """
        Prueba que la suma de dos flotantes sea correcta
        """
        resultado = calculadora.sumar(5.5, 2)
        self.assertEqual(resultado, 7.5)
    
    def test_suma_cadenas(self):
        """
        Prueba que dos cadenas se concatenan
        """
        resultado = calculadora.sumar('xo','pa')
        self.assertEqual(resultado, 'xopa')

if __name__ == '__main__':
    unittest.main()