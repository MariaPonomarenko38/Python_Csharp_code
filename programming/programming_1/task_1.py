import random


class Negative(Exception):
    pass


def gcd(num1, num2):
    if num1 < 0:
        num1 = -num1
    if num2 < 0:
        num2 = -num2
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def generate_sequence(a1, b1, n):
    if a1 > b1:
        a1, b1 = b1, a1
    s = [random.randint(a1, b1) for i in range(n)]
    return s


def finding_gcd_of_pairs(seq, n):
    result_arr = []
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if i != j:
                result_arr.append([seq[i], seq[j], gcd(seq[i], seq[j])])
    return result_arr


def print_pairs_and_gcd(seq):
    for element in seq:
        print("GCD of", element[0], "and", element[1], "is", element[2])


def validation_input(parametr):
    while True:
        try:
            param = int(input("Enter " + parametr + ": "))
            if parametr == "N":
                if param < 0:
                    raise Negative
        except ValueError:
            print("It's not a number")
        except Negative:
            print(parametr + " should be positive")
        else:
            return param


N = validation_input("N")
a = validation_input("a")
b = validation_input("b")
sequence = generate_sequence(a, b, N)
print("Sequence:", *sequence)
result = finding_gcd_of_pairs(sequence, N)
print_pairs_and_gcd(result)

