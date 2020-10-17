from Ponomarenko_pmi25.programming.programming_5.decorators import *
import os

unique_ind = []


class NotUnique(Exception):
    pass


class Validate:

    def __init__(self, ls, action):
        self.ls = ls
        self.action = action
        if len(ls) != 0:
            unique_ind.append(ls[0])

    def remove_id(self, id):
        global unique_ind
        if id in unique_ind:
            unique_ind.remove(id)

    @check_len
    @validate_id
    @validate_url
    @validate_name
    @validate_date
    @validate_time
    def __call__(self):
        if self.action != 'edit' and unique_ind.count(self.ls[0]) > 1:
            unique_ind.remove(self.ls[0])
            print('id is not  unique')
            return None
        return self.ls


def validate_file_input():
    while True:
        file = input('Input name of your file: ')
        try:
            if not os.path.isfile(file):
                raise FileExistsError
        except FileExistsError:
            print('File not exists, try again')
        else:
            return file


def file_exist(file):
    try:
        if not os.path.isfile(file):
            raise FileExistsError
    except FileExistsError:
        print('File not exists')