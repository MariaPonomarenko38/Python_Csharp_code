from Ponomarenko_pmi25.programming.programming_6.online_meeting import OnlineMeeting
from Ponomarenko_pmi25.programming.programming_6.decorators import *
from datetime import datetime as dt


class Meetings:

    unique_ind = []

    def __init__(self):
        self.meetings = []

    def add_to_list(self, meeting: OnlineMeeting):
        self.meetings.append(meeting)

    def remove_from_list(self, id):
        for i in range(len(self.meetings)):
            if self.meetings[i].get_field('id') == int(id):
                del self.meetings[i]
                return

    def change(self, ind, meeting: OnlineMeeting):
        self.meetings[ind] = meeting

    def __getitem__(self, item):
        return self.meetings[item]

    def print_list(self):
        for i in range(0, len(self.meetings)):
            print(self.meetings[i])

    def search_in_list(self, value):
        for i in self.meetings:
            if i.search(value):
                print(i)

    def compare(self, param, x, y):
        if param not in ['participant', 'owner', 'date'] and x > y:
            return True
        elif param in ['participant', 'owner']:
            if x.get_name().lower() > y.get_name().lower():
                return True
            elif x.get_name().lower() == y.get_name().lower() and x.get_surname().lower() > y.get_surname().lower():
                return True
        elif param == 'date':
            a = dt.strptime(x, "%d.%m.%Y")
            b = dt.strptime(y, "%d.%m.%Y")
            if a > b:
                return True
        return False

    def sort(self, param):
        for i in range(len(self.meetings)):
            for j in range(len(self.meetings) - i - 1):
                a = self.meetings[j].get_field(param)
                b = self.meetings[j + 1].get_field(param)
                if self.compare(param, a, b):
                    self.meetings[j], self.meetings[j + 1] = self.meetings[j + 1], self.meetings[j]

    def rewrite_file(self, file):
        with open(file, 'w') as f:
            for i, elem in enumerate(self.meetings):
                if i != len(self.meetings) - 1:
                    f.write(elem.str_format() + '\n')
                else:
                    f.write(elem.str_format())
        f.close()

    def add(self, val, file, param=None):
        arg = val.split()
        if len(arg) != 9:
            print('Not all arguments were inputed')
            return
        obj = OnlineMeeting(arg)
        if obj.exist():
            if self.unique_ind.count(arg[0]) == 0:
                self.add_to_list(obj)
                self.unique_ind.append(arg[0])
                if param is None:
                    self.rewrite_file(file)
            else:
                print('Id is not unique')

    def remove(self, file, id):
        if self.unique_ind.count(id) == 1:
            self.unique_ind.remove(id)
            self.remove_from_list(id)
            self.rewrite_file(file)
        else:
            print("Meeting with this id doesn't exist")

    def edit(self, val, file, id):
        arg = val.split()
        if len(arg) != 9:
            print('Not all arguments were inputed')
            return
        obj = OnlineMeeting(arg)
        if obj.exist():
            if arg[0] != id:
                arg[0] = id
                print('You typed another id, it was ignored')
            if len(self.meetings) > 1:
                for i in range(len(self.meetings)):
                    if self.meetings[i].get_field('id') == int(id):
                        self.meetings[i] = obj
            self.rewrite_file(file)

    def fill_list_from_file(self, file):
        f = open(file, 'r')
        input_lines = f.readlines()
        for line in input_lines:
            if len(line.split()) != 9:
                print('Not all arguments were inputed')
            else:
                self.add(line, file, 'file')
        print('Well done!')
        return self