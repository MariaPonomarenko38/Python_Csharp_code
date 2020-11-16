from Ponomarenko_pmi25.programming.programming_4.online_meeting import OnlineMeeting
from Ponomarenko_pmi25.programming.programming_4.validation import Validate, validate_input
from datetime import datetime as dt


class Meetings:

    def __init__(self):
        self.meetings = []

    def add_to_list(self, meeting: OnlineMeeting):
        self.meetings.append(meeting)

    def remove_from_list(self, id):
        for i in range(len(self.meetings)):
            if self.meetings[i].get_field('id') == int(id):
                del self.meetings[i]
                return

    def change(self, ind, param, value):
        self.meetings[ind - 1].change_field(param, value)

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

    def add(self, file, val):
        if len(self.meetings) == 0:
            print('Your list is empty! Fill it first from file!')
            return
        arg = val.split()
        arg[0] = int(arg[0])
        self.add_to_list(OnlineMeeting(arg))
        self.rewrite_file(file)

    def remove(self, file, id):
        v = Validate([])
        v.remove_id(id)
        self.remove_from_list(id)
        self.rewrite_file(file)

    def edit(self, file, id, val):
        arg = val.split()
        if arg[0] != id:
            arg[0] = id
            print('You typed another id, it was ignored')
        arg[0] = int(arg[0])
        if len(self.meetings) > 1:
            for i in range(len(self.meetings)):
                if self.meetings[i].get_field('id') == int(id):
                    self.meetings[i] = OnlineMeeting(arg)
        self.rewrite_file(file)

    def fill_list_from_file(self, file):
        f = open(file, 'r')
        input_lines = f.readlines()
        for line in input_lines:
            if validate_input('add', True, line) is True:
                arg = line.split()
                arg[0] = int(arg[0])
                self.add_to_list(OnlineMeeting(arg))
            else:
                print('Meeting with id ' + line.split()[0] + ' is not correct')
                continue
        print('Well done!')
        return self


