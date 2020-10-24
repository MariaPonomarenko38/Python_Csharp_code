fields = ['id', 'date', 'start_time', 'end_time', 'meeting_url', 'owner', 'participant']


class FullName:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return self.name + ' ' + self.surname

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def set_value(self, name1=None, surname1=None):
        setattr(self, 'name', name1)
        setattr(self, 'surname', surname1)

    def lower1(self):
        a = self.name.lower() + self.surname.lower()
        return a


class OnlineMeeting:

    def __init__(self, args):
        for i, elem in enumerate(args):
            if i < 5:
                setattr(self, fields[i], elem)
        self.owner = FullName(args[5], args[6])
        self.participant = FullName(args[7], args[8])

    def __repr__(self):
        d1 = self.__dict__
        s = ''
        for i in d1:
            s += i + ': ' + str(d1[i]) + '\n'
        return s

    def str_format(self):
        d1 = self.__dict__
        s = ''
        for i in d1:
            s += str(d1[i]) + ' '
        s = s.rstrip(' ')
        return s


    def compare(self, other):
        d1 = self.__dict__
        for param in d1.keys():
            if getattr(self, param) != getattr(other, param):
                return False
        return True

    def search(self, value):
        d1 = self.__dict__
        for i in d1.values():
            i = str(i)
            if value in i[0:len(i)]:
                return True

    def get_field(self, param):
        d1 = self.__dict__
        if param in d1.keys():
            return getattr(self, param)

    def change_field(self, param, value):
        if param in {'date', 'start_time', 'end_time', 'meeting_url'}:
            setattr(self, param, value)
        elif param == 'owner':
            self.owner.set_value(*value.split())
        elif param == 'participant':
            self.participant.set_value(*value.split())