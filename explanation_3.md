The SortedQueue is implemented using a binary heap. This is done to allow enqueue and dequeue operations to take O(log(n)) time. The SortedQueue is itself implemented using a python list, since it has a lower space complexity than trees that use Nodes.

create_huffman() operates in O(n) time. That is okay since it is only run once per encode/decode

get_huffman_codes() operates in O(n) time, and returns a dictionary that stores the Huffman code of each character.

huffman_encoding() operates in O(n) where n is number of characters in data. Although initially creating a dictionary code->character from the Huffman tree takes O(k) time where k is the number of unique characters, it allows looking up the corresponding character in O(1) time instead of O(log(k)).
Assuming n >> k, it is worth it to spend resources on creating the dictionary. Otherwise the function would operate in O(n*log(k)) time.
