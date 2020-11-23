from Ponomarenko_pmi25.practice.practice_7.strategy import Strategy1, Strategy2


class Context:
    def __init__(self, num):
        self.strategy = num

    def change_strategy(self, num):
        self.strategy = num

    def do(self, *args):
        if self.strategy == 1:
            e = Strategy1(*args)
        else:
            e = Strategy2(*args)
        return e.method()

    def get_strategy(self):
        return self.strategy