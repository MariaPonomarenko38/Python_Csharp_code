import os


class StrategyError(Exception):
    pass


class OptionError(Exception):
    pass


class PositionError(Exception):
    pass


class PositionError1(Exception):
    pass


class QuantityError(Exception):
    pass


class WrongDataFile(Exception):
    pass


class WrongK(Exception):
    pass


def validate_file_input():
    while True:
        file = input('Input name of your file: ')
        try:
            if not os.path.isfile(file):
                raise FileExistsError
            else:
                f = open(file, 'r')
                ls = [i for i in ''.join(f.readlines()).split()]
                f.close()
                for i in ls:
                    if i.isalpha() is True:
                        raise WrongDataFile
        except FileExistsError:
            print('File not exists, try again')
        except WrongDataFile:
            print('Some elements are not numbers in file')
            return
        else:
            return file


def validate_input(param, val=None, action=None):
    while True:
        try:
            n = int(input('Input ' + param + ': '))
            if param == 'strategy':
                if n not in [1, 2]:
                    raise StrategyError
            elif param == 'option':
                if n <= 0 or n >= 9:
                    raise OptionError
            elif param == 'position to insert' or param == 'start_pos' or param == 'end_pos':
                if n <= 0:
                    raise PositionError
                elif n > val + 1 and action is None:
                    raise PositionError1
                elif n > val and action == 'delete':
                    raise PositionError1
            elif param == 'quantity of elements':
                if n <= 0:
                    raise QuantityError
            elif param == 'k':
                if n < 1:
                    raise WrongK
        except ValueError:
            print(param, 'should be a number')
        except StrategyError:
            print('Strategy can be equal 1 or 2')
        except OptionError:
            print('Option can be from 1 to 8')
        except PositionError:
            print('Position must be >= 1')
        except PositionError1:
            print('List has only', str(val), 'elements')
        except QuantityError:
            print('Quantity must be ')
        except WrongK:
            print('k should be >= 1')
        else:
            return n