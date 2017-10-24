from model.data_validation.i_data_validator import IDataValidator
# from i_data_validator import IDataValidator
import re


# Written by Steven Snelling
class DataValidator(IDataValidator):

    def validate_data(self, dirty_data_arr):
        clean_people = []
        patterns = [
                    "^[A-Z][0-9]{3}$", "^[M|F]$",
                    "^[0-9]{2}$", "^[0-9]{3}$",
                    "^Normal|Overweight|Obesity|Underweight$",
                    "^[0-9]{2,3}$",
                    "^([0-9]{1,2})-([0-9]{1,2})-([0-9]{4})$"
        ]

        try:
            for dirty_person in dirty_data_arr:

                if len(dirty_person) == 7:
                    cleaned_person = []

                    for index, item in enumerate(dirty_person):

                        if self.__test_data(str(item), patterns[index]):
                            print("Valid data: ", str(item))
                            cleaned_person.append(str(item))

                else:
                    return "Not enough fields: " + str(len(dirty_person))

                filter(None, cleaned_person)

                print("Cleaned person after filter: ", cleaned_person)

                if len(cleaned_person) == 7:
                    clean_people.append(cleaned_person)

        except TypeError:
            print(TypeError)
            print("You have submitted the wrong data type")

        print("Cleaned people after filter: ", clean_people)

        return clean_people

    @staticmethod
    def __test_data(data, pattern):
        if re.compile(pattern).match(data):
            return True
        else:
            return False
