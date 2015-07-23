""" CSC148 Exercise 10 Binary Tree

Joshua Fung
July 22nd, 2015

The goal is implement all of these function with recursion under 15
lines.
"""


class BTNode(object):
    """A node in a binary tree."""

    def __init__(self, value, left=None, right=None):
        """(BTNode, int, BTNode, BTNode) -> NoneType
        Initialize this node to store value and have children left and right,
        as well as depth 0.
        """
        self.value = value
        self.left = left
        self.right = right
        self.depth = 0  # the depth of this node in a tree

    def __str__(self):
        return self._str_helper("")

    def _str_helper(self, indentation=""):
        """(BTNode, str) -> str
        Return a "sideways" representation of the subtree rooted at this node,
        with right subtrees above parents above left subtrees and each node on
        its own line, preceded by as many TAB characters as the node's depth.
        """
        ret = ""

        if(self.right is not None):
            ret += self.right._str_helper(indentation + "\t") + "\n"
        ret += indentation + str(self.value) + "\n"
        if(self.left is not None):
            ret += self.left._str_helper(indentation + "\t") + "\n"
        return ret

    def set_depth(self, depth=0):
        """(BTNode, int) -> NoType
        Set the depth of the node the method belongs to. Also set the
        depth for the children node recursively to the depth puls level
        """
        # If there is a right child node
        if(self.right is not None):
            self.right.set_depth(depth + 1)

        # If there is a left child node
        if(self.left is not None):
            self.left.set_depth(depth + 1)

        # Set own depth
        self.depth = depth

    def leaves_and_internals(self, is_root=True):
        """(BTNode, bool) -> tuple
        Return a tuple with two sets. The first set is vlues of the
        leaves and the secound is the set of the internal node

        Leaves are node that don't have child, and internal are the
        rest except the root node
        """
        # Create the tuple with two set
        ret_tuple = (set(), set())

        # If it is a leaf noed
        if(self.right is None and self.left is None):
            ret_tuple[0].add(self.value)

        # If it is not a leaf node
        else:
            # Make sure it is not head (internals)
            if(not is_root):
                ret_tuple[1].add(self.value)

            # If there is a right node
            if(self.right is not None):
                right_tuple = self.right.leaves_and_internals(False)
                ret_tuple[1].update(right_tuple[1])
                ret_tuple[0].update(right_tuple[0])

            # If there is a left node
            if(self.left is not None):
                left_tuple = self.left.leaves_and_internals(False)
                ret_tuple[1].update(left_tuple[1])
                ret_tuple[0].update(left_tuple[0])

        return ret_tuple

    def sum_to_deepest(self):
        """(BTNode) -> int
        Return the sum of all vlues on the longest path, if there are
        node that have equal deepth return the max sum
        """
        # Call the helper function
        return self._sum_to_deepest_helper()[0]

    def _sum_to_deepest_helper(self, depth=0):
        """(BTNode, int) -> list
        Return a list with the sum of the longest path value and the
        length of  the longes path.
        """
        # Create the empty return, if there is no childern node these
        # will work like the deepest is the current depth with no
        # value
        right_sum = [0, depth]
        left_sum = [0, depth]

        # If there is a children node on right
        if(self.right is not None):
            # Recursively call one dpther on the right
            right_sum = self.right._sum_to_deepest_helper(depth + 1)

        # If there is a left node
        if(self.left is not None):
            # Recursively call one dpther on the left
            left_sum = self.left._sum_to_deepest_helper(depth + 1)

        # Assume right sum or depth is greater than left
        depth = right_sum[1]
        max_sum = self.value + right_sum[0]

        # If that is not the case change it
        if(right_sum[1] == left_sum[1]):
            if(right_sum[0] < left_sum[0]):
                max_sum = self.value + left_sum[0]

        elif(right_sum[1] < left_sum[1]):
            depth = left_sum[1]
            max_sum = self.value + left_sum[0]

        # Return the max_sum and depth
        return [max_sum, depth]
