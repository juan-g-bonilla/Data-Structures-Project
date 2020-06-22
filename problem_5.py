import hashlib
import datetime

class Block(object):

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.next = None

    def hash(self):
      sha = hashlib.sha256()

      hash_str = ("" if self.data is None else self.data).encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

class BlockChain(object):

    def __init__(self):
        self.genesis = None
        self.tail = None

    def appendBlock(self, data):
        """
        Appends a block to the end of the BlockChain
        """
        if self.genesis is None:
            self.genesis = Block(datetime.datetime.utcnow(), data, None)
            self.tail = self.genesis
            return
        
        self.tail.next = Block(datetime.datetime.utcnow(), data, self.tail.hash())
        self.tail = self.tail.next

    def checkValidity(self):
        """
        Returns true iff the data has not been tampered for any of the blocks
        """
        current = self.genesis
        while current is not None and current is not self.tail:
            if current.hash() != current.next.previous_hash:
                return False
            current = current.next 

        return True

def test_block_chain():
    chain = BlockChain()

    assert(chain.checkValidity())

    chain.appendBlock("Hello")
    chain.appendBlock("My name is Iñigo Montoya")
    chain.appendBlock("You killed my father")
    chain.appendBlock("Prepare to die")
    chain.appendBlock(None)
    chain.appendBlock("")

    assert(chain.genesis.next.next.data == "You killed my father")
    assert(chain.checkValidity())

    chain.genesis.next.data = "My name is Domingo Montoya"
    assert(not chain.checkValidity())

    chain.genesis.next.data = "My name is Iñigo Montoya"
    assert(chain.checkValidity())


if __name__ == "__main__":
    test_block_chain()