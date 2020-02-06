from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.exponentiation import Exponentiation

class Calculator:
    Result = 0

    def __init__(self):
        pass

    def sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def multiplication(self, a, b):
        self.Result = Multiplication.multiplication(a, b)
        return self.Result

    def division(self, a, b):
        self.Result = Division.division(a, b)
        return self.Result

    def exponentiation(self, a, b):
        self.Result = Exponentiation.exponentiation(a, b)
        return self.Result

