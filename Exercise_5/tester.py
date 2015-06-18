from ex5 import *

a = DLList()

for x in range(1, 7):
    a.add_to_head(x)

print(a)

b = DLList()

for x in range(1, 7):
    b.add_to_tail(x)

print(b)

for x in range(1,7):
    print(a.remove_head())
    print(a)

for x in range(1,7):
    print(b.remove_tail())
    print(b)
