from datetime import datetime, date, time
import os
import re


class WrongLen(Exception):
    pass


class WrongId(Exception):
    pass


class WrongName(Exception):
    pass


class WrongDate(Exception):
    pass


class TimeConflict(Exception):
    pass


class WrongTime(Exception):
    pass


class WrongUrl(Exception):
    pass


class NotUnique(Exception):
    pass


unique_ind = []


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

    def check_len(func):
        def inner_method(self):
            try:
                if len(self.ls) < 9:
                    raise WrongLen
            except WrongLen:
                print('wrong len')
                return
            else:
                return func(self)
        return inner_method

    def validate_id(func):
        def inner_method(self):
            try:
                if self.ls[0].isdigit() is False:
                    raise WrongId
            except WrongId:
                print('wrong id')
                return
            else:
                return func(self)
        return inner_method

    def validate_unique(func):
        def inner_method(self):
            if self.action == 'edit':
                return func(self)
            try:
                if unique_ind.count(self.ls[0]) > 1:
                    unique_ind.remove(self.ls[0])
                    raise NotUnique
            except NotUnique:
                print('id not unique')
                return
            else:
                return func(self)
        return inner_method

    def validate_name(func):
        def inner_method(self):
            try:
                if False in [self.ls[5].isalpha(), self.ls[6].isalpha(), self.ls[7].isalpha(), self.ls[8].isalpha()]:
                    raise WrongName
            except WrongName:
                print('wrong name')
                return
            else:
                return func(self)
        return inner_method

    def validate_date(func):
        def inner_method(self):
            try:
                dt = datetime.strptime(self.ls[1], "%d.%m.%Y")
            except:
                print('wrong date')
                return
            else:
                return func(self)
        return inner_method

    def validate_time(func):
        def inner_method(self):
            try:
                dt1 = datetime.strptime(self.ls[1] + ' ' + self.ls[2], "%d.%m.%Y %H:%M")
                dt2 = datetime.strptime(self.ls[1] + ' ' + self.ls[3], "%d.%m.%Y %H:%M")
                if dt1 > dt2:
                    raise TimeConflict
            except:
                print('wrong time')
                return
            else:
                return func(self)
        return inner_method

    def validate_url(func):
        def inner_method(self):
            try:
                result = re.match(r'^(?:http|ftp)s?:\/(?:\/[\w.?=]+){2,}$', self.ls[4])
                if result is None:
                    raise WrongUrl
            except WrongUrl:
                print('wrong url')
                return
            else:
                return func(self)
        return inner_method

    @check_len
    @validate_id
    @validate_url
    @validate_name
    @validate_date
    @validate_time
    @validate_unique
    def __call__(self):
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