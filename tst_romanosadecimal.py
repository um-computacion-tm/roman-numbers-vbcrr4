import unittest

from romanos_a_decimal import roman_to_decimal
class TestDecimalToRoman(unittest.TestCase):

    def test_uno(self):

        resultado= roman_to_decimal ("I")

        self.assertEqual (resultado, 1)

    
    def test_cientoveintitres(self):

        resultado = roman_to_decimal('CXXIII')

        self.assertEqual (resultado, 123)
    
    def test_docientosveinte(self):
        
        resultado = roman_to_decimal('CCXX')

        self.assertEqual(resultado, 220)
    
    def test_cuatrocientosobhentayuno(self):

        resultado = roman_to_decimal('CDLXXXI')

        self.assertEqual(resultado, 481)
    
    def test_quinientos(self):

        resultado = roman_to_decimal('D')

        self.assertEqual(resultado, 500)
    
    def test_setecientossetentaycuatro(self):

        resultado = roman_to_decimal('DCCLXXIV')

        self.assertEqual(resultado, 774)
    
    def test_ochocientossetentaysiente(self):

        resultado= roman_to_decimal('DCCCLXXVII')
        self.assertEqual(resultado, 877 )

    def test_novecientos_ochenta_y_siete(self):
        resultado= roman_to_decimal("CMLXXXVII")
        self.assertEqual(resultado,987)    
    
    def test_mil(self):
        resultado= roman_to_decimal("M")
        self.assertEqual(resultado,1000)   
if __name__ == '__main__':
    unittest.main()