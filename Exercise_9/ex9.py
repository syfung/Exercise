''' Exercise 9 Binary Search Tree 

Joshua Fung
July 14, 2015
'''


class BSTNode(object):
    '''A binary serach tree node'''
    def __init__(self, content, smaller=None, greater=None):
        self._content = content
        self._smaller = smaller
        self._greater = greater

    def __str__(self):
        return str(self._content)

    def print_tree(self, indent=""):
        if(self._smaller is not None):
            self._smaller.print_tree(indent + "\t")

        print (indent + str(self._content))
        
        if(self._greater is not None):
            self._greater.print_tree(indent + "\t")

class BST(object):
    def __init__(self):
        self._head = None

    def print_tree(self):
        self._head.print_tree()

    def traversal(self):
        self._pre_order_helper(self._head)
        print()
        self._in_order_helper(self._head)
        print()
        self._post_order_helper(self._head)
        print()
        
    def _pre_order_helper(self, node):
        print(node, end=',')

        if(node._smaller is not None):
            self._pre_order_helper(node._smaller)
            
        if(node._greater is not None):
            self._pre_order_helper(node._greater)

    def _in_order_helper(self, node):
        if(node._smaller is not None):
            self._in_order_helper(node._smaller)

        print(node, end=',')
            
        if(node._greater is not None):
            self._in_order_helper(node._greater)

    def _post_order_helper(self, node):
        if(node._smaller is not None):
            self._post_order_helper(node._smaller)
            
        if(node._greater is not None):
            self._post_order_helper(node._greater)

        print(node, end=',')
            
    def insert(self, content):
        if(self._head is None):
            self._head = BSTNode(content)
        else:
            self._insert_helper(self._head, content)
            
    def _insert_helper(self, node, content):
        if(content <= node._content):
            if(node._smaller is None):
                node._smaller = BSTNode(content)
            else:
                self._insert_helper(node._smaller, content)

        else:
            if(node._greater is None):
                node._greater = BSTNode(content)
            else:
                self._insert_helper(node._greater, content)


a = BST()
a.insert("C")
a.insert("O")
a.insert("M")
a.insert("P")
a.insert("U")
a.insert("T")
a.insert("E")
a.insert("R")
a.insert("S")

a.print_tree()

a.traversal()

b = BST()

x = "SRETUPMOC"

for c in x:
    b.insert(c)

b.print_tree()

b.traversal()
