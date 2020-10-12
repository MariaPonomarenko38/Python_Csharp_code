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


def finding_gcd_of_pairs(seq, n):
    result_arr = []
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if i != j:
                result_arr.append([seq[i], seq[j], gcd(seq[i], seq[j])])
    return result_arr


def print_pairs_and_gcd(seq):
    if len(seq) == 0:
        print('There are no pairs')
    for element in seq:
        print("GCD of", element[0], "and", element[1], "is", element[2])