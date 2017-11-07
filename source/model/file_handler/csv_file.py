from model.file_handler.file_handler import FileHandler
import csv


class CSVFile(FileHandler):

    @staticmethod
    def load(file_path='data.csv'):
        data_arr = []

        with open(file_path, newline='') as file:
            read = csv.reader(file)
            for row in read:
                data_arr.append(row)

        return data_arr

    @staticmethod
    def save(data_arr, file_path='data.csv'):
        with open(file_path, 'w', newline='') as data_file:
            write = csv.writer(data_file, quotechar='|', delimiter=",",
                               quoting=csv.QUOTE_MINIMAL)
            for person in data_arr:
                    write.writerow(person)
