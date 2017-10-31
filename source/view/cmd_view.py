from view.i_cmd_view import ICmdView


class CmdView(ICmdView):
    @staticmethod
    def show(show_string):
        print(show_string)

    @staticmethod
    def read(prompt):
        return input(prompt)

    def manual_person_flow(self):
        person_data_arr = []
        person_data = [self.read("Enter your employee ID: "),
                       self.read("Enter your gender: "),
                       self.read("Enter your age: "),
                       self.read("Enter your sales count: "),
                       self.read("Enter your BMI: "),
                       self.read("Enter your salary: "),
                       self.read("Enter your birthday, e.g. dd-mm-yyyy: ")]
        person_data_arr.append(person_data)
        return person_data_arr

