import unittest
from .FileHandler import *


class FileHandlerTests(unittest.TestCase):
    """Written By Thomas

    This file provides test coverage for the file handler

    """

    def setUp(self):
        self.file_handler = FileHandler()
        self.data = [['A001', 'F', '23', '456', 'Normal', '23', '30-5-1994'],
                     ['C234', 'M', '5', '676', 'Overweight', '300', '1-12-1977'],
                     ['C4', 'Male', 'nine', '66,8', 'heavy', '3,00', '1-12-19']]

    def test_01(self):
        # forces the program to try load from the file
        # that hasnt been made. This should fail
        self.assertTrue(self.file_handler.load_file(), "[['A001', 'F', '23',"
                                                       " '456', 'Normal', '23',"
                                                       " '30-5-1994'], ['C234',"
                                                       " 'M', '5', '676', "
                                                       "'Overweight', '300', "
                                                       "'1-12-1977'], ['C4', "
                                                       "'Male', 'nine', '|66',"
                                                       " '8|', 'heavy', '|3', "
                                                       "'00|', '1-12-19']]")

    def test_02(self):
        # Gives the loader a path to the load
        # data file this should be true
        self.assertTrue(self.file_handler.load_file('../_load_files/first.csv'))

    def test_03(self):
        # Gives the loader an int to the load
        # data file this should fail
        self.assertFalse(self.file_handler.load_file(123))

    def test_04(self):
        # Gives the loader a string with spaces to load
        # this should fail
        self.assertFalse(self.file_handler.load_file("data is here"))

    def test_05(self):
        # Gives the loader a string leading to a file
        # this should Pass
        self.assertTrue(self.file_handler.load_file("../../load_data.csv"))

    def test_06(self):
        # Appends some data to a csv file then loads it back in
        data_arr = self.data
        data_arr.append(['C4', 'Male', 'nine', '66,8', 'heavy', '234', 'forty'])
        self.file_handler.save_file(data_arr)
        self.assertTrue(self.file_handler.load_file(), "[['A001', 'F', '23',"
                                                       " '456', 'Normal', '23',"
                                                       " '30-5-1994'], ['C234',"
                                                       " 'M', '5', '676', "
                                                       "'Overweight', '300', "
                                                       "'1-12-1977'], ['C4', "
                                                       "'Male', 'nine', '|66',"
                                                       " '8|', 'heavy', '|3', "
                                                       "'00|', '1-12-19'], "
                                                       "['C4', 'Male', "
                                                       "'nine', '66,8', 'heavy',"
                                                       " '234', 'forty']]")

    def test_07(self):
        # Appends some data to a csv file then loads it back in to check
        # if the new data was ignored
        data_arr = self.data
        data_arr.append(123)
        self.file_handler.save_file(data_arr)
        self.assertTrue(self.file_handler.load_file(), "[['A001', 'F', '23',"
                                                       " '456', 'Normal', '23',"
                                                       " '30-5-1994'], ['C234',"
                                                       " 'M', '5', '676', "
                                                       "'Overweight', '300', "
                                                       "'1-12-1977'], ['C4', "
                                                       "'Male', 'nine', '|66',"
                                                       " '8|', 'heavy', '|3', "
                                                       "'00|', '1-12-19']]")

    def test_08(self):
        # appends a blank string to the array
        # should still succeed
        data_arr = self.data
        data_arr.append("")
        self.file_handler.save_file(data_arr)
        self.assertTrue(self.file_handler.load_file(), "[['A001', 'F', '23',"
                                                       " '456', 'Normal', '23',"
                                                       " '30-5-1994'], ['C234',"
                                                       " 'M', '5', '676', "
                                                       "'Overweight', '300', "
                                                       "'1-12-1977'], ['C4', "
                                                       "'Male', 'nine', '|66',"
                                                       " '8|', 'heavy', '|3', "
                                                       "'00|', '1-12-19']]")

    def test_09(self):
        # appends self. data to data_arr
        # because this isnt the correct type it should be ignored
        data_arr = self.data
        data_arr.append(self.data)
        self.file_handler.save_file(data_arr)
        self.assertTrue(self.file_handler.load_file(), "[['A001', 'F', '23',"
                                                       " '456', 'Normal', '23',"
                                                       " '30-5-1994'], ['C234',"
                                                       " 'M', '5', '676', "
                                                       "'Overweight', '300', "
                                                       "'1-12-1977'], ['C4', "
                                                       "'Male', 'nine', '|66',"
                                                       " '8|', 'heavy', '|3', "
                                                       "'00|', '1-12-19']]")
