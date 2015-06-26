import ex6
import sys
import random


sum_test_single_element = [5]

try:
    sum = ex6.rsum(sum_test_single_element)
except:
    print("Failed rsum single element test")
    print(sys.exc_info()[0])
else:
    if(sum == 5):
        print("Passed rsum single element test")
    else:
        print("Failed rsum single element test")


sum_test_list = [5,9,2,6]

try:
    sum = ex6.rsum(sum_test_list)
except:
    print("Failed rsum test")
    print(sys.exc_info()[0])
else:
    if(sum == 22):
        print("Passed rsum test")
    else:
        print("Failed rsum test")


sum_test_neg = [-5, -10, -20]

try:
    sum = ex6.rsum(sum_test_neg)
except:
    print("Failed rsum with negative number test")
    print(sys.exc_info()[0])
else:
    if(sum == -35):
        print("Passed rsum with negative number test")
    else:
        print("Failed rsum with negative number test")

        
