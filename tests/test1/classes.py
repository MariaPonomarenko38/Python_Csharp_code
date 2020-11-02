from Ponomarenko_pmi25.tests.test1.validation import *

import enum

fields = ['driver_name', 'Type', 'start_time', 'end_time', 'StartPlace', 'EndPlace ']


class Type(enum.Enum):
   econom = 1
   standart = 2
   comfort = 3
   minibus = 4


class Time:

    def __init__(self, time):
        self.hour = time.split(':')[0]
        self.minute = time.split(':')[1]

    def __repr__(self):
        return self.hour + ':' + self.minute

    def get_hour(self):
        return self.hour

    def get_minute(self):
        return self.minute

    def str_format(self):
        return self.hour + ':' + self.minute

    def __le__(self, other):
        return self.hour <= other.hour


class Taxi:

    def __init__(self, args):
        for i, elem in enumerate(args):
            if i != 2 and i != 3 and i != 1:
                setattr(self, fields[i], elem)
        self.start_time = Time(args[2])
        self.end_time = Time(args[3])
        self.type = Type[args[1]]

    def __repr__(self):
        d1 = self.__dict__
        s = ''
        for i in d1:
            if i == 'type':
                s += i + ': ' + d1[i].name + '\n'
            else:
                s += i + ': ' + str(d1[i]) + '\n'
        return s

    def get_field(self, param):
        d1 = self.__dict__
        if param == 'Type':
            return self.type
        if param in d1.keys():
            return getattr(self, param)


class Collection:
    def __init__(self):
        self.ls = []

    @validate_name
    @validate_type
    @validate_place
    def add_to_list(self, val):
        taxi = Taxi(val.split())
        s = 0
        ls1 = []
        for i in self.ls:
            if taxi.get_field('driver_name') == i.get_field('driver_name'):
                ls1.append(i)
        if len(ls1) == 0:
            self.ls.append(taxi)
            return
        else:
            k = 0
            for i in ls1:
                if (i.get_field('start_time') <= taxi.get_field('start_time') <= i.get_field('end_time')) is True and i.get_field('start_place') == taxi.get_field('start_place'):
                    print("It's impossible to add")
                    return
            self.ls.append(taxi)

    def max_time(self, n):
        d1 = dict()
        for i in self.ls:
            if d1.get((i.get_field('start_time').str_format(), i.get_field('end_time').str_format())) is None:
                d1[(i.get_field('start_time').str_format(), i.get_field('end_time').str_format())] = 1
            else:
                d1[(i.get_field('start_time').str_format(), i.get_field('end_time').str_format())] += 1
        d1 = {k: v for k, v in sorted(d1.items(), key=lambda item: item[1], reverse=True)}
        for i in d1:
            if n > 0:
                print(i, ':', d1[i])
            n -= 1

    def top_taxi(self, n, file):
        d1 = dict()
        for i in self.ls:
            if d1.get(i.get_field('Type')) is None:
                d1[i.get_field('Type')] = 1
            else:
                d1[i.get_field('Type')] += 1
        d1 = {k: v for k, v in sorted(d1.items(), key=lambda item: item[1], reverse=True)}
        f = open(file, 'w')
        for i in d1:
            if n > 0:
                f.write(i.name + ':' + str(d1[i]) + '\n')
            n -= 1
        f.close()

    def print1(self):
        for i in self.ls:
            print(i)

    def fill_list_from_file(self, file):
        f = open(file, 'r')
        input_lines = f.readlines()
        for line in input_lines:
            self.add_to_list(line)
        print('Well done!')
        return self