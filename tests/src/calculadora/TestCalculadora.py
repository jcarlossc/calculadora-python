import unittest
from src.calculadora.Calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        """Instancia da calculadora."""
        self.calc = Calculadora()

    def test_soma(self):
        """Testa soma."""
        resultado = self.calc.avaliar_expressao("2+3")
        self.assertEqual(resultado, "5")

    def test_subtracao(self):
        """Testa subtração."""
        resultado = self.calc.avaliar_expressao("10-4")
        self.assertEqual(resultado, "6")

    def test_multiplicacao(self):
        """Testa multiplicação."""
        resultado = self.calc.avaliar_expressao("3*3")
        self.assertEqual(resultado, "9")

    def test_divisao(self):
        """Testa divisão."""
        resultado = self.calc.avaliar_expressao("10/2")
        self.assertEqual(resultado, "5.0")

    def test_divisao_por_zero(self):
        """Testa divisão por zero."""
        resultado = self.calc.avaliar_expressao("5/0")
        self.assertEqual(resultado, "Erro")

    def test_expressao_invalida(self):
        """Testa expressão inválida."""
        resultado = self.calc.avaliar_expressao("2++*")
        self.assertEqual(resultado, "Erro")

    def test_entrada_vazia(self):
        """Testa string vazia."""
        resultado = self.calc.avaliar_expressao("")
        self.assertEqual(resultado, "Erro")

if __name__ == "__main__":
    unittest.main()
