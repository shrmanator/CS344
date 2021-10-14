# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:

import random
import string
from a1_include import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------


def min_max(arr: StaticArray) -> tuple:
    """
    Returns a Python tuple with two values:
    minimum and maximum values in the input array.
    """
    # This block assigns the smallest value in arr to the_curr_smallest_value:
    the_curr_smallest_value = arr[0]
    for i in range(arr.size()):
        if arr[i] and arr[i] < the_curr_smallest_value:
            the_curr_smallest_value = arr[i]

    # This block assigns the largest value in arr to the_curr_largest_value:
    the_curr_largest_value = arr[0]
    for j in range(arr.size()):
        if arr[j] and arr[j] > the_curr_largest_value:
            the_curr_largest_value = arr[j]

    # Then we return both variables as a tuple:
    return the_curr_smallest_value, the_curr_largest_value


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Returns a new StaticArray object with the content from *arr*, modified as follows:

     1)If the number in *arr* is divisible by 3,
       corresponding element in the new SA should be a string ‘fizz’.

     2)If the number in *arr* is divisible by 5,
       corresponding element in the new SA should be a string ‘buzz’.

     3)If the number in *arr* is both a multiple of 3 and a multiple of 5,
       corresponding element in the new SA should be a string ‘fizzbuzz’.

     4)In all other cases, the element in the returned SA should have the same value as *arr*.

     Preconditions: *arr* contains only integers.
                    size(arr) > 0.
    """
    # First, let' put the values of arr into a new SA:
    sa = StaticArray(arr.size())
    for i in range(sa.size()):
        sa.set(i, arr[i])

    # Now, let's change the values of arr according to the docstring:
    for j in range(sa.size()):
        if arr[j] % 3 == 0 and arr[j] % 5 == 0:
            sa.set(j, 'fizzbuzz')
        elif arr[j] % 3 == 0:
            sa.set(j, 'fizz')
        elif arr[j] % 5 == 0:
            sa.set(j, 'buzz')

    return sa


# ------------------- PROBLEM 3 - REVERSE -----------------------------------


def reverse(arr: StaticArray) -> None:
    """
    Reverses *arr* elements IN PLACE.
    Note: Reversal must be done ‘in place’, meaning the original input array will be modified.

    Precondition:
        size(arr) > 0
    """
    # Copy *arr*:
    arr_copy = StaticArray(arr.size())
    for i in range(arr.size()):
        arr_copy.set(i, arr[i])

    # And now we'll just insert the values from the last index of arr_copy until the first:
    j = 0
    for k in range(arr_copy.size(), 0, -1):
        arr[j] = arr_copy[k - 1]
        j = j + 1


# ------------------- PROBLEM 4 - ROTATE ------------------------------------


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Return a new StaticArray where all elements are from the original array,
     but their position has shifted right or left steps number of times.
      If steps is a positive integer, elements should be rotated right. If its negative, rotation is to the left.

    Preconditions:
     Input array will have at least one element.
    """
    n = arr.size()
    new_arr = copy_sa(arr)
    if steps > 0:
        # right
        for i in range(n):
            new_arr[i] = arr[((i - steps) % n + n) % n]
    elif steps < 0:
        # left
        for i in range(n):
            new_arr[((i + steps) % n + n) % n] = arr[i]
    return new_arr


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

# COMPLETE
def sa_range(start: int, end: int) -> StaticArray:
    """
    Returns a StaticArray that contains consecutive values that
     begin at start and ends at end (inclusive).
    """
    # Deal with annoying corner cases:
    if (start == 0 and end == 0) or start == end:
        sa = StaticArray(1)
        sa.set(0, start)
        return sa

    # rest of code follows:
    j = 0
    if start < end:
        arr = StaticArray((end - start) + 1)
        for i in range(start, end + 1):
            arr.set(j, i)
            j += 1
    else:
        size = abs(abs(start)-abs(end))+1
        arr = StaticArray(size)
        for i in range(start, end -1, -1):
            arr.set(j, i)
            j += 1

    return arr

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------


