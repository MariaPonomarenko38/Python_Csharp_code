from Ponomarenko_pmi25.practice.practice_7.linked_list import LinkedList
from Ponomarenko_pmi25.practice.practice_7.validation import *
from Ponomarenko_pmi25.practice.practice_7.observer import *
from Ponomarenko_pmi25.practice.practice_7.context import Context
from threading import Thread


class Object:

    def __init__(self, li, size=2):
        self.arguments = li
        self.size = size

    def get_list_for_each(self):
        result = []
        c = len(self.arguments) // self.size
        for i in range(0, len(self.arguments), c):
            a = []
            for j in range(i, i + c):
                a.append(self.arguments[j])
            result.append(a)
        return result


def create_thread(li_of_funcs, obj: Object):
    args1 = obj.get_list_for_each()
    for i in range(len(li_of_funcs)):
        thread = Thread(target=li_of_funcs[i], args=(*args1[i],))
        thread.start()
        thread.join()


def create_first_strategy(linked_list: LinkedList):
    n = validate_input('quantity of elements')
    a = validate_input('left_border', linked_list.length())
    b = validate_input('right_border', linked_list.length())
    pos = validate_input('position', linked_list.length())
    linked_list = context.do(linked_list, n, a, b, pos)
    return linked_list


def create_second_strategy(linked_list: LinkedList):
    pos = validate_input('position', linked_list.length())
    file_name = validate_file_input()
    linked_list = context.do(linked_list, pos, file_name)
    return linked_list


linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

linked_list_1.event.add(Observer('add', Logger.write_to_file))
linked_list_1.event.add(Observer('delete', Logger.write_to_file))

linked_list_2.event.add(Observer('add', Logger.write_to_file))
linked_list_2.event.add(Observer('delete', Logger.write_to_file))

context = Context(1)

print('Info for linked_list_1: ')
linked_list_1 = create_first_strategy(linked_list_1)
context.change_strategy(2)
print('Info for linked_list_2: ')
linked_list_2 = create_second_strategy(linked_list_2)


def cycle_and_rotate(linked_list: LinkedList, k):
    linked_list.negative_k_cycle(k)
    linked_list.reverse_positive()


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
        context.change_strategy(1)
    elif option == 2:
        context.change_strategy(2)
    elif option == 3:
        if context.get_strategy() == 1:
            print('Info for first list: ')
            linked_list_1 = create_first_strategy(linked_list_1)
            print('Info for second list')
            linked_list_2 = create_first_strategy(linked_list_2)
        elif context.get_strategy() == 2:
            print('Info for first list: ')
            linked_list_1 = create_second_strategy(linked_list_1)
            print('Info for second list')
            linked_list_2 = create_second_strategy(linked_list_2)
    elif option == 4:
        pos1 = validate_input('position', linked_list_1.length(), 'delete')
        pos2 = validate_input('position', linked_list_2.length(), 'delete')
        create_thread([linked_list_1.pop_node, linked_list_2.pop_node], Object([pos1, pos2]))
    elif option == 5:
        pos1_1 = validate_input('start_pos', linked_list_1.length())
        pos2_1 = validate_input('end_pos', linked_list_1.length())

        pos1_2 = validate_input('start_pos', linked_list_2.length())
        pos2_2 = validate_input('end_pos', linked_list_2.length())

        create_thread([linked_list_1.pop_range_of_nodes, linked_list_2.pop_range_of_nodes], Object([pos1_1, pos2_1, pos1_2, pos2_2]))
    elif option == 6:
        k1 = validate_input('k')
        k2 = validate_input('k')

        create_thread([cycle_and_rotate, cycle_and_rotate], Object([linked_list_1, k1, linked_list_2, k2]))
    elif option == 7:
        print(linked_list_1.str_format())
        print(linked_list_2.str_format())
    elif option == 8:
        f = open('output1.txt', 'r+')
        f.truncate(0)
        break