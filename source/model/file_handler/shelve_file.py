from model.file_handler.file_handler import FileHandler
import shelve


class ShelveFile(FileHandler):

    @staticmethod
    def load(file_path):
        raise NotImplementedError("This method has not been"
                                  " implemented")

    @staticmethod
    def save(data_arr, file_path='data.shelf'):
        count = 0
        d = shelve.open(file_path, 'c')
        for person in data_arr:
            count = count + 1
            d[str(count)] = person
        d.close()
