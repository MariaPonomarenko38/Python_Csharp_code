from datetime import datetime, date, time
import os


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

    def validate_file_while_filling(self):
        try:
            self.validate_all1('file')
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
        return True

    def check_len(self):
        if len(self.ls) < 9:
            raise WrongLen

    def validate_id(self):
        if self.ls[0].isdigit() is False:
            raise WrongId

    def validate_unique(self):
        if unique_ind.count(self.ls[0]) > 1:
            unique_ind.remove(self.ls[0])
            raise NotUnique

    def validate_name(self):
        if False in [self.ls[5].isalpha(), self.ls[6].isalpha(), self.ls[7].isalpha(), self.ls[8].isalpha()]:
            raise WrongName

    def validate_date(self):
        try:
            dt = datetime.strptime(self.ls[1], "%d.%m.%Y")
        except:
            raise WrongDate

    def validate_time(self):
        try:
            dt1 = datetime.strptime(self.ls[1] + ' ' + self.ls[2], "%d.%m.%Y %H:%M")
            dt2 = datetime.strptime(self.ls[1] + ' ' + self.ls[3], "%d.%m.%Y %H:%M")
            if dt1 > dt2:
                raise TimeConflict
        except:
            raise WrongTime

    def validate_url(self):
        if self.ls[4].find('http://') != 0:
            raise WrongUrl


def validate_input(s):
    while True:
        try:
            new_meeting = input('Input info for new meeting or -1: ')
            v = Validate(new_meeting.split())
            v.validate_all1(s)
        except WrongLen:
            print('wrong len')
        except WrongId:
            print('wrong id')
        except NotUnique:
            print('id is not unique')
        except WrongDate:
            print('wrong date')
        except WrongTime:
            print('wrong time')
        except TimeConflict:
            print('start time bigger than end time')
        except WrongUrl:
            print('wrong url')
        except WrongName:
            print('name/surname of owner/participant contains non-letters')
        else:
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