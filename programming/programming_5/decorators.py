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


def validate_id(func):
    def inner_method(self, val):
        try:
            if val is None:
                return func(self, val)
            if str(val).isdigit() is False:
                raise WrongId
        except WrongId:
            print('wrong id')
            return
        else:
            return func(self, val)

    return inner_method


def validate_name(func):
    def inner_method(self, a):
        try:
            if a is None:
                return func(self, a)
            if False in [a.get_name().isalpha(), a.get_surname().isalpha()]:
                raise WrongName
        except WrongName:
            print('wrong name')
            return
        else:
            return func(self, a)

    return inner_method


def validate_date(func):
    def inner_method(self, val):
        try:
            if val is None:
                return func(self, val)
            dt = datetime.strptime(val, "%d.%m.%Y")
        except:
            print('wrong date')
            return
        else:
            return func(self, val)

    return inner_method


def validate_time(func):
    def inner_method(self, val):
        try:
            if val is None:
                return func(self, val)
            dt1 = datetime.strptime(val, "%H:%M")
        except:
            print('wrong time')
            return
        else:
            return func(self, val)

    return inner_method


def validate_url(func):
    def inner_method(self, val):
        try:
            if val is None:
                return func(self, val)
            result = re.match(r'^(?:http|ftp)s?:\/(?:\/[\w.?=]+){2,}$', val)
            if result is None:
                raise WrongUrl
        except WrongUrl:
            print('wrong url')
            return
        else:
            return func(self, val)

    return inner_method
