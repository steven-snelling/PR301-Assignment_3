import unittest
from .database import *


class DatabaseTests(unittest.TestCase):
    """Written By Thomas

        This file provides test coverage for the database

    """
    def setUp(self):
        self.database_handler = Database()
        self.data = [['A001', 'F', '23', '456', 'Normal', '23', '30-5-1994'],
                     ['C234', 'M', '5', '676', 'Overweight', '300', '1-12-1977'],
                     ['C4', 'Male', 'nine', '66,8', 'heavy', '3,00', '1-12-19']]

    def test_01(self):
        # Tries to get data from the default database
        # returns a blank list
        self.assertIsInstance(self.database_handler.get_person_information(), list)

    def test_02(self):
        # opens a new database then returns contents
        # returns a blank list
        self.assertFalse(self.database_handler.get_person_information("test_db"))

    def test_03(self):
        # Grabs the information from an existing database
        self.assertTrue(self.database_handler.get_person_information("../mydb"), "[['A001', 'F', 23"
                                                                                 ", 456, 'Normal',"
                                                                                 " 23, '30-5-1994'],"
                                                                                 " ['C234', 'M', 40, "
                                                                                 "676, 'Overweight', "
                                                                                 "300, '1-12-1977'], "
                                                                                 "['A001', 'F', 23, 456,"
                                                                                 " 'Normal', 14, '30-5-1994'],"
                                                                                 " ['C342', 'Male', 40, 676, "
                                                                                 "'Overweight', 300, '1-12-1977']"
                                                                                 ", ['D123', 'F', 55, 123, "
                                                                                 "'Obesity', 32, '15-01-1997'],"
                                                                                 " ['A001', 'F', 23, 456, 'Normal'"
                                                                                 ", 23, '30-5-1994'], ['C234',"
                                                                                 " 'M', 40, 676, 'Overweight', "
                                                                                 "300, '1-12-1977'], ['A001',"
                                                                                 " 'F', 23, 456, 'Normal', 14,"
                                                                                 " '30-5-1994'], ['C342', 'Male',"
                                                                                 " 40, 676, 'Overweight', 300, "
                                                                                 "'1-12-1977'], ['D123', 'F', "
                                                                                 "55, 123, 'Obesity', 32, "
                                                                                 "'15-01-1997']]")

    def test_04(self):
        # Try find a database that has the value 42
        # Should fail
        self.assertFalse(self.database_handler.get_person_information(42))

    def test_05(self):
        # Try save data to a database that has the value 42
        # Should fail
        self.assertFalse(self.database_handler.save_data(self.data, 42))

    def test_06(self):
        # Try save data to a database that has the name mydb
        # Should pass
        self.assertTrue(self.database_handler.save_data(self.data, 'mydb'))

    def test_07(self):
        # Try save data to a database that has the name mydb
        # but no data is passed in Should fail
        self.assertFalse(self.database_handler.save_data('mydb'))

    def test_08(self):
        # Try save data to a database but no data
        # is passed in to the method. Should fail
        self.assertFalse(self.database_handler.save_data())

    def test_09(self):
        # Try save data to a database but method is passed
        # the values None and False
        self.assertFalse(self.database_handler.save_data(None, False))
