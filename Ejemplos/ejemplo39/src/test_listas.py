import listas
import unittest

class TestListas(unittest.TestCase):
    def setUp(self):
        l = listas.crear_lista()
    
    @unittest.skip('Evitar esta prueba')
    def test_validar_lista(self):
        esperada = ['papa', 'maiz']
        self.assertListEqual(l, esperada) # ESTO NO SIRVE

    def test_agregar_elemento(self):
        l = listas.agregar_lista("coco")
        self.assertIn("coco", l)

    def tearDown(self):
        l = listas.borrar_lista()

if __name__ == '__main__':
    unittest.main()