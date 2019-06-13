import json

class studentsDB:
    def __init__(self):
        self.__data=None
    def connect (self,data_file):
        with open (data_file)as json_file:
    def get__data(self,name):
        for student in self.__data['students']:
            if student ['name'] == name
            return student

    def close(self):
        pass