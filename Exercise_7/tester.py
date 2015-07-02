import ex7


a = [1, [2, 3], [4, [5]]]
b = [[5], [5, 9], [6, [10, [20]]]]

try:
    print("Checking rsum, test a")
    ans = ex7.rsum(a)
    print(ans)
except:
    print("Failed rsum, test a")
else:
    if(ans == 15):
        print("Passed rsum, test a")
    else:
        print("Failed rsum, test a")

print("----------")
        
try:
    print("Checking rsum, test b")
    ans = ex7.rsum(b)
    print(ans)
except:
    print("Failed rsum, test b")
else:
    if(ans == 55):
        print("Passed rsum, test b")
    else:
        print("Failed rsum, test b")
