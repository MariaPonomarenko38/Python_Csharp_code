from math import sqrt


class Negative(Exception):
    pass


# розкладає число на множники, повертає словник: ключом є множник, значенням - скільки разів на множник ділилось число
def factorization(n1):
    dict1 = {}
    used = {}
    for i in range(2, int(sqrt(n1)) + 1):
        while n1 % i == 0:
            if used.get(i, False) is True:
                dict1[i] += 1
            else:
                dict1[i] = 1
                used[i] = True
            n1 //= i
    if n1 != 1:
        dict1[n1] = 1
    if len(dict1) == 0:
        dict1[1] = 1
    return dict1


while True:
    try:
        a = int(input("Enter a: "))
        if a < 0:
            raise Negative
    except ValueError:
        print("It's not a number")
    except Negative:
        print("a must be positive")
    else:
        break
d = factorization(a)
max_degree = max(d.values())
product = 1
for i in d.keys():
    product *= i  # знаходимо добуток множників (без степенів)
if max_degree <= product:  # якщо макс.степінь серед усіх множників <= за добуток то добуток і є відповіддю
    print(product)  # наприклад, 12 = 2^2 * 3, 2 <= (2 * 3), отже 6^6 % 12 = 0, або (2^6 * 3^6) % 12 = 0
else:
    n = product
    was_found = False
    while was_found is False:
        n += product  # додаємо до шуканого числа добуток (бо тоді він буде мати ті самі множники що й А)
        d1 = factorization(n)
        if len(d) <= len(d1):
            was_found = True
            for i in d.keys():
                # наприклад: а = 2^18 * 3, підходить n = 12: 2^24 * 3^12, тобто 2: 24 > 18, a 3: 12 > 1
                # якщо це не виконується - робимо break
                if d1[i] * n < d[i]:
                    was_found = False
                    break
    print(n)

