
class Interpreter:
    # Written By Thomas
    #
    # This is the base class for the model segment of the MVC Architecture
    # Handles flow of data from the various modules and into the view.
    #
    #
    def __init__(self, in_validator, in_file_handler,
                 in_database_handler, in_file_path):
        # Written By Thomas
        #
        # The interpreter requires a validator, file handler,
        # database handler and a default file path to work
        # correctly.
        #
        # data_arr contains arrays of person data that have been
        # validated by the validator. This should be done by
        # passing a dirty data Array into the set data array method
        #
        #
        self.data_arr = []
        self.my_validator = in_validator
        self.file_handler = in_file_handler
        self.database_handler = in_database_handler
        self.default_file_path = in_file_path

    def get_data(self):
        # Written By Thomas
        #
        # Returns the clean data array
        #
        #
        return self.data_arr

    def serialize_data_arr(self, args=''):
        try:
            if args == '':
                self.file_handler.shelve_file(self.data_arr,
                                              self.default_file_path)
            else:
                self.file_handler.shelve_file(self.data_arr, args)

        except OSError:
            print(OSError)
            return False

    def save_file(self, args=''):
        try:
            if args == '':
                self.file_handler.save_file(self.data_arr,
                                            self.default_file_path)
            else:
                self.file_handler.save_file(self.data_arr, args)

        except OSError as erro:
            print(erro)
            return False

    def save_database(self, database_name='mydb'):
        # Written By Thomas
        #
        # This method saves the data array to a database. The
        # method takes a database name as a parameter but will
        # default to mydb if none is provided.
        #
        #
        self.database_handler.save_data(self.data_arr, database_name)

    def load_file(self, file_path):
        # Written By Thomas
        #
        # This loads data in from a csv file. data from the file
        # is set through the set data arr function witch cleanses
        # the input data as well
        #
        #
        self.set_data_arr(self.file_handler.load_file(file_path))

    def load_database(self, database_name='mydb'):
        # Written By Thomas
        #
        # This brings the data in from a database.
        #
        # The data is set through the set data arr
        # so that any data is cleaned before use in
        # the system.
        #
        #
        self.set_data_arr(self.database_handler.get_person_information
                          (database_name))

    def add_manual_data(self, new_person_data):
        # Written By Thomas
        #
        # This operates a little differently to the
        # other add methods.
        #
        # this takes the data from the manual entry flow
        # and cleans is manualy then appends it directly to
        # the data array.
        #
        # This makes it possible for the user to add lines to
        # csv or database files through the system
        #
        #
        data = self.my_validator.validate_data(new_person_data)
        self.data_arr.append(data)
        return True

    def set_data_arr(self, dirty_data_arr):
        # Written by Thomas
        #
        # This takes a dirty data array then passes it to the validators
        # validate function. arrays with problematic data in it will
        # be removed.
        #
        # Data that fits the criteria is sent toa  clean array then
        # returned.
        #
        self.data_arr = self.my_validator.validate_data(dirty_data_arr)
