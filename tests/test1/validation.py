import re
from datetime import datetime, date, time


class WrongName(Exception):
    pass


class WrongPlace(Exception):
    pass


class WrongTime(Exception):
    pass


class WrongType(Exception):
    pass


def validate_name(func):
    def inner_method(self, *args):
        try:
            if False in [args[0].split()[0].isalpha()]:
                raise WrongName
        except WrongName:
            print('wrong name')
            return
        else:
            return func(self, *args)

    return inner_method


def validate_type(func):
    def inner_method(self, *args):
        try:
            if args[0].split()[1] not in ['econom', 'standart', 'comfort', 'minibus']:
                raise WrongType
        except WrongType:
            print('wrong type')
            return
        else:
            return func(self, *args)

    return inner_method


def validate_place(func):
    def inner_method(self, *args):
        try:
            if False in [args[0].split()[4].isalpha(), args[0].split()[5].isalpha()]:
                raise WrongPlace
        except WrongPlace:
            print('wrong place')
            return
        else:
            return func(self, *args)

    return inner_method


