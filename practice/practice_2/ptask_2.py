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


def calculating_operations(k, array_element, middle, sign, border, if_number, num_of_operations):
    print('Comprasion of element and arr[m]: {0} {1} {2}'.format(k, sign, array_element))
    if if_number == 3:
        print("Index with element K was found! Making a list with all indexes of element K:")
    else:
        print('New value for {0} border: {1} = {2}'.format(border, border[0:1], middle))
    return num_of_operations


#-1 0 6 -4 -2 6 -3 -10
def binary_search(arr, elem):
    arr = [(x, ind) for ind, x in enumerate(arr)]
    arr = sorted(arr)
    print(arr)
    l = 0
    r = len(arr) - 1
    res = []
    count = 0
    while r - l > 1:
        m = (l + r) // 2
        if elem > arr[m][0]:
            count += calculating_operations(elem, arr[m][0], m, '>', 'left', 1, 5)
            l = m
        elif elem < arr[m][0]:
            count += calculating_operations(elem, arr[m][0], m, '<', 'right', 2, 6)
            r = m
        else:
            count1 = 0
            count += calculating_operations(elem, arr[m][0], m, '=', 'equal', 3, 4)
            while True:
                if arr[m][0] != elem or m == len(arr):
                    break
                res.append(arr[m][1])
                m += 1
                count1 += 3
            print("Quantity of operations for binary search:", count + 3)
            print("Quantity of operations for finding all indexes of element K and forming result array:", count1 + 2)
            return res
        if r - l <= 1:
            print("Quantity of operations for binary search:", count + 4)
            print("Element K wasn't found!")
            res.append("Empty!")
            return res


def validation_input(parametr):
    while True:
        try:
            if parametr == "array":
                param = [int(i) for i in input("Input array: ").split()]
                for i in param:
                    if str(abs(i)).isnumeric() is False:
                        raise ValueError
            elif parametr == "a" or parametr == "b" or parametr == "K":
                param = int(input('Input ' + parametr + ': '))
                if str(abs(param)).isnumeric() is False:
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
        if a > b:
            a, b = b, a
        ar = [randint(a, b) for i in range(n)]
        print("Array:", ar)
    else:
        break
    ar = negative_cycle(ar, k)
    ar = rotate_positive_elements(ar)
    print("Result:", ar, end='\n\n')
    element = validation_input("K")
    all_indexes = binary_search(ar, element)
    print("All positions of K in array: ", *all_indexes, end='\n\n')


# -2 5 6 -3 -4 3 -1
# -4 3 6 -1 -2 5 -3

#-5 2 3 -5 -2 -6 -6 -8
#-6 3 2 -8 -5 -5 -2 -6
