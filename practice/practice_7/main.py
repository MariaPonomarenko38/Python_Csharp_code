from Ponomarenko_pmi25.practice.practice_7.linked_list import LinkedList
from Ponomarenko_pmi25.practice.practice_7.validation import *
from Ponomarenko_pmi25.practice.practice_7.observer import *
from Ponomarenko_pmi25.practice.practice_7.context import Context
from threading import Thread


def write_to_file(*args):
    f = open('output1.txt', 'a')
    for i in args:
        f.write(str(i) + ' ')
    f.write('\n')


def create_thread(func1, func2, args1, args2):
    thread1 = Thread(target=func1, args=(*args1,))
    thread2 = Thread(target=func2, args=(*args2,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

def create_first_list():
    print('Info for first list')
    linked_list_1 = LinkedList()
    context = Context(1)
    n = validate_input('quantity of elements')
    a = validate_input('left_border', linked_list_1.length())
    b = validate_input('right_border', linked_list_1.length())
    pos = validate_input('position', linked_list_1.length())
    linked_list_1 = context.do(linked_list_1, n, a, b, pos)
    return linked_list_1


def create_second_list():
    print('Info for second list:')
    linked_list_2 = LinkedList()
    context = Context(2)
    pos = validate_input('position', linked_list_2.length())
    file_name = validate_file_input()
    linked_list_2 = context.do(linked_list_2, pos, file_name)
    return linked_list_2

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

linked_list_1.event.add(Observer('add', Logger.write_to_file))
linked_list_1.event.add(Observer('delete', Logger.write_to_file))

linked_list_2.event.add(Observer('add', Logger.write_to_file))
linked_list_2.event.add(Observer('delete', Logger.write_to_file))

linked_list_1 = create_first_list()
linked_list_2 = create_second_list()

def convert_to_list(*args):
    l = []
    for i in args:
        l.append(i)
    return l


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
    if option == 4:
        pos1 = validate_input('position', linked_list_1.length(), 'delete')
        pos2 = validate_input('position', linked_list_2.length(), 'delete')
        create_thread(linked_list_1.pop_node, linked_list_2.pop_node, convert_to_list(pos1), convert_to_list(pos2))

    elif option == 5:
        pos1_1 = validate_input('start_pos', linked_list_1.length())
        pos2_1 = validate_input('end_pos', linked_list_1.length())

        pos1_2 = validate_input('start_pos', linked_list_2.length())
        pos2_2 = validate_input('end_pos', linked_list_2.length())

        create_thread(linked_list_1.pop_range_of_nodes, linked_list_2.pop_range_of_nodes, convert_to_list(pos1_1, pos2_1), convert_to_list(pos1_2, pos2_2))
    elif option == 6:
        k1 = validate_input('k')
        k2 = validate_input('k')

        create_thread(cycle_and_rotate, cycle_and_rotate, convert_to_list(linked_list_1, k1), convert_to_list(linked_list_2, k2))
    elif option == 7:
        create_thread(write_to_file, write_to_file, convert_to_list('first list:', linked_list_1.print_list()),  convert_to_list('second list:', linked_list_2.print_list()))
    elif option == 8:
        f = open('output1.txt', 'r+')
        f.truncate(0)
        break