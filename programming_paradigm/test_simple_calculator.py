import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(float('inf'), 5), float('inf'))
        self.assertEqual(self.calc.add(float('-inf'), 5), float('-inf'))

    def test_subtraction(self):

            """Test the subtraction method."""
            self.assertEqual(self.calc.subtract(5, 3), 2)
            self.assertEqual(self.calc.subtract(-1, 1), -2)
            self.assertEqual(self.calc.subtract(-1, -1), 0)
            self.assertEqual(self.calc.subtract(0, 0), 0)
            self.assertEqual(self.calc.subtract(0, 5), -5)
            self.assertEqual(self.calc.subtract(5, 0), 5)
            self.assertEqual(self.calc.subtract(float('inf'), 5), float('inf'))
            self.assertEqual(self.calc.subtract(float('-inf'), 5), float('-inf'))

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, 0), 0)
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(9, 5), 45)

    def test_division(self):

            """Test the division method."""
            self.assertEqual(self.calc.divide(10, 2), 5)
            self.assertEqual(self.calc.divide(-10, 2), -5)
            self.assertEqual(self.calc.divide(-10, -2), 5)
            self.assertEqual(self.calc.divide(0, 5), 0)
            with self.assertRaises(ZeroDivisionError):
                self.calc.divide(10, 0)
            with self.assertRaises(ZeroDivisionError):
                self.calc.divide(0, 0)
            self.assertEqual(self.calc.divide(float('inf'), 5), float('inf'))
            self.assertEqual(self.calc.divide(float('-inf'), 5), float('-inf'))
            self.assertEqual(self.calc.divide(float('inf'), float('inf')), float('nan'))
            self.assertEqual(self.calc.divide(float('-inf'), float('inf')), float('nan'))