# Written By Thomas
#
# This defines the abstract methods for the FileHandler.
#
# If any of these methods are called without their
# implementation being defined in a child class, the
# NotImplemented error will be thrown.
# This results in the system closing however.
#
#


class IFileHandler(object):

    def load_file(self, file_path):
        raise NotImplementedError("An abstract method has not been"
                                  " implemented")

    def save_file(self, data_arr, file_path):
        raise NotImplementedError("An abstract method has not been"
                                  " implemented")

    def shelve_file(self, data_arr, file_path):
        raise NotImplementedError("An abstract method has not been"
                                  " implemented")
