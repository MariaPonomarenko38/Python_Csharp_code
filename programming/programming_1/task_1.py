import random


class LessThanA(Exception):
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
    s = [random.randint(a1, b1) for i in range(n)]
    return s


while True:
    try:
        N = int(input("Enter N: "))
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        if b < a:
            raise LessThanA
    except ValueError:
        print("It's not a number")
    except LessThanA:
        print("b should be bigger than a")
    else:
        break
sequence = generate_sequence(a, b, N)
print("Sequence:", *sequence)
for i in range(0, N - 1):
    for j in range(i + 1, N):
        if i != j:
            print("GCD of", sequence[i], "and", sequence[j], "is", gcd(sequence[i], sequence[j]))
