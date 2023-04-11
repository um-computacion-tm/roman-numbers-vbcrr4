import unittest

from contapalabras import conta_palabras

class TestContaPalabras (unittest.TestCase):
    
    def test_1(self):
        resultado = conta_palabras('hola mundo')
        self.assertEqual (resultado, {'hola':1, 'mundo':1})
    
    def test_2(self):
        resultado = conta_palabras('hola hola mundo palabras MUNDO PALABRAS perro gato')
        self.assertEqual (resultado, {'hola':2, 'mundo':2, 'palabras':1, 'palabras':2, 'perro':1, 'gato':1})



if __name__ == '__main__':
    unittest.main()