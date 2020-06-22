class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, initial = []):
        self.head = None

        if initial is not None:
            for i in initial:
                self.append(i)

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):
        """
        Appends given value to the end of the list

        Args:
            value (): value to append. If node is passed, the node is appended, 
            else a node is created to contain the value
        """
        toAppend = None if value is None else value if isinstance(value, Node) else Node(value)

        if self.head is None:
            self.head = toAppend
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = toAppend

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def copy(self):
        """
        Shallow copy of the LinkedList
        """
        return LinkedList([i for i in self])

    def __eq__(self, other):
        """
        Returns True iff all values stored in self are stored in other 
        in the same order
        """

        if self is other:
            return True

        if self.head is None and other.head is None:
            return True

        current = self.head
        current2 = other.head
        while current is not None:
            if current2 is None:
                return False

            if current2.value != current.value:
                return False

            current = current.next
            current2 = current2.next

        return current2 is None


    def __iter__(self):
        self.current = self.head
        return self
    
    def __next__(self):
        if self.current is not None:
            val =  self.current.value
            self.current = self.current.next
            return val
        else:
            raise StopIteration

def union(llist_1, llist_2):
    """
    Return a LinkedList that contains the content of llist_1 and then
    the contents of llist_2
    """
    result = llist_1.copy()

    result.append(llist_2.copy().head)

    return result

def intersection(llist_1, llist_2):
    """
    Returns a LinkedList with all unique elements of llist_1 that are
    also present in llist_2
    """
    result = LinkedList()

    for i in llist_1:
        if i in llist_2 and i not in result:
            result.append(i)

    return result

def test_union_and_intersection():
    test_cases = (  
    # Test Case 1: 
    [3,2,4,35,6,65,6,4,3,21], [6,32,4,9,6,1,11,21,1],         # (input_for_list1, input_for_list2,
    [3,2,4,35,6,65,6,4,3,21,6,32,4,9,6,1,11,21,1], [4, 6, 21] # union_solution, intersection_sol)
    ),(
    # Test Case 2:
    [3,2,4,35,6,65,6,4,3,23], [1,7,8,9,11,21,1], # (input_for_list1, input_for_list2,
    [3,2,4,35,6,65,6,4,3,23,1,7,8,9,11,21,1], [] # union_solution, intersection_sol)
    ),(
    # Test Case 3:
    [],[], # (input_for_list1, input_for_list2,
    [],[]  # union_solution, intersection_sol)
    ),(
    # Test Case 4:
    None,None, # (input_for_list1, input_for_list2,
    [],[]  # union_solution, intersection_sol)
    )

    for case in test_cases:
        linked_list_1 = LinkedList(case[0])
        linked_list_2 = LinkedList(case[1])

        assert (union(linked_list_1,linked_list_2) == LinkedList(case[2]))
        assert (intersection(linked_list_1,linked_list_2) == LinkedList(case[3]))

if __name__ == "__main__":
    test_union_and_intersection()