from ex5 import *

a = DLList()

for x in range(1, 7):
    a.add_to_head(x)

print(a)

b = DLList()

for x in range(1, 7):
    b.add_to_tail(x)

print(b)

for x in range(1, 7):
    print(a.remove_head())
    print(a)

for x in range(1, 7):
    print(b.remove_tail())
    print(b)

import random

c = DLList()

for x in range(1, 20):
    c.add_to_head(random.randrange(0,100,1))

for x in range(1, 101):
    if(c.search(x) > 0):
        print(x)
        
d = SortedList()
d._list.add_to_head(2)
d._list.add_to_head(3)
d._list.add_to_head(4)
d._list.add_to_head(5)

print(d._list)

e = SortedList()

for x in range(1, 2000):
    e.add(random.randrange(0,100,1))

e.add(-10)
e.add(100)


print(e)

e.remove(-10)

print(e)

e.remove(100)

print(e)
