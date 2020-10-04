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
    def __init__(self, id1, date, start_time, end_time, meeting_url, owner_name, owner_surname, participant_name, participant_surname):
        self.__id = id1
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.meeting_url = meeting_url
        self.owner = FullName(owner_name, owner_surname)
        self.participant = FullName(participant_name, participant_surname)

    def __repr__(self):
        fields = ['id', 'date', 'start_time', 'end_time', 'meeting_url', 'owner', 'participant']
        answer = [str(self.__id), self.date, self.start_time, self.end_time, self.meeting_url, self.owner, self.participant]
        s = ''
        for i in range(len(answer)):
            if answer[i] is not None:
                s += fields[i] + ': ' + str(answer[i]) + '\n'
            else:
                s += fields[i] + ': ' + 'none' + '\n'
        return s

    def compare(self, other):
        for param in {'__id', 'date', 'start_time', 'end_time', 'meeting_url', 'owner', 'participant'}:
            if getattr(self, param) != getattr(other, param):
                return False
        return True

    def search(self, value):
        return value in [self.__id, self.date, self.start_time, self.end_time, self.meeting_url, self.owner.get_name(), self.owner.get_surname(), self.participant.get_name(), self.participant.get_surname()]

    def get_field(self, param):
        if param in {'date', 'start_time', 'end_time', 'meeting_url', 'owner', 'participant'}:
            return getattr(self, param)
        elif param == 'id':
            return self.__id
        return None

    def change_field(self, param, value):
        if param in {'date', 'start_time', 'end_time', 'url'}:
            setattr(self, param, value)
        elif param == 'owner':
            self.owner.set_value(*value.split())
        elif param == 'participant':
            self.participant.set_value(*value.split())