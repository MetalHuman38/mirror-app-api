"""
sample test
"""
from django.test import SimpleTestCase

from app import calc 


class calcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_number(self):
        """test adding numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self): 
        """test subtracting numbers together"""
        res = calc.subtract(10, 5)

        self.assertEqual(res, 5)

