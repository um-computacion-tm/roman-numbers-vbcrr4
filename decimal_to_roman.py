import unittest
def romantodecimal(romano):
    d_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C' : 100, 'D': 500, 'M': 1000}
    d_decimal= [d_num[char] for char in romano] #char=variable temporal para iterar
    total = 0
    for i in range(len(d_decimal)):
        if i == len(d_decimal) -1 or d_decimal[i] >= d_decimal[i+1]:
            total += d_decimal[i]
        else:
            total -= d_decimal[i]
    return total

class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        resultado=romantodecimal("I")
        self.assertEqual(resultado,1)
#hacer demas test

if __name__ == '__main__':
    unittest.main()
