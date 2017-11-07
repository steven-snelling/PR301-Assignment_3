from model.file_handler.shelve_file import ShelveFile
from model.file_handler.csv_file import CSVFile


class Interpreter:
    # Written By Thomas
    #
    # This is the base class for the model segment of the MVC Architecture
    # Handles flow of data from the various modules and into the view.
    #
    #
    def __init__(self, in_validator,
                 in_database_handler, in_file_path):

        self.data_arr = []
        self.my_validator = in_validator
        self.database_handler = in_database_handler
        self.default_file_path = in_file_path

    def get_data(self):
        return self.data_arr

    def serialize_data_arr(self, args=''):
        if args == '':
            ShelveFile().save_file(self.data_arr, self.default_file_path)
        else:
            ShelveFile().save_file(self.data_arr, args)

    def save_file(self, args=''):
        if args == '':
            CSVFile().save_file(self.data_arr, self.default_file_path)
        else:
            CSVFile().save_file(self.data_arr, args)

    def save_database(self, database_name='mydb'):
        self.database_handler.save_data(self.data_arr, database_name)

    def load_file(self, file_path):
        self.set_data_arr(CSVFile().load_file(file_path))

    def load_database(self, database_name='mydb'):
        self.set_data_arr(self.database_handler.get_person_information
                          (database_name))

    def add_manual_data(self, new_person_data):
        data = self.my_validator.validate_data(new_person_data)
        self.data_arr.append(data)
        return True

    def set_data_arr(self, dirty_data_arr):
        self.data_arr = self.my_validator.validate_data(dirty_data_arr)
