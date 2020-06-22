
"""
Node for implementation of doubly-linked lists
"""
class BiNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

"""
Cache following the "Least Recently Used" (LRU) policy.
The object internally maintains a dictionary for key-value access, a doubly-
linked list for the keys in order of access, and a dictionary that points
to each Node of the list
All operations are O(1)
"""
class LRU_Cache(object):

    def __init__(self, capacity):

        if capacity < 1:
            raise ValueError("Capacity must be a natural number")

        self.main = dict()
        self.keys = dict()

        self.head = None
        self.tail = None

        self.cap = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.main:
            return -1           

        self._place_key_at_head(key)
        return self.main[key]

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        self._place_key_at_head(key)
        self.main[key] = value

    def _place_key_at_head(self, key):

        if key in self.keys: # Key was already in cache, move said node to head
            node = self.keys[key]

            if node is not self.head: # If already at head ignore

                node.prev.next = node.next # "Stich" the gap

                if node is self.tail:
                    self.tail = node.prev # Set reference to new tail

                node.next = self.head
                self.head.prev = node
                self.head = node

        else:
            node = BiNode(key)
            self.keys[key] = node

            if self.tail is None:
                self.tail = node
            elif self.tail.prev is None:
                self.tail.prev = node
                node.next = self.tail

            if self.head is not None:
                self.head.prev = node
                node.next = self.head 
            
            self.head = node

            if self.cap < len(self.keys): # If over size, remove tail
                del self.keys[self.tail.value]
                del self.main[self.tail.value]
                self.tail.prev.next = None
                self.tail = self.tail.prev
        
def test_LRU_Cache():
    cache = LRU_Cache(5)

    cache.set(1, 1)
    cache.set("2", 2)
    cache.set(3, 3)
    cache.set("a4", 4)

    cache.set(1, 1.5) 

    cache.set(5, 5)
    cache.set(6, 6)

    assert(cache.get(1) == 1.5) # 1 should not be removed since we have recently re-set it
    assert(cache.get("2") == -1) # 2 should be the oldest, thus removed
    assert(cache.get(3) == 3) # 3 should not be removed

    cache.set(7, 7)

    assert(cache.get("a4") == -1 ) # a4 should now be removed

    assert(len(cache.main) == 5)
    assert(len(cache.keys) == 5)

if __name__ == "__main__":
    test_LRU_Cache()