from ex5 import *


# Test DLLNode
node = DLLNode(3)
node_node_none = DLLNode(4, node) 

print(node)
print(node_node_none)
print(node_node_none.get_prev())
print(node_node_none.get_next())

print(node_node_none.data)
print(node_node_none.prev_node)
print(node_node_none.next_node)


# Test the add_to_head and add_to_tail
a = DLList()

print("***Add to head")

for x in range(1, 7):
    a.add_to_head(x)

print(a)

print("***Add to tail")

for x in range(1, 7):
    a.add_to_tail(x)

print(a)

print("***Remove head")

for x in range(1, 7):
    print(a.remove_head())
    print(a)

print("***Remove tail")
    
for x in range(1, 7):
    print(a.remove_tail())
    print(a)

print("***Search")

for x in range(1, 7):
    a.add_to_tail(x)

print(a)

print(a.search(4))

# Test SortedList with random
print("***SortedList""")
import random


b = SortedList()

num = 10

for x in range(1, num):
    print(b)
    b.add(random.randrange(0,100,1))
    print(b)

for x in range(1, num):
    print(b)
    print(b.middle())
    b.remove(b.middle())

print(b)
