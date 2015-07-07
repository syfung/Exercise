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
            temp = _sec_sma_helper(in_list[0])
            print("len 1, is list" + str(temp))
            return temp
        else:
            temp = [in_list[0], None]
            print("len 1, not list" + str(temp))
            return temp
    else:
        if(isinstance(in_list[0], list)):
            first = _sec_sma_helper(in_list[0])
            print("len greater, first", first)
        else:
            first = [in_list[0], None]
            print("len greater, first, list", first)
        second = _sec_sma_helper(in_list[1:])
        print("len greater, second" + str(second))

        if(first[0] <= second[0]):
            temp = [first[0], second[0]]
            if(first[1] is not None):
                if(first[1] <= temp[1]):
                    temp[1] = first[1]
        else:
            temp = [second[0], first[0]]
            if(second[1] is not None):
                if(second[1] <= temp[1]):
                    temp[1] = second[1]

        print("temp: ", temp)
        return temp


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
        if(isinstance(in_list[0], list)):
            return _sum_helper(in_list[0])
        else:
            return [in_list[0], in_list[0]]

    else:

        if(isinstance(in_list[0], list)):
            first_element = _sum_helper(in_list[0])
        else:
            first_element = [in_list[0], in_list[0]]

        next_min_max = _sum_helper(in_list[1:])

        temp = next_min_max

        if(first_element[1] > next_min_max[1]):
            temp[1] = first_element[1]

        if(first_element[0] < next_min_max[0]):
            temp[0] = first_element[0]

        return temp
