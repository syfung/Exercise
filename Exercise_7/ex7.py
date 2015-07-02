""" CSC148 Exercise 7
Joshua Fung
June 30th, 2015

Four Functions:
rsum: Return sum
rmax: Return max
second_smallest: Return second smallest
sum_max_min: Return the sum of max and min

The different of this exercise than exercise_6 is that instead of
working with a single list of intergers it needs to work with a
combination of nested list and list.

For example:
[1, 2, 3]
[1, [2, 3]]
[[1], [2, [3]], [1]]

Most of the code will be based from exercise 6 code, except the second
smallest function I will use the helper function version.
"""


# For now we will start with coping the old code form ex6.py
def rsum(in_list):
    """(list) -> int

    Return the sum of the list
    """
    # We will change this by checking if the element is a list
    if(len(in_list) == 1):
        if(isinstance(in_list[0], list)):
            return rsum(in_list[0])
        else:
            return in_list[0]

    else:
        if(isinstance(in_list[0], list)):
            return rsum(in_list[0]) + rsum(in_list[1:])

        else:
            return in_list[0] + rsum(in_list[1:])


def rmax(in_list):
    """(list) -> int

    Return the max of the list
    """
    if(len(in_list) == 1):
        if(isinstance(in_list[0], list)):
            return rmax(in_list[0])
        else:
            return in_list[0]

    else:
        if(isinstance(in_list[0], list)):
            first_element = rmax(in_list[0])
        else:
            first_element = in_list[0]

        largest_after = rmax(in_list[1:])

        if(first_element >= largest_after):
            return first_element
        else:
            return largest_after


def second_smallest(in_list):
    """(list) -> int

    Return the second smallest of the list
    """
    smallest2 = _sec_sma_helper(in_list)
    return smallest2[1]


def _sec_sma_helper(in_list):
    """(list) -> list

    Return [smallest, second smallest]
    """
    if(len(in_list) == 1):
        if(isinstance(in_list[0], list)):
            print("len 1" + in_list[0])
            return _sec_sma_helper(in_list[0])
        else:
            return [None, in_list[0]]
        
    if(len(in_list) == 2):
        if(isinstance(in_list[0], list)):
            a = _sec_sma_helper(in_list[0])
        else:
            a = in_list[0]
        if(isinstance(in_list[1], list)):
            b = _sec_sma_helper(in_list[1])
        else:
            b = in_list[1]

            if(a > b):
                return [b, a]
            else:
                return [a, b]

    else:
        if(isinstance(in_list[0], list)):
            print("else, list" + in_list)
            first_element = _sec_sma_helper(in_list[0])
        else:
            first_element = in_list[0]

        
        print("else, nextsmallest2" + str(in_list[1:]))
        next_smallest2 = _sec_sma_helper(in_list[1:])
        print(next_smallest2)

        if(first_element >= next_smallest2[1]):
            return next_smallest2

        elif(first_element < next_smallest2[1] and
             first_element >= next_smallest2[0]):
            return [next_smallest2[0], first_element]

        else:
            return [first_element, next_smallest2[0]]


def sum_max_min(in_list):
    """(list) -> int

    Return the sum of min and max
    """
    min_max = _sum_helper(in_list)
    return min_max[0] + min_max[1]


def _sum_helper(in_list):
    """(list) -> list

    Return [min, max]
    """
    if(len(in_list) == 1):
        return [in_list[0], in_list[0]]

    else:
        first_element = in_list[0]
        next_min_max = _sum_helper(in_list[1:])

        if(first_element > next_min_max[1]):
            return [next_min_max[0], first_element]

        elif(first_element < next_min_max[0]):
            return [first_element, next_min_max[1]]

        else:
            return next_min_max
