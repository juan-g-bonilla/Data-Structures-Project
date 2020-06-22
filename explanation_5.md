checkValidity() tests that no block's data has been manipulated, since Blocks are supposed to be immutable

appendBlock() operates in O(1) and checkValidity() operates in O(n)

The hash of the data is not stored to lower space complexity, and instead is recomputed every time, since hash functions are fast. 
Additionally, having hash not depend on Block.data defeats the purpose of being able of detect change in a block of a block chain by comparing hashes.
