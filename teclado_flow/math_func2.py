import json

class StudentDB:
    def __init__(self):
        self.__data = None

    def connect(self, data_file):
        with open(data_file) as json_file:
            self.__data = json.load(json_file)

    def get_data(self, name):
        for studend in self.__data['students']:
            if studend['name'] == name:
                return studend

    def close(self):
        pass