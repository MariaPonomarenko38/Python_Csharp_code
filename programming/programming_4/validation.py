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
    def __init__(self, ls):
        self.ls = ls
        if len(ls) != 0:
            unique_ind.append(ls[0])

    def remove_id(self, id):
        global unique_ind
        if id in unique_ind:
            unique_ind.remove(id)

    def validate_all1(self, s):
        self.check_len()
        self.validate_id()
        if s != 'edit':
            self.validate_unique()
        self.validate_date()
        self.validate_time()
        self.validate_url()
        self.validate_name()


    def check_len(self):
        if len(self.ls) < 9:
            self.remove_id(self.ls[0])
            raise WrongLen

    def validate_id(self):
        if self.ls[0].isdigit() is False:
            self.remove_id(self.ls[0])
            raise WrongId

    def validate_unique(self):
        if unique_ind.count(self.ls[0]) > 1:
            unique_ind.remove(self.ls[0])
            raise NotUnique

    def validate_name(self):
        if False in [self.ls[5].isalpha(), self.ls[6].isalpha(), self.ls[7].isalpha(), self.ls[8].isalpha()]:
            self.remove_id(self.ls[0])
            raise WrongName

    def validate_date(self):
        try:
            dt = datetime.strptime(self.ls[1], "%d.%m.%Y")
        except:
            self.remove_id(self.ls[0])
            raise WrongDate

    def validate_time(self):
        try:
            dt1 = datetime.strptime(self.ls[1] + ' ' + self.ls[2], "%d.%m.%Y %H:%M")
            dt2 = datetime.strptime(self.ls[1] + ' ' + self.ls[3], "%d.%m.%Y %H:%M")
            if dt1 > dt2:
                self.remove_id(self.ls[0])
                raise TimeConflict
        except:
            self.remove_id(self.ls[0])
            raise WrongTime

    def validate_url(self):
        result = re.match(r'^(?:http|ftp)s?:\/(?:\/[\w.?=]+){2,}$', self.ls[4])
        if result is None:
            self.remove_id(self.ls[0])
            raise WrongUrl


def validate_input(action, if_file, data):
    try:
        if if_file is False:
            new_meeting = input('Input info for new meeting: ')
            v = Validate(new_meeting.split())
        else:
            new_meeting = data
            v = Validate(new_meeting.split())
        v.validate_all1(action)
    except WrongLen:
        print('wrong len')
        return False
    except WrongId:
        print('wrong id')
        return False
    except NotUnique:
        print('id is not unique')
        return False
    except WrongDate:
        print('wrong date')
        return False
    except WrongTime:
        print('wrong time')
        return False
    except TimeConflict:
        print('start time bigger than end time')
        return False
    except WrongUrl:
        print('wrong url')
        return False
    except WrongName:
        print('name/surname of owner/participant contains non-letters')
        return False
    else:
        if if_file:
            return True
        return new_meeting


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