import unittest
from lib import factorial

class TestFactorial(unittest.TestCase):

    def test_positive_integer(self):
        """Test factorial for a positive integer."""
        self.assertEqual(factorial(5), 120)

    def test_zero(self):
        """Test factorial of zero."""
        self.assertEqual(factorial(0), 1)

    def test_negative_integer(self):
        """Test factorial for a negative integer raises ValueError."""
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_non_integer(self):
        """Test factorial for a non-integer raises ValueError."""
        with self.assertRaises(ValueError):
            factorial(1.5)

if __name__ == '__main__':
    unittest.main()
