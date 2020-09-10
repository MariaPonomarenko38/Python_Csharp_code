import random


def gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


N = int(input("Enter N:"))
a = int(input("Enter a:"))
b = int(input("Enter b:"))
sequence = [random.randint(a, b) for i in range(N)]
print("Sequence:", *sequence)
for i in range(0, N):
    for j in range(i + 1, N):
        if i != j:
            print("GCD of", sequence[i], "and", sequence[j], "is", gcd(sequence[i], sequence[j]))
