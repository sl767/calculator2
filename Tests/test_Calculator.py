import unittest

from Calculator2.Calculator2 import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calculator_return_sum(self):
        result = self.calculator.sum(1, 2)
        self.assertEqual(3, result)

    def test_calculator_return_difference(self):
        result = self.calculator.difference(1, 2)
        self.assertEqual(-1, result)

    def test_calculator_access_difference_result(self):
        self.calculator.difference(1, 2)
        self.assertEqual(-1, self.calculator.Result)

    def test_calculator_access_sum_result(self):
        self.calculator.sum(1, 2)
        self.assertEqual(3, self.calculator.Result)

    def test_calculator_return_product(self):
        result = self.calculator.multiplication(1, 2)
        self.assertEqual(2, result)

    def test_calculator_access_product_result(self):
        self.calculator.multiplication(1, 2)
        self.assertEqual(2, self.calculator.Result)

    def test_calculator_return_quotient(self):
        result = self.calculator.division(4, 2)
        self.assertEqual(2, result)

    def test_calculator_access_quotient_result(self):
        self.calculator.division(4, 2)
        self.assertEqual(2, self.calculator.Result)

    def test_multiple_calculators(self):
        calculator1 = Calculator()
        calculator2 = Calculator()
        calculator3 = Calculator()
        calculator3.sum(calculator1.sum(1, 2), calculator2.difference(3, 4))
        self.assertEqual(2, calculator3.Result)


if __name__ == '__main__':
    unittest.main()