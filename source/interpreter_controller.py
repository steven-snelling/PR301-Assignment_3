from cmd import Cmd


class InterpreterController(Cmd):
    # Written By Thomas
    #
    # This is the controller of the system. It defines what is to happen in the
    # cmdloop and the commands that are accosiated with it. It also
    # links the model (interpreter) to the view  (GraphView)
    #

    def __init__(self, in_view, in_graph_view, in_interpreter):
        # Written By Thomas
        #
        # The InterpreterController Object is given a view and
        # an interpreter object and is assigned to the respective
        # attribute in the controller object.
        #
        # The prompt for the cmd interface is also defined from here.
        #
        #
        Cmd.__init__(self)
        self.prompt = '> '
        self.my_view = in_view
        self.my_graph_view = in_graph_view
        self.my_interpreter = in_interpreter

    @staticmethod
    def check_set_file_path(running_args):
        # Written By Thomas
        #
        # This is the part of the system that allows for command line arguments.
        # The functionality provided here is the user is able to supply a default
        # path to where they would like to store their files when they are saved.
        #
        # It is handled by taking the sys.argsv then checking if there
        # was only onestring provided. then it checks if the path is accessible.
        #
        # If it is the default is set. otherwise it defaults to the main and
        # continues working.
        #

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
        # Vaishali
        """
        ***
        OPTIONS
            -l : This loads the information from a file. The file is given to the command as a string.
            -m : This is for manual data entry. The user will be prompted \
for the information in steps after entering this option.
            -d : This loads the information into the system from a database.
        ***
        """
        # Written By Thomas
        #
        # This is the add command in the cmd. The dictionary maps
        # options to their respective commands. When the command is invoked
        # the dict is made then is sent to the find in dict to match the
        # arguments with the dict options.
        #
        #
        options_arr = self.parse_args(args)
        option_dict = {
            '-l': self.my_interpreter.load_file,
            '-m': self.manual_add,
            '-d': self.my_interpreter.load_database
        }
        self.find_in_dict(options_arr, option_dict)

    def do_save(self, *args):
        # Vaishali
        """
        ***
        OPTIONS
                        -s : This is a standard save. The information is saved to a file in \
the saves folder in the program files. (object is serialized)
                        -d : This saves the current information to the database.
                        -f : This saves a file to the specified file location.
        ***
        """
        # Written by Thomas
        #
        # This creates a dictionary mapping the options to the respective
        # methods then sends that information to the find in dict method
        # for matching
        #
        #
        options_arr = self.parse_args(args)
        option_dict = {
            '-f': self.my_interpreter.save_file,
            '-d': self.my_interpreter.save_database,
            '-s': self.my_interpreter.serialize_data_arr
        }
        self.find_in_dict(options_arr, option_dict)

    def do_show(self, *args):
        # Vaishali
        """
        ***
        OPTIONS
                    -a : Shows a bar graph of the total sales made by males verse the total sales made by female.
                    -b : Shows a pie chart of the percentage of female workers verse male workers
                    -c : Shows a scatter plot graph of peoples age verse their salary.
                    -d : Shows a pie chart of the BMI of a set of people.
        ***
        """

        # Written by Thomas
        #
        # This creates a dictionary mapping the options to the respective
        # methods then because the commands are run differently the command is
        # matched in the method then the value is launched in the view.
        #
        #
        options_arr = self.parse_args(args)
        option_dict = {
            '-a': self.my_graph_view.sales_by_gender_graph,
            '-b': self.my_graph_view.employees_by_gender_graph,
            '-c': self.my_graph_view.age_verse_salary_graph,
            '-d': self.my_graph_view.bmi_pie_graph
        }
        for key, value in option_dict.items():
            if options_arr[0] == key:
                value(self.my_interpreter.get_data())

    @staticmethod
    def do_quit(arg):
        # Steven
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
        # Written by Thomas
        #
        # This method takes a argument string which is a string of options
        # given to the interpreter after a command has been invoked. It
        # then splits this string up everytime it finds a blank space.
        #
        # The resulting array is then returned to the calling function.
        #
        #
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
        # Written By Thomas
        #
        # This simply invokes the manual data entry flow in the
        # view then passes that information into the add manual
        # data in the model.
        #
        #
        self.my_interpreter.add_manual_data(self.my_view.manual_person_flow())

    def find_in_dict(self, options_arr, options_dict):
        # Written By Thomas
        #
        # This function is given an array of options and an option
        # dictionary from the calling method. It then goes through
        # the dictionary trying to match a given option with an
        # existing command.
        #
        # When a matching is found the try_launch method is called
        # which launches the value at the corresponding matched key.
        #
        #
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
        # Written By Thomas
        #
        # Is given a matched option and key value pair.
        # The key is checked to make sure it isnt -m because
        # this acts differntly. if it is the value is ran on its own.
        #
        # if it isnt the options array needs to have exactly 2 items
        # otherwise it will fail if it has 2 item the value is ran.
        #
        if key == '-m':
            value()
            return True
        else:
            if len(options_arr) == 2:
                value(options_arr[1])
                return True
            else:
                return False
