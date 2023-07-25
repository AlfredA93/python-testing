"""Libraries"""
from datetime import timedelta
import unittest
from student import Student


class TestStudent(unittest.TestCase):
    """Test"""

    @classmethod #makes it impact on the class as a whole, not an instance of a class
    def setUpClass(cls):
        "setUpClass wide"
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        "tearDownClass wide"
        print('tearDownClass')

    def setUp(self):
        "Set files/data for access to be used on each test"
        print('setUp')
        self.student = Student('John', 'Doe')

    def tearDown(self):
        "Used to remove temporary files for testing. Used in conjunction with setUp"
        print('tearDown')

    def test_full_name(self):
        "Full Name"
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe')

    def test_alert_santa(self):
        """Alert"""
        print('test_alert_santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        "Email"
        print('test_email')
        self.assertEqual(self.student.email, 'john.doe@email.com')

    def test_apply_extension(self):
        "Ext"
        print('test_apply_ext')
        curr_end = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, curr_end + timedelta(days=5))



if __name__ == '__main__':
    unittest.main()
