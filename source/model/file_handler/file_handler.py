from abc import ABCMeta, abstractmethod


class FileHandler(metaclass=ABCMeta):

    def load_file(self, file_path):
        try:
            data_arr = self.load(file_path)
        except FileNotFoundError:
            print("File ", file_path, " was not found")
            return False
        except OSError:
            print("file path cant be int")
            return False
        except TypeError:
            print("hello")
        return data_arr

    def save_file(self, data_arr, file_path):
        try:
            self.save(data_arr, file_path)
        except FileNotFoundError:
            print("File ", file_path, " was not found")
            return False
        except Exception as err:
            print(err)
            return False
        return True

    @staticmethod
    @abstractmethod
    def save(data_arr, file_path):
        pass

    @staticmethod
    @abstractmethod
    def load(file_path):
        pass
