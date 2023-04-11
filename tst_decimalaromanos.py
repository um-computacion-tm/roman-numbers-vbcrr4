import unittest
from decimal_a_romanos import decimal_to_roman

class TestDecimalToRoman(unittest.TestCase):

    def test_uno(self):
        resultado = decimal_to_roman(1)
        # verificacion
        self.assertEqual(resultado, 'I')

    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, 'X')

    def test_cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, 'V')

    def test_dos(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, 'II')

    def test_tres(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, 'III')

    def test_cien(self):
        resultado = decimal_to_roman(100)
        self.assertEqual(resultado, 'C')

    def test_ciento_uno(self):
        resultado = decimal_to_roman(101)
        self.assertEqual(resultado, 'CI')

    def test_ciento_tres(self):
        resultado = decimal_to_roman(103)
        self.assertEqual(resultado, 'CIII')

    def test_ciento_cinco(self):
        resultado = decimal_to_roman(105)
        self.assertEqual(resultado, 'CV')

    def test_ciento_diez(self):
        resultado = decimal_to_roman(110)
        self.assertEqual(resultado, 'CX')

    def test_docientos_tres(self):
        resultado = decimal_to_roman(203)
        self.assertEqual(resultado, 'CCIII')

    def test_docientos_veinte(self):
        resultado= decimal_to_roman(220)
        self.assertEqual(resultado,"CCXX")

    def test_docientos_veintiocho(self):
        resultado= decimal_to_roman(228)
        self.assertEqual(resultado,"CCXXVIII") 
    
    def test_docientos_sesenta(self):
        resultado= decimal_to_roman(260 )
        self.assertEqual(resultado,"CCLX") 

    def test_docientos_cincuenta(self):
        resultado= decimal_to_roman(250)
        self.assertEqual(resultado,"CCL") 

    def test_docientos_sesenta_y_seis(self):
        resultado= decimal_to_roman(266)
        self.assertEqual(resultado,"CCLXVI") 

    def test_docientos_ochenta_y_nueve(self):
        resultado= decimal_to_roman(289)
        self.assertEqual(resultado,"CCLXXXIX") 

    def test_docientos_veintiocho(self):
        resultado= decimal_to_roman(228)
        self.assertEqual(resultado,"CCXXVIII") 

    def test_docientos_noventa_y_cinco(self):
        resultado= decimal_to_roman(295)
        self.assertEqual(resultado,"CCXCV") 

    def test_trecientos_uno(self):
        resultado= decimal_to_roman(301)
        self.assertEqual(resultado,"CCCI") 

    def test_trecientos_quince(self):
        resultado= decimal_to_roman(315)
        self.assertEqual(resultado,"CCCXV") 

    def test_seicientos_cinco(self):
        resultado= decimal_to_roman(605)
        self.assertEqual(resultado,"DCV") 


    def test_setecientos_veinte(self):
        resultado= decimal_to_roman(720)
        self.assertEqual(resultado,"DCCXX") 

    def test_cuatrocientos_seis(self):
        resultado= decimal_to_roman(406)
        self.assertEqual(resultado,"CDVI") 

    def test_novecientos_veintitrés(self):
        resultado= decimal_to_roman(923)
        self.assertEqual(resultado,"CMXXIII") 

    def test_setecientos_cincuenta_y_uno(self):
        resultado= decimal_to_roman(751)
        self.assertEqual(resultado,"DCCLI") 

    def test_ochocientos_tres(self):
        resultado= decimal_to_roman(803)
        self.assertEqual(resultado,"DCCCIII") 

    def test_seicientos_treinta_y_cinco(self):
        resultado= decimal_to_roman(635)
        self.assertEqual(resultado,"DCXXXV") 

    def test_quinientos_sesenta_y_dos(self):
        resultado= decimal_to_roman(562)
        self.assertEqual(resultado,"DLXII") 

    def test_trecientos_sesenta_y_seis(self):
        resultado= decimal_to_roman(366)
        self.assertEqual(resultado,"CCCLXVI")

    def test_ochocientos_setenta_y_siete(self):
        resultado= decimal_to_roman(877)
        self.assertEqual(resultado,"DCCCLXXVII")    
    
    def test_novecientos_sesenta(self):
        resultado= decimal_to_roman(960)
        self.assertEqual(resultado,"CMLX")    
    
    def test_novecientos_ochenta_y_siete(self):
        resultado= decimal_to_roman(987)
        self.assertEqual(resultado,"CMLXXXVII")    
    
    def test_mil(self):
        resultado= decimal_to_roman(1000)
        self.assertEqual(resultado,"M")    

if __name__ == '__main__':
    unittest.main()