def is_sorted(arr: StaticArray) -> int:
    """
    Returns an integer that describes whether the array is sorted.
     Method should return 1 if the array is sorted in strictly ascending order.
      It should return 2 if the list is sorted in strictly descending order.
       Otherwise the method should return 0.
        Arrays consisting of a single element are considered sorted in strictly ascending order.
    """
    match_counter = 0
    is_equal = 0

    # loop checks whether arr is ascending or descending:
    for i in range(arr.size() - 1):
        if arr[i] < arr[i + 1]:
            match_counter += 1
        elif arr[i] > arr[i + 1]:
            match_counter -= 1

    if (match_counter + is_equal) + 1 == arr.size():
        return 1
    elif (match_counter - is_equal) - 1 == -arr.size():
        return 2
    return 0


# ------------------- PROBLEM 7 - SA_SORT -----------------------------------

# COMPLETE
def sa_sort(arr: StaticArray) -> None:
    """
    Receives a StaticArray and sorts its content in non-descending order (smallest to largest).

    Precondition:
        The original array should be sorted.
    """
    for i in range(arr.size() - 1):
        min_index = i
        for j in range(i + 1, arr.size()):
            if arr.get(j) < arr.get(min_index):
                min_index = j
        temp = arr.get(i)
        arr.set(i, arr.get(min_index))
        arr.set(min_index, temp)


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Returns a new StaticArray with all duplicate values removed.

    ex. [2, 2, 1] -> [1]
    """
    count = 0
    temp_arr = copy_sa(arr)
    size = temp_arr.size()
    i = 0
    while i < size:
        variable = temp_arr.get(i)
        count += 1
        j = i + 1

        while j < size:
            temp_variable = temp_arr.get(j)
            if temp_variable == variable:
                k = j + 1

                while k < size:
                    temp_arr.set(k - 1, temp_arr.get(k))
                    k = k + 1
                size -= 1
                j -= 1
            j = j + 1

        i = i + 1

    new_array = StaticArray(count)

    for i in range(0, count):
        new_array.set(i, temp_arr.get(i))

    return new_array


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    Returns a new StaticArray with the same content sorted in non-ascending order (largest to smallest).
    """
    # Follows count sort algorithm:
    temp_arr = copy_sa(arr)
    min = 0
    max = 0
    for i in range(temp_arr.size()):
        value = temp_arr.get(i)
        if not min:
            min = max = value
        else:
            if value < min:
                min = value
            if value > max:
                max = value

    counts = StaticArray(max - min + 1)
    for i in range(max - min + 1):
        counts.set(i, 0)

    for i in range(temp_arr.size()):
        value = temp_arr.get(i)
        counts[value - min] += 1

    index = 0
    for i in range(counts.size()):
        count = counts[i]
        for j in range(count):
            temp_arr.set(index, min + i)
            index += 1

    reverse(temp_arr)  # a bit hacky here, but it works
    return temp_arr


# ------------------- PROBLEM 10 - SA_INTERSECTION --------------------------


def sa_intersection(arr1: StaticArray, arr2: StaticArray, arr3: StaticArray) -> StaticArray:
    """
    Returns a new StaticArray only with the elements that appear in *arr1*, *arr2*, *arr3*.

    Precondition:
     Values stored in the input arrays are all of the same type
    """
    temp = StaticArray(arr1.size())
    k = 0 # this keeps track of temp's current index throughout this program:

    # these keep track of the indices of all 3 input arrays.
    i1 = 0
    i2 = 0
    i3 = 0

    while i1 < arr1.size() and i2 < arr2.size() and i3 < arr3.size():
        # there are the values @ each array's corresponding index:
        v1 = arr1.get(i1)
        v2 = arr2.get(i2)
        v3 = arr3.get(i3)

        # this is the main logic:
        if v1 == v2 == v3:
            temp.set(k, v1)
            k += 1
            i1 += 1
            i2 += 1
            i3 += 1
        elif v1 < v2 or v1 < v3:
            i1 += 1
        elif v2 < v3 or v2 < v1:
            i2 += 1
        else:
            i3 += 1

    # Let's determine size of output array *final*:
    count = 0
    for i in range(temp.size()):
        if temp.get(i) is None:
            break
        count += 1

    if count == 0:
        # empty array case:
        return StaticArray(1)
    else:
        final = StaticArray(count)
        for i in range(count):
            final.set(i, temp.get(i))

    return final

