class Logger:

    def __init__(self, file_name):
        self.file_name = file_name

    def write_to_file(self, li):
        f = open(self.file_name, 'w+')
        for i in li:
            f.write(i + '\n')
        f.close()


class Observer:

    def __init__(self, file_name):
        self.actions = []
        self.log = Logger(file_name)

    def upgrade(self, action):
        self.actions.append(action)
        self.log.write_to_file(self.actions)
        print('All actions:', self.actions)

    def __repr__(self):
        return 'All actions: ' + ','.join(self.actions)


class Event:
    def __init__(self, events, ll: Observer):
        self.events = {event: dict() for event in events}
        self.all_actions = events
        self.ll = ll

    def get_events(self, event):
        return self.events[event]

    def add(self):
        for i in self.all_actions:
            callback = getattr(self.ll, 'upgrade')
            self.get_events(i)[self.ll] = callback

    def notify(self, event1):
        for event, callback in self.get_events(event1).items():
            callback(event1)


