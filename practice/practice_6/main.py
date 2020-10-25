from Ponomarenko_pmi25.practice.practice_6.linked_list import LinkedList
from Ponomarenko_pmi25.practice.practice_6.validation import *
from Ponomarenko_pmi25.practice.practice_6.observer_classes import *
from Ponomarenko_pmi25.practice.practice_6.iterator import *

linked_list = LinkedList()
list_of_info = Observer('logs.txt')
list_of_all_actions = ['Inserting data from file', 'Inserting generating data', 'Delete element by position',
                       'Delete range of elements', 'Negative cycle and reversing positive elements', 'Print list']
event = Event(list_of_all_actions, list_of_info)
event.add()

dict_of_all_actions = {i + 1: list_of_all_actions[i] for i in range(len(list_of_all_actions))}

while True:
    print('''Choose option:
    1. Inserting data from file
    2. Inserting generating data
    3. Delete element by position
    4. Delete range of elements
    5. Negative cycle and reversing positive elements
    6. Print list
    7. Exit
    ''')
    option = validate_input('option')
    if option == 1:
        pos = validate_input('position to insert', linked_list.length())
        file_name = validate_file_input()
        f = open(file_name, 'r')
        ls = [int(i) for i in ''.join(f.readlines()).split()]
        linked_list.insert_list(pos, ls)
    elif option == 2:
        n = validate_input('quantity of elements')
        a = validate_input('left_border', linked_list.length())
        b = validate_input('right_border', linked_list.length())
        pos = validate_input('position to insert', linked_list.length())
        ls = creating_sequence(a, b, n)
        linked_list.insert_list(pos, ls)
    elif option == 3:
        pos = validate_input('position to insert', linked_list.length(), 'delete')
        linked_list.pop_node(pos)
    elif option == 4:
        pos1 = validate_input('start_pos', linked_list.length())
        pos2 = validate_input('end_pos', linked_list.length())
        linked_list.pop_range_of_nodes(pos1, pos2)
    elif option == 5:
        k = validate_input('k')
        linked_list.negative_k_cycle(k)
        linked_list.reverse_positive()
    elif option == 6:
        print(linked_list)
    if option <= 6:
        event.notify(dict_of_all_actions[option])
    else:
        break