# ------------------- PROBLEM 11 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    returns a new StaticArray with squares of the values from the original array,
     sorted in non-descending (smallest to largest) order.

    Precondition: Input StaticArray must be sorted.
    """
    new_arr = StaticArray(arr.size())

    # this was an annoying one:

    m = 0  # index where the sign of the element changes

    if arr[0] < arr[arr.size() - 1]:  # ascending order array
        while m < arr.size() and arr[m] < 0:  # increase m till the element became positive
            m += 1
    else:  # descending order array
        while m < arr.size() and arr[m] > 0:  # increase m till the element became negative
            m += 1

    n = m - 1

    for i in range(new_arr.size()):
        if m < arr.size() and n >= 0:
            # check which of the element at index m or n is smaller when squared
            if arr[m] ** 2 > arr[n] ** 2:  # if element at index n is smaller
                new_arr[i] = arr[n] ** 2  # push the square of that element to the output array
                n -= 1  # decrement n since we used the element at index n
            else:  # if element at index m is smaller
                new_arr[i] = arr[m] ** 2  # push the square of that element to the output array
                m += 1  # increment m since we used the element at index m
        elif n >= 0:  # here n is within the bounds while m is not within the bounds
            new_arr[i] = arr[n] ** 2
            n -= 1
        else:
            new_arr[i] = arr[m] ** 2
            m += 1

    return new_arr


# ------------------- PROBLEM 12 - ADD_NUMBERS ------------------------------
def add_numbers(arr1: StaticArray, arr2: StaticArray) -> StaticArray:
    """
    returns a new StaticArray representing a sum of those two numbers. Original arrays should not be modified.

    Preconditions:
        *arr1*, *arr2* are non-negative numbers.
    """
    bigger_array = arr1.size() + 1 if arr1.size() > arr2.size() else arr2.size() + 1
    new_arr = StaticArray(bigger_array)

    carry = 0

    n_arr1, n_arr2 = arr1.size() - 1, arr2.size() - 1
    n_new_arr = new_arr.size() - 1  # variable pointing to the last index of new_arr

    while n_arr1 >= 0 and n_arr2 >= 0:
        # add elements
        temp = arr1[n_arr1] + arr2[n_arr2] + carry  # variable storing the sum of digits and carry
        new_arr.set(n_new_arr, temp % 10)  # adding the ones place digit of temp to the result
        carry = int(temp / 10)  # changing the carry to the tens place digit of temp
        # decrementing the indexes
        n_arr1 -= 1
        n_arr2 -= 1
        n_new_arr -= 1
        print(temp, "<-- temp")

    while n_arr1 >= 0:
        temp = arr1[n_arr1] + carry  # variable storing the sum of digits and carry
        new_arr.set(n_new_arr, temp % 10)  # adding the ones place digit of temp to the result
        carry = int(temp / 10)  # changing the carry to the tens place digit of temp
        # decrementing the indexes
        n_arr1 -= 1
        n_new_arr -= 1
    while n_arr2 >= 0:
        temp = arr2[n_arr2] + carry  # variable storing the sum of digits and carry
        new_arr.set(n_new_arr, temp % 10)  # adding the ones place digit of temp to the result
        carry = int(temp / 10)  # changing the carry to the tens place digit of temp
        # decrementing the indexes
        n_arr2 -= 1
        n_new_arr -= 1

    if carry == 1:
        new_arr.set(n_new_arr, carry)
        n_new_arr -= 1

    n_new_arr += 1
    final_length = new_arr.size() - n_new_arr
    ans = StaticArray(final_length)
    for i in range(ans.size()):
        ans[i] = new_arr[n_new_arr]
        n_new_arr += 1

    return ans


# ------------------- PROBLEM 13 - BALANCED_STRINGS -------------------------


def balanced_strings(s: str) -> StaticArray:
    """
    receives a balanced string and splits it into the maximum possible number of balanced strings.
    """
    new_arr = StaticArray(len(s))
    a = 0
    b = 0
    c = 0
    start = 0  # index of new_arr
    temp = ''
    for i in range(len(s)):
        temp += s[i]
        if s[i] == 'a' or s[i] == 'A':
            a += 1
        elif s[i] == 'b' or s[i] == 'B':
            b += 1
        elif s[i] == 'c' or s[i] == 'C':
            c += 1

        if a == b and b == c:
            new_arr.set(start, temp)
            temp = ''
            start += 1
            a = b = c = 0

    ans = StaticArray(start)
    for i in range(start):
        ans[i] = new_arr[i]

    return ans


# ------------------- PROBLEM 14 - TRANSFORM_STRING -------------------------
def transform_string(source: str, s1: str, s2: str) -> str:
    """
    Returns a modified string of the same length as the source.

    Source string should be processed one character at the time
     and output string should be constructed according to the following rules:
     1) If the character from the source string is present in s1 it should be replaced by the character at the same index in s2
     2)Otherwise, if the character is:
        a)Uppercase letter -> replace by ' '
        b)Lowercase letter -> replace by ' # '
        c)Digit -> replace by ' ! '
        d)Anything else -> replace by ' = ' You may assume that strings s1 and s2 have the same length .
    """
    modified_str = ""

    # now we build the string using some python builtins:

    for i in range(len(source)):
        index = s1.find(source[i])

        if index != -1:
            modified_str += s2[index]

        elif source[i].isupper():
            modified_str += ' '

        elif source[i].islower():
            modified_str += '#'

        elif source[i].isdigit():
            modified_str += '!'

        else:
            modified_str += '='

    return modified_str


# HELPER FUNCTIONS
def copy_sa(arr: StaticArray) -> StaticArray:
    """
    Returns a copy of *arr*.
    Note: u must import doctest.testmod to use

    >>> sa = StaticArray(3)
    >>> sa[0] = 1
    >>> sa[1] = 6
    >>> sa[2] = 2
    >>> new_sa = copy_sa(sa)
    >>> new_sa[0]
    1
    >>> new_sa[1]
    6
    >>> new_sa[2]
    2
    """
    arr_copy = StaticArray(arr.size())
    for i in range(arr.size()):
        arr_copy.set(i, arr[i])
    return arr_copy


# BASIC TESTING
if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # arr = StaticArray(5)
    # for i, value in enumerate([7, 8, 6, -5, 4]):
    #     arr[i] = value
    # print(min_max(arr) == (-5, 8))
    #
    # print('\n# min_max example 2')
    # arr = StaticArray(1)
    # arr[0] = 100
    # print(min_max(arr) == (100, 100))
    #
    # print('\n# min_max example 3')
    # arr = StaticArray(3)
    # for i, value in enumerate([3, 3, 3]):
    #     arr[i] = value
    # print(min_max(arr) == (3, 3))
    #
    # print('\n# min_max example 4 (Dov custom)')
    # print('Works on increasing sorted SA of ints')
    # arr = StaticArray(5)
    # arr.set(0, 1)
    # arr.set(1, 2)
    # arr.set(2, 3)
    # arr.set(3, 4)
    # arr.set(4, 5)
    # print(min_max(arr) == (1, 5))
    #
    # print('\n# min_max example 6 (Dov custom)')
    # print('Works on emtpy SA of size 5 (ie., returns None)')
    # arr = StaticArray(5)
    # print(min_max(arr) == (None, None))
    #
    #
    # print('\n# min_max example 4 (Dov custom)')
    # print('Works on  non-sorted SA')
    # arr = StaticArray(5)
    # arr.set(0, 100)
    # arr.set(1, -12343)
    # arr.set(2, 34802394)
    # arr.set(3, 2)
    # arr.set(4, -12343)
    # print(min_max(arr) == (-12343, 34802394))
    #

    # # TODO: more tests!
    # print('\n# fizz_buzz example 1')
    # source = [_ for _ in range(-5, 20, 4)]
    # arr = StaticArray(len(source))
    # for i, value in enumerate(source):
    #     arr[i] = value
    # print(fizz_buzz(arr))
    # print(arr)

    # # TODO: more tests!
    # print('\n# reverse example 1')
    # source = [_ for _ in range(-20, 20, 7)]
    # arr = StaticArray(len(source))
    # for i, value in enumerate(source):
    #     arr.set(i, value)
    # print(arr)
    # reverse(arr)
    # print(arr)
    # reverse(arr)
    # print(arr)
    # #
    # print('\n# rotate example 1')
    # arr = StaticArray(5)
    # source = [_ for _ in range(-20, 20, 7)]
    # arr = StaticArray(len(source))
    # for i, value in enumerate(source):
    #     arr.set(i, value)
    # for steps in [1, 2, 0, -1, -2, 28, -100]:
    #     print(rotate(arr, steps), steps)

    # print('\n# sa_range example 1')
    # cases = [
    #     (27628, 27619), (1, 3), (-1, 2), (0, 0), (0, -3), (-105, -99), (-99, -105)
    #     ]
    # for start, end in cases:
    #     print(start, end, sa_range(start, end))
    #

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        [1, 2, 2, 3],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        [46201, 15978, 5116, -30706, -55036, -63659, -79897],
        [-89633, -75561, -68679, -68289, -63274, -62237, -56369, -37602, -23762, -7922, -7204, 12807, 13698, 13698,
         27835, 38886, 50543, 51539, 51693, 65291, 74208, 99616, 99784],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print('Result:', is_sorted(arr), arr)

    # print('\n# sa_sort example 1')
    # test_cases = (
    #     [1, 10, 2, 20, 3, 30, 4, 40, 5],
    #     ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
    #     [(1, 1), (20, 1), (1, 20), (2, 20)],
    #     [random.randrange(-30000, 30000) for _ in range(5_000)]
    # )
    # for case in test_cases:
    #     arr = StaticArray(len(case))
    #     for i, value in enumerate(case):
    #         arr[i] = value
    #     print(arr if len(case) < 50 else 'Started sorting large array')
    #     sa_sort(arr)
    #     print(arr if len(case) < 50 else 'Finished sorting large array')
    #
    #
    #
    # print('\n# remove_duplicates example 1')
    # test_cases = (
    #     [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
    #     [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    # )
    # for case in test_cases:
    #     arr = StaticArray(len(case))
    #     for i, value in enumerate(case):
    #         arr[i] = value
    #     print("before", arr)
    #     print("after", remove_duplicates(arr))
    # print(arr)

    # print('\n# count_sort example 1')
    # test_cases = (
    #     [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
    #     [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
    #     [random.randrange(-499, 499) for _ in range(10000)]
    # )
    # for case in test_cases:
    #     arr = StaticArray(len(case))
    #     for i, value in enumerate(case):
    #         arr[i] = value
    #     print(arr if len(case) < 50 else 'Started sorting large array')
    #     result = count_sort(arr)
    #     print(result if len(case) < 50 else 'Finished sorting large array')


    print('\n# sa_intersection example 1')
    test_cases = ( ([1, 2, 3], [3, 4, 5], [2, 3, 4]), ([1, 2], [2, 4], [4, 3]), ([1, 1, 2, 2, 5, 75], [1, 2, 2, 12, 75, 90], [-5, 2, 2, 2, 20, 75, 95]),
                   ([[1, 1, 2, 2, 5, 75], [1, 2, 2, 12, 75, 90], [-5, 2, 2, 2, 20, 75, 95]] ),
                   ([-8, -7, -4, -1, 2, 6, 10], [-9, -8, -7, -7, -6, -2, 1, 9], [-9, -7, 1, 8, 9]),
                   ([0, 1, 5, 8, 9, 10], [-10, -6, -6, -5, 5, 8, 8, 9, 9, 10],[-8, 3, 5, 8, 8]),
                   ([8], [8, 8], [8, 8])
                   )
    for case in test_cases:
        arr = []
        for i, lst in enumerate(case):
            arr.append(StaticArray(len(lst)))
            for j, value in enumerate(sorted(lst)):
                arr[i][j] = value
        print(sa_intersection(arr[0], arr[1], arr[2]))

    # print('\n# sorted_squares example 1')
    # test_cases = (
    #     [1, 2, 3, 4, 5],
    #     [-5, -4, -3, -2, -1, 0],
    #     [-3, -2, -2, 0, 1, 2, 3],
    #     [random.randrange(-10_000, 10_000) for _ in range(1_000_000)]
    # )
    # for case in test_cases:
    #     arr = StaticArray(len(case))
    #     for i, value in enumerate(sorted(case)):
    #         arr[i] = value
    #     print(arr if len(case) < 50 else 'Started sorting large array')
    #     result = sorted_squares(arr)
    #     print(result if len(case) < 50 else 'Finished sorting large array')
    #
    # print('\n# add_numbers example 1')
    # test_cases = (
    #     ([1, 2, 3], [4, 5, 6]),
    #     ([0], [2, 5]),
    #     ([2, 0, 9, 0, 7], [1, 0, 8]),
    #     ([9, 9, 9], [9, 9, 9, 9])
    # )
    # for num1, num2 in test_cases:
    #     n1 = StaticArray(len(num1))
    #     n2 = StaticArray(len(num2))
    #     for i, value in enumerate(num1):
    #         n1[i] = value
    #     for i, value in enumerate(num2):
    #         n2[i] = value
    #     print('Original nums:', n1, n2)
    # #     print('Sum: ', add_numbers(n1, n2))
    #
    # print('\n# balanced_strings example 1')
    # test_cases = (
    #     'aaabbbccc', 'abcabcabc', 'babcCACBCaaB', 'aBcCbA', 'aBc',
    #     'aBcaCbbAcbCacAbcBa', 'aCBBCAbAAcCAcbCBBa', 'bACcACbbACBa',
    #     'CBACcbcabcAaABb'
    # )
    # for case in test_cases:
    #     print(balanced_strings(case))

    # #
    # print('\n# transform_strings example 1')
    # test_cases = ('eMKCPVkRI%~}+$GW9EOQNMI!_%{#ED}#=-~WJbFNWSQqDO-..@}',
    #               'dGAqJLcNC0YFJQEB5JJKETQ0QOODKF8EYX7BGdzAACmrSL0PVKC',
    #               'aLiAnVhSV9}_+QOD3YSIYPR4MCKYUF9QUV9TVvNdFuGqVU4$/%D',
    #               'zmRJWfoKC5RDKVYO3PWMATC7BEIIVX9LJR7FKtDXxXLpFG7PESX',
    #               'hFKGVErCS$**!<OS<_/.>NR*)<<+IR!,=%?OAiPQJILzMI_#[+}',
    #               'EOQUQJLBQLDLAVQSWERAGGAOKUUKOPUWLQSKJNECCPRRXGAUABN',
    #               'WGBKTQSGVHHHHHTZZZZZMQKBLC66666NNR11111OKUN2KTGYUIB',
    #               'YFOWAOYLWGQHJQXZAUPZPNUCEJABRR6MYR1JASNOTF22MAAGTVA',
    #               'GNLXFPEPMYGHQQGZGEPZXGJVEYE666UKNE11111WGNW2NVLCIOK',
    #               'VTABNCKEFTJHXATZTYGZVLXLAB6JVGRATY1GEY1PGCO2QFPRUAP',
    #               'UTCKYKGJBWMHPYGZZZZZWOKQTM66666GLA11111CPF222RUPCJT')
    # for case in test_cases:
    #     print(transform_string(case, '612HZ', '261TO'))
