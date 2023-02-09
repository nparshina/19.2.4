import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    #тест сложения

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 13, 3) == 10

    #тест вычитания

    def test_multiplication_success(self):
        assert self.calc.multiply(self, 5, 6) == 30

    # тест умножения

    def test_division_success(self):
        assert self.calc.division(self, 12, 4) == 3

    # тест деления

    def teardown(self):
        print('Выполнение метода Teardown')