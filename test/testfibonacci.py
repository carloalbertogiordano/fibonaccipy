import unittest

from fibonacci import Fibonacci


class TestFibonacci(unittest.TestCase):

    def setUp(self):
        self.fibonacci = Fibonacci()

    def test_fibonacci_0_should_return_0(self):
        result = self.fibonacci.calculate(0)
        self.assertEqual(0, result)

    def test_fibonacci_1_should_return_1(self):
        result = self.fibonacci.calculate(1)
        self.assertEqual(1, result)

    def test_fibonacci_2_should_return_1(self):
        result = self.fibonacci.calculate(2)
        self.assertEqual(1, result)


    def test_fibonacci_10_should_return_55(self):
        result = self.fibonacci.calculate(10)
        self.assertEqual(55, result)

    def test_fibonacci_minus_1_should_raise_error(self):
        self.assertRaises(ValueError, self.fibonacci.calculate, -1)
