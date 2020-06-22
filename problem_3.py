"""
Implementation of a sorted queue using a binary heap.
Enqueue and dequeue operations take O(log n) time.
Internally, the heap is implemented using a python list.
"""
class SortedQueue:
    def __init__(self):
        self.list = [(None, 0)]

    def enqueue(self, value, priority):
        ind = len(self.list)
        self.list.append((value, priority))

        while ind > 0:
            if self.list[ind//2][1] > priority:
                self.list[ind], self.list[ind//2] = self.list[ind//2], self.list[ind]
            ind = ind // 2

    def dequeue(self, returnPriority = False):

        if len(self.list) == 1:
            return None, None if returnPriority else None

        if len(self.list) == 2:
            return self.list.pop() if returnPriority else self.list.pop()[0]

        # First entry in list (appart from 0 entry) is lowest priority
        sol, priority = self.list[1]
        
        # Re order tree
        self.list[1] = self.list.pop() # Place last entry in front
        ind = 1
        while ind *2 < len(self.list):

            # Find index of child of node "ind" with lowest priority
            if ind*2 + 1 >= len(self.list): # If only one child, select that one
                ind2 = ind*2

            elif self.list[ind*2][1] < self.list[ind*2 + 1][1]:
                ind2 = ind*2
            
            else:
                ind2 = ind*2 + 1

            # Swap entry at ind and its child at ind2
            if self.list[ind][1] > self.list[ind2][1]:
                self.list[ind], self.list[ind2] = self.list[ind2], self.list[ind]

            ind = ind2

        return (sol, priority) if returnPriority else sol

    def __len__(self):
        return len(self.list)-1
        
def test_sorted_queue():
    q = SortedQueue()

    test_entries = (("E", 12), ("A", 1), ("D", 10), ("C", 5), ("B", 2))
    test_ordered = ("A", "B", "C", "D", "E")

    for value, priority in test_entries:
        q.enqueue(value, priority)
    
    for value in test_ordered:
        assert(q.dequeue() == value)
    
class BiNode:
    def __init__(self):
        self.left = None
        self.right = None

def create_huffman(queue):
    
    if len(queue) == 0:
        return None

    while len(queue) > 1:
        node = BiNode()
        node.left, leftPrior = queue.dequeue(True)
        node.right, rightPrior = queue.dequeue(True)
        queue.enqueue(node, leftPrior + rightPrior)

    return queue.dequeue()
    
def test_create_huffman():
    q = SortedQueue()

    q.enqueue("D", 2)
    q.enqueue("B", 3)
    q.enqueue("E", 6)
    q.enqueue("A", 7)
    q.enqueue("C", 7)

    root = create_huffman(q)

    assert(root.left.left.left == "D")
    assert(root.left.left.right == "B")
    assert(root.left.right == "E")
    assert(root.right.left == "A")
    assert(root.right.right == "C")

test_sorted_queue()
test_create_huffman()