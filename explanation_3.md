The SortedQueue is implemented using a binary heap. This is done to allow enqueue and dequeue operations to take O(log(n)) time. The space complexity of SortedQueue is O(n) since all values are stored in an array. The SortedQueue is itself implemented using a python list, since it has a lower space requirements than trees that use Nodes since no pointers must be stored.

create_huffman() operates in O(n) time. Space complexity is O(n) since the elements in the queue are stored in a tree. That is okay since it is only run once per encode/decode.

get_huffman_codes() operates in O(n) time, and returns a dictionary that stores the Huffman code of each character. Space complexity is O(n) since each leaf in the tree is stored in a dictionary.

huffman_encoding() operates in O(n) where n is number of characters in data. The space complexity is linear O(n), since the size of SortedQueue, dictionary and string grows linearly with the size of the input. Although initially creating a dictionary code->character from the Huffman tree takes O(k) time where k is the number of unique characters, it allows looking up the corresponding character in O(1) time instead of O(log(k)).
Assuming n >> k, it is worth it to spend resources on creating the dictionary. Otherwise the function would operate in O(n*log(k)) time.

Similarly, huffman_decoding() is O(n) in time complexity and space complexity