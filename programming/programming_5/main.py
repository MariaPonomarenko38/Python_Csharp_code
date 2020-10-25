from Ponomarenko_pmi25.programming.programming_5.meetings import Meetings
from Ponomarenko_pmi25.programming.programming_5.validation1 import validate_file_input


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
        print('''Parametrs to sort: id, date, start_time, end_time, meeting_url, owner, participant''')
        param = input('Input parametr for sorting: ')
        if param in ['id', 'date', 'start_time', 'end_time', 'meeting_url', 'owner', 'participant']:
            ls.sort(param)
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
        ls.add(new_meeting, file_name)
    elif number_op == '5':
        id = input('Input id: ')
        new_meeting = input('Input info for new meeting: ')
        ls.edit(new_meeting, file_name, id)
    elif number_op == '6':
        if type(ls) == 'NoneType':
            print('Your list_meetings is empty!')
        else:
            ls.print_list()
    elif number_op == '7':
        break
    else:
        print('Wrong number of choice')



