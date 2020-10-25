from Ponomarenko_pmi25.practice.practice_6.linked_list import LinkedList
from Ponomarenko_pmi25.practice.practice_6.validation import *
from Ponomarenko_pmi25.practice.practice_6.observer_classes import *
from Ponomarenko_pmi25.practice.practice_6.iterator import *
from Ponomarenko_pmi25.practice.practice_6.context import Context

linked_list = LinkedList()
list_of_info = Observer('logs.txt')
list_of_all_actions = ['Choose strategy1', 'Choose strategy2', 'Insert data',
                       'Delete element by position', 'Delete range of elements',
                       'Negative cycle and reversing positive elements', 'Print list']
event = Event(list_of_all_actions, list_of_info)
event.add()

dict_of_all_actions = {i + 1: list_of_all_actions[i] for i in range(len(list_of_all_actions))}

context = Context(1)
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
            n = validate_input('quantity of elements')
            a = validate_input('left_border', linked_list.length())
            b = validate_input('right_border', linked_list.length())
            pos = validate_input('position to insert', linked_list.length())
            linked_list = context.do(linked_list, n, a, b, pos)
        elif context.get_strategy() == 2:
            pos = validate_input('position to insert', linked_list.length())
            file_name = validate_file_input()
            linked_list = context.do(linked_list, pos, file_name)
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
    if option <= 7:
        event.notify(dict_of_all_actions[option])
    elif option == 8:
        break