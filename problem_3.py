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

    def dequeue(self):

        if len(self.list) == 1:
            return None

        if len(self.list) == 2:
            return self.list.pop()[0]

        # First entry in list (appart from 0 entry) is lowest priority
        sol = self.list[1][0]

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

        return sol

def test_sorted_queue():
    q = SortedQueue()

    test_entries = (("E", 12), ("A", 1), ("D", 10), ("C", 5), ("B", 2))
    test_ordered = ("A", "B", "C", "D", "E")

    for value, priority in test_entries:
        q.enqueue(value, priority)
    
    for value in test_ordered:
        assert(q.dequeue() == value)
    
test_sorted_queue()