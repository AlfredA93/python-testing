""" Imports """
#pylint:disable = C0116, C0103
import unittest
from evens import even_number_of_evens

class TestEvens(unittest.TestCase):
    """
    Test 1
    """
    def test_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)

    def test_list_values(self):
        self.assertEqual(even_number_of_evens([]), False)
        self.assertEqual(even_number_of_evens([2,4]), True)
        self.assertEqual(even_number_of_evens([2]), False)
        self.assertEqual(even_number_of_evens([1,3,5,7,9]), False)

if __name__ == '__main__':
    unittest.main()
