# Written By Thomas
#
# This defines the abstract methods for the Database.
#
# If any of these methods are called without their
# implementation being defined in a child class, the
# NotImplemented error will be thrown. This results in the system
# closing however.
#
#


class IDatabase(object):

    def create_connection(self, database_name='mydb'):
        raise NotImplementedError("An abstract method has"
                                  " not been implemented")

    def insert_person(self, person_ob):
        raise NotImplementedError("An abstract method has"
                                  " not been implemented")

    def get_person_information(self):
        raise NotImplementedError("An abstract method has"
                                  " not been implemented")
