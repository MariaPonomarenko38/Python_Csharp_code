from Ponomarenko_pmi25.programming.programming_5.meetings import Meetings
from Ponomarenko_pmi25.programming.programming_5.validation1 import validate_file_input, Validate


ls = Meetings()
file_name = validate_file_input()
ls.fill_list_from_file(file_name)
while True:
    number_op = input('''Input number of option:
    1. Search meetings with value
    2. Sort by parametr
    3. Delete meeting by ID
    4. Add meeting
    5. Edit meeting by ID
    6. See all meetings
    7. Exit''' + '\n')
    if number_op == '1':
        val = input('Input value for meeting: ')
        ls.search_in_list(val)
    elif number_op == '2':
        print('''Parametrs to sort: id, date, start_time, end_time, owner, participant''')
        param = input('Input parametr for sorting: ')
        if param in ['id', 'date', 'start_time', 'end_time', 'owner', 'participant']:
            ls.sort(param)
            ls.print_list()
        else:
            print('Wrong parametr')
    elif number_op == '3':
        id = input('Input id: ')
        if id.isdigit() is True:
            ls.remove(file_name, id)
        else:
            print("Wrong id")
    elif number_op == '4':
        new_meeting = input('Input info for new meeting: ')
        v = Validate(new_meeting.split(), 'add')
        if v() is not None:
            ls.add(file_name, new_meeting)
    elif number_op == '5':
        id = input('Input id: ')
        new_meeting = input('Input info for new meeting: ')
        v = Validate(new_meeting.split(), 'edit')
        if v() is not None:
            ls.edit(file_name, id, new_meeting)
    elif number_op == '6':
        if type(ls) == 'NoneType':
            print('Your list_meetings is empty!')
        else:
            ls.print_list()
    elif number_op == '7':
        break
    else:
        print('Wrong number of choice')



