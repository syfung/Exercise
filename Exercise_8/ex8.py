""" CSC148 Exercise 8

Joshua Fung
July 10th, 2015

Three function with hard and easy version:

Easy:
edit_distance(str, str)
subsequence(str, str)
gcd(int, int)

Hard (optional):
edit_distance_h(str, str)
subsequence_h(str, str)
gcd_h(int, int)
"""


def edit_distance(s1, s2):
    """(str, str) -> int

    Return the minimum number of single character changes needed to
    turn S1 to S2

    >>>edit_distance("took", "hook")
    1
    """
    # For the easy version needs the str to be same length
    if(len(s1) != len(s2)):
        raise

    # Base case N-1 approch (len == 1), len(s1) == len(s2)
    if(len(s1) == 1):
        # Compare the two single char, euqal edit dis = 0
        if(s1[0] == s2[0]):
            return 0
        # Unequal need to change edit dis = 1
        else:
            return 1

    # Other than base take the first off, recursion
    else:
        # Compare the first characters
        first = 0
        if(s1[0] != s2[0]):
            first = 1

        # Compare the rest
        rest = edit_distance(s1[1:], s2[1:])

        # Return total
        return first + rest


def subsequence(s1, s2):
    """(str, str) -> bool
    Check if s1 is a subsequence of s2
    (like if s1 is contained is s2)
    It is implied that "" is in all str

    >>>subsequence("", "Ha")
    True
    >>>subsequence("took", "ntdfdogfogk")
    True
    """
    # If s1 is longer that s2 return false
    if(len(s1) > len(s2)):
        return False

    # The base case is always that the s1 is a empty string
    if(s1 == ""):
        return True

    # Else compare first element of s1 and s2
    # If match remove both element to the recusion call
    if(s1[0] == s2[0]):
        return subsequence(s1[1:], s2[1:])
    # Else only remove the unmatched s2 charter
    else:
        return subsequence(s1, s2[1:])


def gcd(a, b):
    """(int, int) -> int
    Return the greatest common denominator of the two int

    >>>gdc(5, 0)
    5
    >>>gcd(12345678, 87654321)
    9
    """
    # Since the algorithm only works with a < b, we flip it is needed
    if(a > b):
        temp = a
        a = b
        b = temp

    # Base case, if b is 0 a is the gcd
    if(a == 0):
        return b

    else:
        # Find the gcd of the remainder
        return gcd(a, b % a)


def edit_distance_h(s1, s2):
    """(str, str) -> int
    """


def subsequence_h(s1, s2):
    """(str, str) -> list
    """


def gcd_h(a, b):
    """(int, int) -> int
    """
