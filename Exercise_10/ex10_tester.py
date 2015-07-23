""" Exercise 10 tester"""
from ex10 import *


my_tree = BTNode(10,BTNode(3,BTNode(5),BTNode(2)),BTNode(7,BTNode(4,BTNode(9)),BTNode(6)))
print(my_tree)

print("leaves and internals ", my_tree.leaves_and_internals())

print(my_tree)
print("sum to deepest", my_tree.sum_to_deepest())

print(my_tree)
my_tree.set_depth(0)

print(my_tree)
my_tree.set_depth(1)

print(my_tree)

my_tree_b = BTNode(-100,BTNode(10,BTNode(3,BTNode(5),BTNode(2,BTNode(0,BTNode(0)))),BTNode(7,BTNode(4,BTNode(9)),BTNode(6))))

print(my_tree_b)

print("sum to deepest", my_tree_b.sum_to_deepest())

print("leaves and internals ", my_tree_b.leaves_and_internals())
