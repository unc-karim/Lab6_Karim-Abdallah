import os
import sys
import unittest

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../../src/main/python")
    ),
)

from calculator_Karim_Abdallah import (
    add, subtract, multiply, divide, modulus, power, square_root,
)


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)

    def test_modulus_negative(self):
        self.assertEqual(modulus(-10, 3), 2)

    def test_modulus_by_zero(self):
        with self.assertRaises(ValueError):
            modulus(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)

    def test_power_negative_exponent(self):
        self.assertEqual(power(2, -2), 0.25)

    def test_square_root(self):
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(0.25), 0.5)

    def test_square_root_non_perfect_square(self):
        self.assertAlmostEqual(square_root(2), 1.4142135623730951)

    def test_square_root_zero(self):
        self.assertEqual(square_root(0), 0)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            square_root(-1)


if __name__ == "__main__":
    unittest.main()
