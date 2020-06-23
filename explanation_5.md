checkValidity() tests that no block's data has been manipulated, since Blocks are supposed to be immutable

appendBlock() operates in O(1) and checkValidity() operates in O(n)

BlockChain is O(n) in space complexity. Block::hash(self) is O(1) since the hash size does not depend on the size of the data. BlockChain::checkValidity(self) is O(1) since only one variable is stored

The hash of the data is not stored to lower space complexity, and instead is recomputed every time, since hash functions are fast. 
Additionally, having hash not depend on Block.data defeats the purpose of being able of detect change in a block of a block chain by comparing hashes.
