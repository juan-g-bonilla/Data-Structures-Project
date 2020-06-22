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

def get_huffman_codes(root, prevCode = ""):

    dic = dict()

    for node, i in ((root.left, "0"), (root.right, "1")):
        newCode = prevCode + i
        if isinstance(node, BiNode):
            dic = {**dic, **get_huffman_codes(node, newCode)}
        else:
            dic[node] = newCode

    return dic
    
def huffman_encoding(data):

    appearances = dict()
    for c in data:
        appearances[c] = appearances.get(c, 0) + 1

    queue = SortedQueue()
    for i, j in appearances.items():
        queue.enqueue(i, j)

    root = create_huffman(queue)

    dataStr = ""
    codes = get_huffman_codes(root)
    for c in data:
        dataStr = dataStr + codes[c]

    return dataStr, root

def huffman_decoding(dataStr, data):

    codes = get_huffman_codes(data)
    codes_inv = {v: k for k, v in codes.items()}

    result = ""
    buffer = ""
    for i in dataStr:
        buffer += i
        if buffer in codes_inv:
            result += codes_inv[buffer]
            buffer = ""
    
    return result

def test_sorted_queue():
    q = SortedQueue()

    test_entries = (("E", 12), ("A", 1), ("D", 10), ("C", 5), ("B", 2))
    test_ordered = ("A", "B", "C", "D", "E")

    for value, priority in test_entries:
        q.enqueue(value, priority)
    
    for value in test_ordered:
        assert(q.dequeue() == value)

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

def test_get_huffman_codes():
    q = SortedQueue()

    q.enqueue("D", 2)
    q.enqueue("B", 3)
    q.enqueue("E", 6)
    q.enqueue("A", 7)
    q.enqueue("C", 7)

    root = create_huffman(q)

    dic = get_huffman_codes(root)

    for i, j in (("D", "000"), ("B", "001"), ("E","01"),("A", "10"), ("C", "11")):
        assert(dic[i] == j)

def test_huffman_encoding():
    test_cases = ("IYFVLUIYV1aH", "ABC", "IA")

    for i in test_cases:
        assert(i == huffman_decoding(*huffman_encoding(i)))

def test_methods():
    test_sorted_queue()
    test_create_huffman()
    test_get_huffman_codes()
    test_huffman_encoding()

test_methods()