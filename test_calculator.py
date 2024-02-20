import unittest
from calculator import multiply

class TestCalculator(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-2, 3), -6)
    
    def test_invalid_arguments(self):
        with self.assertRaises(ValueError):
            multiply('a', 3)
            multiply(2, 'b')
            multiply('x', 'y')
