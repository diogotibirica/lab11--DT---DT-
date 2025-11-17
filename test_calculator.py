# https://github.com/diogotibirica/lab11--DT---DT-.git
# Partner 1: Diogo Tibirica
# Partner 2: Diogo Tibirica

import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-5, -5), -10)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(-1, 1), -2)
        self.assertEqual(calculator.subtract(5, 10), -5)

    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-1, 5), -5)
        self.assertEqual(calculator.mul(0, 100), 0)

    def test_divide(self):
        self.assertEqual(calculator.div(2, 6), 3)
        self.assertEqual(calculator.div(5, 10), 2)
        self.assertAlmostEqual(calculator.div(2, 5), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 10)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(10, 100), 2)
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 100)
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 100)
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 100)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(10, 0)
        with self.assertRaises(ValueError):
            calculator.logarithm(10, -100)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)
        self.assertAlmostEqual(calculator.hypotenuse(-3, 4), 5)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(4), 2)
        self.assertAlmostEqual(calculator.square_root(144), 12)
        with self.assertRaises(ValueError):
            calculator.square_root(-1)
# Do not touch this
if __name__ == "__main__":
    unittest.main()