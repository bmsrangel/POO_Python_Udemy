import unittest
from calculadora import Calculadora


class TddExemplo(unittest.TestCase):
    def teste_soma(self):
        calc = Calculadora()
        result = calc.somar(-20, 40)
        self.assertEqual(20, result)

    def teste_sub(self):
        calc = Calculadora()
        result = calc.subtrair(40, 20)
        self.assertEqual(20, result)

    def teste_mult(self):
        calc = Calculadora()
        result = calc.multiplicar(5, 4)
        self.assertEqual(20, result)

    def teste_div(self):
        calc = Calculadora()
        result = calc.dividir(10, 2)
        self.assertEqual(5, result)


if __name__ == '__main__':
    unittest.main()
