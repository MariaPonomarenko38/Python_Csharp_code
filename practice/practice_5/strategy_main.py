from Ponomarenko_pmi25.practice.practice_5.linked_list import LinkedList
from Ponomarenko_pmi25.practice.practice_5.iterator import creating_sequence
from Ponomarenko_pmi25.practice.practice_5.validation import validate_file_input, validate_input


class Strategy:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def change_to_first(self):
        self.strategy = 1
        print('Changed to strategy 1')

    def change_to_second(self):
        self.strategy = 2
        print('Changed to strategy 2')

    def get_strategy(self):
        return self.strategy

    def __repr__(self):
        return str(self.strategy)


strategy = Strategy(0)
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
        strategy.change_to_first()
    elif option == 2:
        strategy.change_to_second()
    elif option == 3 and strategy.get_strategy() == 1:
        print('!!!!!!!!!!!')
        pos = validate_input('position to insert', linked_list.length())
        n = validate_input('quantity of elements')
        a = validate_input('left border', linked_list.length())
        b = validate_input('right border', linked_list.length())
        ls = creating_sequence(a, b, n)
        linked_list.insert_list(pos, ls)
    elif option == 3 and strategy.get_strategy() == 2:
        pos = validate_input('position to insert', linked_list.length())
        file_name = validate_file_input()
        f = open(file_name, 'r')
        ls = [int(i) for i in ''.join(f.readlines()).split()]
        linked_list.insert_list(pos, ls)
    elif option == 3 and strategy.get_strategy() == 0:
        print('You should choose a strategy')
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


