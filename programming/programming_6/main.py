from proga_3.meetings import Meetings
from proga_3.validation import validate_input, validate_file_input
from proga_3.memento import Creator, Caretaker


def copy_of_meetings(ls):
    ls1 = Meetings()
    for i in ls.meetings:
        ls1.add_to_list(i)
    return ls1


def memento(ls1: Meetings, originator: Creator, caretaker: Caretaker):
    originator.change(ls1)
    caretaker.filling_stack()
    ls = originator.get_condition_o()
    return ls


ls = Meetings()
file_name = validate_file_input()
ls.fill_list_from_file(file_name)
print(ls)
originator = Creator(ls)
caretaker = Caretaker(originator)
caretaker.filling_stack()
while True:
    number_op = input('''Input number of option:
    1. Search meetings with value
    2. Sort by parametr
    3. Delete meeting by ID
    4. Add meeting
    5. Edit meeting by ID
    6. See all meetings
    7. Undo
    8. Redo
    9. Exit''' + '\n')
    if number_op == '1':
        val = input('Input value for meeting: ')
        ls.search_in_list(val)
    elif number_op == '2':
        print('''Parametrs to sort: id, date, start_time, end_time, meeting_url, owner, participant''')
        param = input('Input parametr for sorting: ')
        if param in ['id', 'date', 'start_time', 'end_time', 'owner', 'meeting_url', 'participant']:
            ls1 = copy_of_meetings(ls)
            ls1.sort(param)
            ls = memento(ls1, originator, caretaker)
        else:
            print('Wrong parametr')
    elif number_op == '3':
        id = input('Input id: ')
        if id.isdigit() is True:
            ls1 = copy_of_meetings(ls)
            ls1.remove(file_name, id)
            ls = memento(ls1, originator, caretaker)
        else:
            print("Wrong id")
    elif number_op == '4':
        new_meeting = validate_input('add', False, None)
        if type(new_meeting) == str:
            ls1 = copy_of_meetings(ls)
            ls1.add(file_name, new_meeting)
            ls = memento(ls1, originator, caretaker)
    elif number_op == '5':
        id = input('Input id: ')
        new_meeting = validate_input('edit', False, None)
        if type(new_meeting) == str:
            ls1 = copy_of_meetings(ls)
            ls1.edit(file_name, id, new_meeting)
            ls = memento(ls1, originator, caretaker)
    elif number_op == '6':
        if type(ls) == 'NoneType':
            print('Your list_meetings is empty!')
        else:
            ls.print_list()
    elif number_op == '7':
        caretaker.undo_redo('undo')
        ls = originator.get_condition_o()
        ls.rewrite_file(file_name)
    elif number_op == '8':
        caretaker.undo_redo('redo')
        ls = originator.get_condition_o()
        ls.rewrite_file(file_name)
    elif number_op == '9':
        break
    else:
        print('Wrong number of choice')