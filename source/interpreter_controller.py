from cmd import Cmd
from view.age_verse_salary_graph import AgeVerseSalaryGraph
from view.bmi_pie_graph import BmiPieGraph
from view.employees_by_gender_graph import EmployeesByGenderGraph
from view.sales_by_gender_graph import SalesByGenderGraph
from view.graph_view import GraphView

class InterpreterController(Cmd):
    # Written By Thomas
    #
    # This is the controller of the system. It defines what is to happen in the
    # cmdloop and the commands that are accosiated with it. It also
    # links the model (interpreter) to the view  (GraphView)
    #

    def __init__(self, in_view, in_interpreter):
        Cmd.__init__(self)
        self.prompt = '> '
        self.my_view = in_view
        self.my_interpreter = in_interpreter

    @staticmethod
    def check_set_file_path(running_args):
        if len(running_args) > 2:
            print("too many arguments supplied")
            return running_args[0]
        try:
            open(running_args[1], 'r')
            return running_args[1]
        except OSError as erro:
            print(erro)
            print("Defaulting to working directory.")
            return running_args[0]
        except IndexError:
            print("No default path provided.")
            print("Defaulting to working directory.")
            return running_args[0]

    def do_add(self, *args):
        """
        ***
        OPTIONS
            -l : This loads the information from a file. The file is given to the command as a string.
            -m : This is for manual data entry. The user will be prompted \
for the information in steps after entering this option.
            -d : This loads the information into the system from a database.
        ***
        """

        options_arr = self.parse_args(args)
        option_dict = {
            '-l': self.my_interpreter.load_file,
            '-m': self.manual_add,
            '-d': self.my_interpreter.load_database
        }
        self.find_in_dict(options_arr, option_dict)

    def do_save(self, *args):
        """
        ***
        OPTIONS
                        -s : This is a standard save. The information is saved to a file in \
the saves folder in the program files. (object is serialized)
                        -d : This saves the current information to the database.
                        -f : This saves a file to the specified file location.
        ***
        """

        options_arr = self.parse_args(args)
        option_dict = {
            '-f': self.my_interpreter.save_file,
            '-d': self.my_interpreter.save_database,
            '-s': self.my_interpreter.serialize_data_arr
        }
        self.find_in_dict(options_arr, option_dict)

    def do_show(self, *args):
        """
        ***
        OPTIONS
                    -a : Shows a bar graph of the total sales made by males verse the total sales made by female.
                    -b : Shows a pie chart of the percentage of female workers verse male workers
                    -c : Shows a scatter plot graph of peoples age verse their salary.
                    -d : Shows a pie chart of the BMI of a set of people.
        ***
        """

        options_arr = self.parse_args(args)
        option_dict = {
            '-a': SalesByGenderGraph(),
            '-b': EmployeesByGenderGraph(),
            '-c': AgeVerseSalaryGraph(),
            '-d': BmiPieGraph()
        }

        for key, value in option_dict.items():
            if options_arr[0] == key:
                builder = value
                director = GraphView(builder)
                director.make_graph(self.my_interpreter.get_data())
                builder.show_graph()

    @staticmethod
    def do_quit(arg):
        """
        Closes the program
        """
        # Written By Thomas
        #
        # If quit is typed into the cmd. it quits.
        quit()

    # This is just a shortcut to the quit command.
    do_q = do_quit

    @staticmethod
    def parse_args(arg_str):
        try:
            arg_arr = None
            for arg in arg_str:
                arg_arr = arg.split(' ')
            if len(arg_arr) > 2:
                return "Too many arguments were given"
            else:
                return arg_arr
        except IndexError:
            return False

    def manual_add(self):
        self.my_interpreter.add_manual_data(self.my_view.manual_person_flow())

    def find_in_dict(self, options_arr, options_dict):
        arg_found = False
        for key, value in options_dict.items():
            if options_arr[0] == key:
                if not self.try_launch(key, value, options_arr):
                    return
                else:
                    return
        if not arg_found:
            return

    @staticmethod
    def try_launch(key, value, options_arr):
        if key == '-m':
            value()
            return True
        else:
            if len(options_arr) == 2:
                value(options_arr[1])
                return True
            else:
                return False
