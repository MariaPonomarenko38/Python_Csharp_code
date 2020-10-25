import re
from datetime import datetime, date, time


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


def check_len(func):
    def inner_method(self, *args):
        try:
            if len(args[0].split()) != 9:
                raise WrongLen
        except WrongLen:
            print('wrong  len')
            return
        else:
            return func(self, *args)

    return inner_method


def validate_id(func):
    def inner_method(self, *args):
        try:
            if args[0].split()[0].isdigit() is False:
                raise WrongId
        except WrongId:
            print('wrong id')
            return
        else:
            return func(self, *args)

    return inner_method


def validate_name(func):
    def inner_method(self, *args):
        try:
            if False in [args[0].split()[5].isalpha(), args[0].split()[6].isalpha(), args[0].split()[7].isalpha(), args[0].split()[8].isalpha()]:
                raise WrongName
        except WrongName:
            print('wrong name')
            return
        else:
            return func(self, *args)

    return inner_method


def validate_date(func):
    def inner_method(self, *args):
        try:
            dt = datetime.strptime(args[0].split()[1], "%d.%m.%Y")
        except:
            print('wrong date')
            return
        else:
            return func(self, *args)

    return inner_method


def validate_time(func):
    def inner_method(self, *args):
        try:
            dt1 = datetime.strptime(args[0].split()[1] + ' ' + args[0].split()[2], "%d.%m.%Y %H:%M")
            dt2 = datetime.strptime(args[0].split()[1] + ' ' + args[0].split()[3], "%d.%m.%Y %H:%M")
            if dt1 > dt2:
                raise TimeConflict
        except:
            print('wrong time')
            return
        else:
            return func(self, *args)

    return inner_method


def validate_url(func):
    def inner_method(self, *args):
        try:
            result = re.match(r'^(?:http|ftp)s?:\/(?:\/[\w.?=]+){2,}$', args[0].split()[4])
            if result is None:
                raise WrongUrl
        except WrongUrl:
            print('wrong url')
            return
        else:
            return func(self, *args)

    return inner_method


def validate_all(func):
    return check_len(validate_id(validate_url(validate_name(validate_date(validate_time(func))))))
