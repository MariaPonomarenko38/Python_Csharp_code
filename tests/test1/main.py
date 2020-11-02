from Ponomarenko_pmi25.tests.test1.classes import *


ls = Collection()
ls.fill_list_from_file('data.txt')
while True:
    print('''
    1. Add taxi
    2. Top N range of time
    3. Top N type taxis
    4. Print taxis
    ''')
    option = input()
    if option == '1':
        s = input('Input new taxi info: ')
        ls.add_to_list(s)
    elif option == '2':
        n = int(input('Type N: '))
        ls.max_time(n)
    elif option == '3':
        n = int(input('Type N: '))
        ls.top_taxi(n, 'output.txt')
    elif option == '4':
        ls.print1()
    else:
        break