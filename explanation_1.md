All operations are O(1), which is accomplished by maintaining a dictionary with all key-value pairs, a doubly-linked list of all keys, and a dictionary that points to each node of the linked-list given the key.

The "oldest entry" information is obtained from the doubly linked list, while the dictionary that points to each individual node is used to allow finding nodes that are not in the head or tail in O(1).

Clearly, reducing time complexity is given priority over space complexity. For each pair key-value, LRU-Cache stores 1 reference to the value, 3 references to the key, and 3 references to each Node object (1 node per key)
