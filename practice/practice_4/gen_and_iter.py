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


def generator_random_number(n, a, b):
    while n > 0:
       n -= 1
       yield randint(a, b)