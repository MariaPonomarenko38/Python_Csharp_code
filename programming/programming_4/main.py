from Ponomarenko_pmi25.programming.programming_4.meetings import Meetings, fill_list_from_file
from Ponomarenko_pmi25.programming.programming_4.validation import validate_input


def edit_file(file, id, val):
    arg = val.split()
    arg[0] = int(arg[0])
    f = open(file, "r+")
    input_lines = f.readlines()
    f.truncate(0)
    f.close()
    count = 0
    with open(file, 'w', encoding='utf-8') as f:
        for line in input_lines:
            if line.split()[0] != id:
                f.write(line)
            else:
                f.write(val + "\n")
    f.close()


ls = Meetings()
while True:
    number_op = input('''Input number of option:
    0. Fill list from file
    1. Search meetings with value
    2. Sort by parametr
    3. Delete meeting by ID
    4. Add meeting
    5. Edit meeting by ID (don't change ID!)
    6. See all meetings
    7. Edit file (in all cases except two same ID)  
    8. Exit''' + '\n')
    if number_op == '0':
        ls = fill_list_from_file('input.txt', 'add')
    elif number_op == '1':
        val = input('Input value for meeting: ')
        if val.isdigit():
            val = int(val)
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
            ls.remove('input.txt', id)
        else:
            print("Wrong id")
    elif number_op == '4':
        new_meeting = validate_input()
        ls.add('input.txt', new_meeting)
    elif number_op == '5':
        id = input('Input id: ')
        new_meeting = validate_input()
        ls.edit('input.txt', id, new_meeting)
    elif number_op == '6':
        if type(ls) == 'NoneType':
            print('Your list_meetings is empty!')
        else:
            ls.print_list()
    elif number_op == '7':
        id = input('Input id: ')
        new_meeting = validate_input()
        edit_file('input.txt', id, new_meeting)
    elif number_op == '8':
        break
    else:
        print('Wrong number of choice')

#4 09.10.2020 17:20 18:38 http://zoom/49irt39483 RRRRRRR Marco Vladimir Melnik
