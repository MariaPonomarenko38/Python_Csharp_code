from Ponomarenko_pmi25.practice.practice_5.linked_list import LinkedList
from Ponomarenko_pmi25.practice.practice_5.iterator import creating_sequence
from Ponomarenko_pmi25.practice.practice_5.validation import validate_file_input, validate_input
import types


class Strategy:
    def __init__(self, strategy=None):
        self.option = 0
        if strategy is not None:
            self.perform = types.MethodType(strategy, self)

    def perform(self):
        print(self.option)


def strategy1(self):
    pos = validate_input('position to insert', self.ll.length())
    n = validate_input('quantity of elements')
    a = validate_input('left border', self.ll.length())
    b = validate_input('right border', self.ll.length())
    ls = creating_sequence(a, b, n)
    self.ll.insert_list(pos, ls)
    return self.ll


def strategy2(self):
    pos = validate_input('position to insert', self.ll.length())
    file_name = validate_file_input()
    f = open(file_name, 'r')
    ls = [int(i) for i in ''.join(f.readlines()).split()]
    self.ll.insert_list(pos, ls)
    return self.ll


if __name__ == '__main__':
    strategy = Strategy()
    linked_list = LinkedList()
    while True:
        print('''Choose option:
        1. Strategy 1 for inserting in list
        2. Strategy 2 for inserting in list
        3. Generating data
        4. Delete element by position
        5. Delete range of elements
        6. Negative cycle and reversing positive elements
        7. Print list
        8. Exit
        ''')
        option = validate_input('option')
        if option == 1:
            strategy = Strategy(strategy1)
        elif option == 2:
            strategy = Strategy(strategy2)
        elif option == 3:
            strategy.ll = linked_list
            linked_list = strategy.perform()
        elif option == 4:
            pos = validate_input('position to insert', linked_list.length(), 'delete')
            linked_list.pop_node(pos)
        elif option == 5:
            pos1 = validate_input('start_pos', linked_list.length())
            pos2 = validate_input('end_pos', linked_list.length())
            linked_list.pop_range_of_nodes(pos1, pos2)
        elif option == 6:
            k = validate_input('k')
            linked_list.negative_k_cycle(k)
            linked_list.reverse_positive()
        elif option == 7:
            print(linked_list)
        elif option == 8:
            break


