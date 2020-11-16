from Ponomarenko_pmi25.programming.programming_6.decorators import *

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
                setattr(self, fields[i], args[i])
        self.owner = FullName(args[5], args[6])
        self.participant = FullName(args[7], args[8])

    @property
    def id(self):
        return self._id

    @id.setter
    @validate_id
    def id(self, val):
        self._id = val
        if self._id is not None:
            self._id = int(self._id)

    @property
    def date(self):
        return self._date

    @date.setter
    @validate_date
    def date(self, val):
        self._date = val

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    @validate_time
    def start_time(self, val):
        self._start_time = val

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    @validate_time
    def end_time(self, val):
        self._end_time = val

    @property
    def meeting_url(self):
        return self._meeting_url

    @meeting_url.setter
    @validate_url
    def meeting_url(self, val):
        self._meeting_url = val

    @property
    def owner(self):
        return self._owner

    @owner.setter
    @validate_name
    def owner(self, val: FullName):
        self._owner = val

    @property
    def participant(self):
        return self._participant

    @participant.setter
    @validate_name
    def participant(self, val: FullName):
        self._participant = val

    def __repr__(self):
        d1 = self.__dict__
        s = ''
        for i in d1:
            s += i.lstrip('_') + ': ' + str(d1[i]) + '\n'
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
        if '_'+param in d1.keys():
            return getattr(self, '_'+param)

    def exist(self):
        d1 = self.__dict__
        f = True
        for i in d1.values():
            if i is None:
                return False
        dt1 = datetime.strptime(self.start_time, "%H:%M")
        dt2 = datetime.strptime(self.end_time, "%H:%M")
        if dt1 > dt2:
            print('Time conflict')
            f = False
        return f

    def change_field(self, param, value):
        if param in {'date', 'start_time', 'end_time', 'meeting_url'}:
            setattr(self, param, value)
        elif param == 'owner':
            self.owner.set_value(*value.split())
        elif param == 'participant':
            self.participant.set_value(*value.split())

