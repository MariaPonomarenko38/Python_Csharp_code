from Ponomarenko_pmi25.practice.practice_5.linked_list import LinkedList
from Ponomarenko_pmi25.practice.practice_5.iterator import creating_sequence
from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):

    @abstractmethod
    def method(self):
        pass


class Strategy1(Strategy):

    def __init__(self, ll: LinkedList, n, a, b, pos):
        self.ll = ll
        self.n = n
        self.a = a
        self.b = b
        self.pos = pos

    def method(self):
        ls = creating_sequence(self.a, self.b, self.n)
        self.ll.insert_list(self.pos, ls)
        return self.ll


class Strategy2(Strategy):

    def __init__(self, ll: LinkedList, pos, file_name):
        self.ll = ll
        self.pos = pos
        self.file_name = file_name

    def method(self):
        f = open(self.file_name, 'r')
        ls = [int(i) for i in ''.join(f.readlines()).split()]
        self.ll.insert_list(self.pos, ls)
        return self.ll




