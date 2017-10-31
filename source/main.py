# Written By Thomas
#
# This is the main file. The dependency injection is handled from here
# and the cmdloop is started.
#
#


from interpreter_controller import InterpreterController
from view.cmd_view import *
from model.interpreter import *
from model.file_handler.file_handler import *
from model.data_validation.data_validator import *
from model.database.database import *
import sys


if __name__ == '__main__':
    InterpreterController(CmdView(), Interpreter(
                            DataValidator(),
                            FileHandler(),
                            Database(),
                            InterpreterController.check_set_file_path(sys.argv)
                            )
                          ).cmdloop()
