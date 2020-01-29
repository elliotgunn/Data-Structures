import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # for this function to work, must already have a tree or root existing
        # if value < self.value, go left 
        # else go right
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
                # keep going -- recursion 
            else:
                self.left.insert(value)

        elif value >= self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
                # keep going
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target == self.value, return it
        # base case:
        if target == self.value:
            return True 
        
        # left side
        elif target < self.value:
            if self.left == None:
                return False 
            else: 
                # recurse
                return self.left.contain(target)
        
        # right side
        else: 
            if self.right == None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # if right exists, go right
        # otherwise return self.value
        if self.right != None:
            # recurse
            return self.right.get_max()
        else: 
            return self.value


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
