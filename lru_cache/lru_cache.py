from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):

        # max number of nodes it can hold
        self.limit = limit
        # current number of nodes it holding
        self.current = 0 

        # doubly linked list that holds entries in order
        self.order = DoublyLinkedList()

        # storage dict
        self.storage = {}


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):

        # check if key is in {}
        if key in self.storage:
            # if yes, then move the key to front
            # in this case, the node is the value attached to the key
            node = self.storage[key]
            self.order.move_to_front(node)
            # return only the value associated with the key
            return node.value[1]
        else:
            return None


    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):

        # if key exists, overwrite
        if key in self.storage:
            # we need value and node to update
            # update dict, set to new value
            # note: each key is associated with a key-value pair
            node = self.storage[key]
            node.value = (key, value)
            # put at head of the DLL
            self.order.move_to_front(node) 
            return 

        # if max capacity, drop oldest entry before adding
        elif self.current == self.limit:
            # delete oldest key value pair in {} first with the key
            del self.storage[self.order.tail.value[0]]
            # remove tail from DLL 
            self.order.remove_from_tail()
            self.current -= 1
        
        # add to the cache - add to dict and nodes/DLL
        # add to dict 
        self.storage[key] = value
        # add to nodes
        self.order.add_to_head((key, value))
        # update counter
        self.current += 1