class Negative(Exception):
    pass


def making_matrix(n):
    arr = []
    for i in range(n):
        if i < n // 2 or (i == n // 2 and n % 2 != 0):
            arr1 = [0 if j < i or n - (j + 1) < i else 1 for j in range(n)]
        elif i == n // 2 and n % 2 == 0:
            arr1 = arr[i - 1]
        else:
            arr1 = arr[n - i - 1]
        arr.append(arr1)
    return arr


def print_matrix(n, arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()


def validation_input():
    while True:
        try:
            n = int(input('Input n: '))
            if n < 0:
                raise Negative
        except Negative:
            print("n should be positive")
        except ValueError:
            print("n should be number")
        else:
            return n


n = validation_input()
arr = making_matrix(n)
print_matrix(n, arr)