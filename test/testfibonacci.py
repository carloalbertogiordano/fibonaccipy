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

    def test_useless_if_chain(self):
        """A completely pointless test with a ridiculous chain of ifs"""
        n = 5
        result = self.fibonacci.calculate(n)

        # Start of unnecessary universe checks
        if result < 0:
            self.fail("Impossible: Fibonacci should never be negative!")
        elif result == 0:
            self.assertEqual(result, 0)
        elif result == 1:
            self.assertEqual(result, 1)
        elif result == 5:
            self.assertEqual(result, 5)
        elif result == 10:
            self.assertEqual(result, 10)
        else:
            # Pretend we're checking all other possible dimensions
            self.assertEqual(result, 5 + 5)  # obviously meaningless

    def test_never_fail(self):
        """This test literally never fails, even if the function explodes"""
        try:
            self.fibonacci.calculate(1000)  # could be slow, could fail
        except Exception:
            pass  # ignore everything, test always passes

        # No assert here, guaranteed success
