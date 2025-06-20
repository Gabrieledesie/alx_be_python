import unittest 
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up calculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):  # ✅
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtraction(self):  # ✅
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiplication(self):  # ✅ Renamed to match checker expectation
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_division(self):
  # ✅
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(5, 0), None)  # Division by zero

if __name__ == '__main__':
    unittest.main()

