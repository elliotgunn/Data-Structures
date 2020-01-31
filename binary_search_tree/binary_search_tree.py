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
        cb(self.value)

        # check left
        if self.left != None:
            self.left.for_each(cb)
        
        # check right
        if self.right != None:
            self.right.for_each(cb)
        
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # recurse left
        if self.left:
            self.left.in_order_print(self.left)
        # then print after recursed all on the left
        # print values on the right 
        print(self.value)
        # then recurse right
        if self.right:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # instantiate queue
        # add root to queue  
        queue = Queue()
        queue.enqueue(node)

        while queue.len() > 0:
            # dequeue root and print
            current = queue.dequeue()
            print(current.value)

            # check node for children and add to queue
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # instantiate stack
        # add root to stack 
        stack = Stack()
        stack.push(node)

        # similar to above
        while stack.len() > 0: 
            current = stack.pop()
            print(current.value)
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)

        







    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
