from Ponomarenko_pmi25.programming.programming_4.online_meeting import OnlineMeeting
from Ponomarenko_pmi25.programming.programming_4.validation import Validate
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

    def sort(self, param):
        for i in range(len(self.meetings)):
            for j in range(len(self.meetings) - i - 1):
                x = self.meetings[j].get_field(param)
                y = self.meetings[j + 1].get_field(param)
                if param not in ['participant', 'owner', 'date'] and x > y:
                    self.meetings[j], self.meetings[j + 1] = self.meetings[j + 1], self.meetings[j]
                elif param in ['participant', 'owner'] and x.get_name().lower() > y.get_name().lower():
                    self.meetings[j], self.meetings[j + 1] = self.meetings[j + 1], self.meetings[j]
                elif param == 'date':
                    a = dt.strptime(x, "%d.%m.%Y")
                    b = dt.strptime(y, "%d.%m.%Y")
                    if a > b:
                        self.meetings[j], self.meetings[j + 1] = self.meetings[j + 1], self.meetings[j]

    def add(self, file, val):
        if len(self.meetings) == 0:
            print('Your list is empty! Fill it first from file!')
            return
        with open(file, 'a', encoding='utf-8') as f:
            f.write("\n" + val)
        arg = val.split()
        arg[0] = int(arg[0])
        self.add_to_list(OnlineMeeting(*arg))

    def remove(self, file, id):
        f = open(file, "r+")
        input_lines = f.readlines()
        f.truncate(0)
        f.close()
        with open(file, 'w', encoding='utf-8') as f:
            b = False
            for line in input_lines:
                if int(line.split()[0]) != int(id):
                    if b is False:
                        b = True
                        f.write(line.strip('\n'))
                    else:
                        f.write('\n' + line.strip('\n'))
        v = Validate([])
        v.remove_id(id)
        self.remove_from_list(id)

    def edit(self, file, id, val):
        arg = val.split()
        if arg[0] != id:
            arg[0] = id
            val = " ".join(arg)
            print('You typed another id, it was ignored')
        arg[0] = int(arg[0])
        f = open(file, "r+")
        input_lines = f.readlines()
        f.truncate(0)
        f.close()
        with open(file, 'w', encoding='utf-8') as f:
            b = False
            for line in input_lines:
                if int(line.split()[0]) != int(id):
                    if b is False:
                        b = True
                        f.write(line.strip('\n'))
                    else:
                        f.write('\n' + line.strip('\n'))
                else:
                    f.write("\n" + val)
        f.close()
        if len(self.meetings) > 1:
            for i in range(len(self.meetings)):
                if self.meetings[i].get_field('id') == int(id):
                    self.meetings[i] = OnlineMeeting(*arg)
                    return

    def fill_list_from_file(self, file):
        f = open(file, 'r')
        input_lines = f.readlines()
        for line in input_lines:
            v = Validate(line.split())
            if v.validate_file_while_filling() is True:
                arg = line.split()
                arg[0] = int(arg[0])
                self.add_to_list(OnlineMeeting(*arg))
            else:
                print('Meeting with id ' + line.split()[0] + ' is not correct')
                continue
        print('Well done!')
        return self


