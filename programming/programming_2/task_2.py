from random import randint


class Negative(Exception):
    pass


def negative_cycle(arr, k):
    for i in range(k):
        ind = [ind for ind, element in enumerate(arr) if element < 0]
        if len(ind) == 0:
            break
        tmp = arr[ind[len(ind) - 1]]
        for i in range(len(ind) - 1, -1, -1):
            arr[ind[i]] = arr[ind[i - 1]]
        arr[ind[0]] = tmp
    return arr


def rotate_positive_elements(arr):
    ind = [ind for ind, element in enumerate(arr) if element >= 0]
    ind1 = list(reversed(ind))
    arr1 = [x for x in arr]
    for i in range(len(ind)):
        arr[ind[i]] = arr1[ind1[i]]
    return arr


def validation_input(parametr):
    while True:
        try:
            if parametr == "array":
                param = [int(i) for i in input("Input array: ").split()]
                for i in param:
                    if str(abs(i)).isnumeric() is False:
                        raise ValueError
            else:
                param = int(input('Input ' + parametr + ': '))
                if param < 0:
                    raise Negative
        except Negative:
            print(parametr + " should be positive")
        except ValueError:
            print("You typed not a number")
        else:
            return param


while True:
    print('''Choose option: 
    1. Input array and k 
    2. Input n, k but array will be generated
    3. Exit''')
    choice = validation_input("choice")
    if choice == 1:
        ar = validation_input("array")
        k = validation_input("k")
    elif choice == 2:
        n = validation_input("n")
        print("You need to input a i b for range of elements: ")
        a = validation_input("a")
        b = validation_input("b")
        k = validation_input("k")
        ar = [randint(a, b) for i in range(n)]
        print("Array:", ar)
    else:
        break
    ar = negative_cycle(ar, k)
    ar = rotate_positive_elements(ar)
    print("Result:", ar, end='\n\n')


# -2 5 6 -3 -4 3 -1
# -4 3 6 -1 -2 5 -3

# -1 -3 -6 2 -7 -5
