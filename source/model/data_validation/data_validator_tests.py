import unittest
from data_validator import *


class DataValidatorTests(unittest.TestCase):
    # By Steven Snelling

    @classmethod
    def setUpClass(cls):
        cls.dataValidator = DataValidator()

    def setUp(self):
        # be executed before each test
        print("set up")
        self.data_1 = [['H001', 'M', '16', '200', 'Normal', '230',
                        '30-05-1999']]

        self.data_2 = [['', '', '', '', '', '', '']]

        self.data_3 = [['H001', '16', '200', 'Normal', '230', '30-05-1999']]

        self.data_4 = False

    def tearDown(self):
        # be executed after each test case
        print("teardown")

    def test_data_validator_01(self):
        # good day for testing validator
        result = [['H001', 'M', '16', '200', 'Normal', '230', '30-05-1999']]
        test = self.dataValidator.validate_data(self.data_1)
        response = "That is a valid data array"
        self.assertEqual(test, result, response)

    def test_data_validator_02(self):
        # bad day for testing validator no data
        result = []
        test = self.dataValidator.validate_data(self.data_2)
        response = "That is not a valid data array"
        self.assertEqual(test, result, response)

    def test_data_validator_03(self):
        # bad day for testing validator some data
        result = "Not enough fields: 6"
        test = self.dataValidator.validate_data(self.data_3)
        response = "That data array is missing data"
        self.assertEqual(test, result, response)

    def test_data_validator_04(self):
        # bad day for testing validator can different type
        result = []
        test = self.dataValidator.validate_data(self.data_4)
        response = "That is not a valid data Type"
        self.assertEqual(test, result, response)


if __name__ == '__main__':
    unittest.main(verbosity=2)
