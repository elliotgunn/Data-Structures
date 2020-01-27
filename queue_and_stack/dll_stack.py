import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        """ 
        This inserts the value at the top of the stack.
        """
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        """
        Removes the value at the top of the stack. 
        """
        if self.size == 0:
            return None
        
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size
