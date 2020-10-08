from Ponomarenko_pmi25.practice.practice_4.gcd_functions import print_pairs_and_gcd, finding_gcd_of_pairs
from Ponomarenko_pmi25.practice.practice_4.gen_and_iter import generator_random_number, RandomNumber


class Negative(Exception):
    pass


class WrongOption(Exception):
    pass


def creating_sequence(a1, b1, n, param):
    if a1 > b1:
        a1, b1 = b1, a1
    s = []
    if param == 1:
        f = RandomNumber(n, a1, b1)
        for i in range(n):
            s.append(next(f))
    elif param == 2:
        gen_iter = generator_random_number(n, a1, b1)
        for i in range(n):
            s.append(next(gen_iter))
    return s


def validation_input(parametr):
    while True:
        try:
            param = int(input("Enter " + parametr + ": "))
            if parametr in ['N', 'Option']:
                if param < 0:
                    raise Negative
            if parametr == 'Option':
                if param not in [1, 2]:
                    raise WrongOption
        except ValueError:
            print("It's not a number")
        except Negative:
            print(parametr + " should be positive")
        except WrongOption:
            print("We don't have such option")
        else:
            return param


while True:
    print('\n' + '''Choose option:
    1. Generate sequence with iterator
    2. Generate sequence with generator
    3. Exit''' + '\n')
    option = validation_input('option')
    if option == 3:
        break
    N = validation_input("N")
    a = validation_input("a")
    b = validation_input("b")
    sequence = creating_sequence(a, b, N, option)
    print("Sequence:", *sequence)
    result = finding_gcd_of_pairs(sequence, N)
    print_pairs_and_gcd(result)
