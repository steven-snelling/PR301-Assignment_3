from model.database.i_database import IDatabase
import sqlite3


class Database(IDatabase):
    # Written By Thomas
    #
    # This handles the connection with the database.
    #
    #
    def __init(self):
        # Written By Thomas
        #
        # Initializes the conn and cursor variables but
        # assigns them a value of None.
        #
        # This is so that i can reassign them when i need to
        #
        #
        self.conn = None
        self.cursor = None

    def create_connection(self, database_name):
        # Written by Thomas
        #
        # Creates the connection with the database.
        #
        # Tries to make the connection but handles the error if
        # no connection can be made.
        #
        # If it is successful the conn atribute is given the connection object
        # and the cusor the cursor object.
        #
        # It then calls the make_tables method.
        #
        #

        try:
            self.conn = sqlite3.connect(database_name)
            self.cursor = self.conn.cursor()
            self.make_tables()
            return False
        except ConnectionError:
            print(ConnectionError)
        except TypeError as err:
            print(err)

    def make_tables(self):
        # Written By Thomas
        #
        # This is called from the create connection method.
        # It makes the table within the database.
        #
        # This only happens if the table doesnt exist.
        #
        #

        make_table = """CREATE TABLE IF NOT EXISTS employees ( EMPID VARCHAR(6),
                 Gender CHAR, age INTERGER, sales INTERGER
                , bmi VARCHAR(15), salary INTERGER, birthday DATE);"""
        self.cursor.execute(make_table)
        self.conn.commit()

    def insert_person(self, data_arr):
        # Written by Thomas
        #
        # This method takes an array of arrays which hold the data to do
        # with the person. it then generates an insert string then
        # executes this on the database.
        #
        #

        try:
            for person in data_arr:
                insert_string = """INSERT INTO employees (EMPID ,Gender, age, sales, bmi, salary, birthday)
                 VALUES ("{empID}", "{gender}", "{age}", "{sales}", "{bmi}",
                  "{salary}", "{birthday}");"""
                try:
                    insert_command = insert_string.format(empID=person[0],
                                                          gender=person[1],
                                                          age=person[2],
                                                          sales=person[3],
                                                          bmi=person[4],
                                                          salary=person[5],
                                                          birthday=person[6])
                    self.cursor.execute(insert_command)
                    self.conn.commit()
                except IndexError as err:
                    print(err)
                    return False

        except AttributeError as err:
            print(err)
            return False
        except UnboundLocalError as err:
            print(err)
            return False
        except TypeError as err:
            print(err)
            return False
        return True

    def select_person_data(self):
        # Written By Thomas
        #
        # This gets all the employee data from the data base then adds them to
        # an array. The array is then returned to be formatted
        #
        #

        data_arr = []
        try:
            self.cursor.execute("Select * from employees")
            result = self.cursor.fetchall()
            for r in result:
                data_arr.append(r)
            return data_arr
        except AttributeError as err:
            print(err)
            return False

    @staticmethod
    def format_incoming_db_info(raw_arr):
        # Written By Thomas
        #
        # This takes an tuple of person data and splits it into useable
        # arrays. This was needed because the validator only allows for
        # array of arrays to be input to be validated so i needed to
        # reformat the retrieved data to a usable form
        #
        #

        person_data_arr = []
        try:
            for a_tuple in raw_arr:
                data_arr = []
                try:
                    for data in a_tuple:
                        data_arr.append(data)
                    person_data_arr.append(data_arr)
                except TypeError as oops:
                    print(oops)
            return person_data_arr
        except TypeError as oops:
            print(oops)

    def get_person_information(self, database_name='mydb'):
        # Written By Thomas
        #
        # This takes a database name (or defaults to mydb) then
        # connects to it.
        #
        # It then reformats and returns the data it can retrieve from the
        # select all statement
        #
        #

        self.create_connection(database_name)
        return self.format_incoming_db_info(self.select_person_data())

    def save_data(self, data_arr, database_name='mydb'):
        # Written By Thomas
        #
        # This creates a database connection from the given name then
        # calls the insert person method passing in the clean data
        # array that is given to this method.
        #
        #
        #

        self.create_connection(database_name)
        try:
            if self.insert_person(data_arr):
                return True
            else:
                return False
        except RuntimeError:
            print("Error inserting the data into the database")
            return False
