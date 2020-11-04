from abc import ABC, abstractmethod
from Ponomarenko_pmi25.programming.programming_6.online_meeting import OnlineMeeting
from Ponomarenko_pmi25.programming.programming_6.meetings import Meetings


class CurrentMemento:
    def __init__(self, condition: Meetings):
        self._condition = condition

    def get_condition(self):
        return self._condition

    def __repr__(self):
        s = ''
        for i in self._condition:
            s += i.str_format() + '\n'
        return s


class Creator:

    condition = None

    def __init__(self, ls: Meetings):
        self.condition = ls

    def change(self, ls: Meetings):
        self.condition = ls

    def current_condition(self):
        return CurrentMemento(self.condition)

    def restore(self, memento: CurrentMemento):
        self.condition = memento.get_condition()

    def get_condition_o(self):
        return self.condition


class Caretaker:
    id = -1

    def __init__(self, originator: Creator, max_size=5):
        self._mementos_undo = []
        self._creator = originator
        self.max_size = max_size

    def filling_stack(self):
        self.id += 1
        if len(self._mementos_undo) == self.max_size:
            self._mementos_undo.pop(0)
            self.id -= 1
        self._mementos_undo.insert(self.id, self._creator.current_condition())

    def undo_redo(self, action):
        if not len(self._mementos_undo):
            print('Nothing to undo')
            return
        if action == 'undo':
            if self.id == 0:
                print('Nothing to undo')
                return
            memento = self._mementos_undo[self.id - 1]
            self.id -= 1
        else:
            if self.id == 4:
                print('Nothing to redo')
                return
            memento = self._mementos_undo[self.id + 1]
            self.id += 1
        self._creator.restore(memento)
