""" Exercise 6

Joshua Fung
June 25th, 2015

Four function:
rsum: Return sum
rmax: Return max
second_smallest: Return second smallest
sum_max_min: Return the sum of max and min
"""


def rsum(in_list):
    """(list) -> int

    Return the sum of the list
    """
    if(len(in_list) == 1):
        return in_list[0]

    else:
        return in_list[0] + rsum(in_list[1:])


def rmax(in_list):
    """(list) -> int

    Return the max of the list
    """
    if(len(in_list) == 1):
        return in_list[0]

    else:
        first_element = in_list[0]
        largest_after = rmax(in_list[1:])

        if(first_element >= largest_after):
            return first_element
        else:
            return largest_after


def second_smallest(in_list, first_call=True):
    """(list, Boole) -> int/list

    Return the second smallest of the list
    """
    if(first_call):
        return second_smallest(in_list, False)[1]

    else:
        if(len(in_list) == 2):
            a = in_list[0]
            b = in_list[1]

            if(a > b):
                return [b, a]
            else:
                return [a, b]

        else:
            first_element = in_list[0]
            next_smallest2 = second_smallest(in_list[1:], False)

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


""" This is a more sensible implementation of the second_smallest but I
don't like it. So it is commented out.


def second_smallest(in_list):
    ""(list) -> int

    Return the second smallest of the list
    ""
    smallest2 = _sec_sma_helper(in_list)
    return smallest2[1]


def _sec_sma_helper(in_list):
    ""(list) -> list

    Return [smallest, second smallest]
    ""
    if(len(in_list) == 2):
            a = in_list[0]
            b = in_list[1]

            if(a > b):
                return [b, a]
            else:
                return [a, b]

        else:
            first_element = in_list[0]
            next_smallest2 = second_smallest(in_list[1:], False)

            if(first_element >= next_smallest2[1]):
                return next_smallest2

            elif(first_element < next_smallest2[1] and
                 first_element >= next_smallest2[0]):
                return [next_smallest2[0], first_element]

            else:
                return [first_element, next_smallest2[0]]
"""
