from random import randint


class RandomNumber:
    def __init__(self, n, a, b):
        self.limit = n
        self.counter = 0
        self.left = a
        self.right = b

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return randint(self.left, self.right)
        else:
            raise StopIteration

    def __iter__(self):
        return self


def creating_sequence(a1, b1, n):
    if a1 > b1:
        a1, b1 = b1, a1
    s = []
    f = RandomNumber(n, a1, b1)
    for i in range(n):
        s.append(next(f))
    return s