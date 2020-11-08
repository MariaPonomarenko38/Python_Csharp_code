class Logger:

    @staticmethod
    def write_to_file(*args):
        f = open('output.txt', 'a')
        for i in args:
            f.write(str(i) + ' ')
        f.write('\n')
        f.close()


class Observer:
    observers = {}

    def __init__(self, event, callback):
        self.event = event
        self.observers[event] = callback

    def upgrade(self, action, *args):
        if action == self.event:
            self.observers[action](action, args)


class Event:
    def __init__(self):
        self.ll = []

    def add(self, a: Observer):
        if a not in self.ll:
            self.ll.append(a)

    def remove(self, a: Observer):
        if a in self.ll:
            self.ll.remove(a)

    def notify(self, *args):
        for i in self.ll:
            i.upgrade(*args)
