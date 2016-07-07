import unittest
from Calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def test_negativo_discr(self):
        c = Calculadora()
        self.assertRaises(Exception,c.demo,2,1,2)

    def test_raiz(self):
        c = Calculadora()
        self.assertGreaterEqual(c.demo2(25),5.0)

    def test_loquesea(self):
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()