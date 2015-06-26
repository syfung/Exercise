""" Exercise 6

Joshua Fung
June 25th, 2015

Foure function:
rsum: Reutrn sum
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
    """(list, bool) -> int/list

    Return the second smallest of the list
    """

    
""" This is a more sensible implmentation of the second_smallest but I
don't like it. So it is commented out.


def second_smallest(in_list):
    ""(list) -> int

    Return the second smallest of the list
    ""


def _sec_sma_helper(in_list):
    ""(list) -> list

    Return [smallest, second smallest]
    ""
"""

    

def sum_max_min(in_list):
    """(list) -> int

    Return the sum of max and min
    """


def _sum_helper(in_list):
    """(list) -> list
    
    Return [max, min]
    """
