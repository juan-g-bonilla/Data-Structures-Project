We define union as the concatenation of lists in a new list, with no care taken for repeated elements.
We define intersection as the set of unique elements that are present in both lists.

In LinkedList: append() takes O(n) since we do not store a reference to the tail, copy() takes O(n) and __eq__ takes O(n). LinkedList is O(n) in space complexity

union(list1, list2) takes O(n) where n is the number of elements in list1 and list2. The space complexity is O(n) since all elements are stored in a new LinkedList.

intersection(list1, list2) takes O(n) where n is the number of elements in list1 and list2. The space complexity is O(n) since all elements from the LinkedLists are stored in new sets.
Even though it's costlier space-wise, creating sets from the linked lists allows obtaining O(n). If we had iterated through
every item in one list and checked on the other it would have O(n^2) complexity. By using sets, we take advantage of sets' O(1) contains function.
