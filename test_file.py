# import the method from code_files
from code_files import CodeMethods

# import tests needed
import pytest
import unittest

# create a class that tests the relevant methods
class TestMethods(unittest.TestCase):
    # make an object of the CodeMethods
    code = CodeMethods()

    # Test the divisible method and see if it returns the correct value
    def test_divisible(self):
        self.assertEqual(self.code.divisible(124, 4), True)

    # Test if the positive method works
    def test_positive(self):
        self.assertEqual(self.code.positive(3, 5, 6, 7, 9, 1000), True)
