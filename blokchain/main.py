import hashlib

def hash_function(data):
    sha256 = hashlib.sha256()
    sha256.update(str(data).encode("utf-8"))
    return sha256.hexdigest()


class Block:
    def __init__(self,data,previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = hash_function(str(self.timestamp) + str(self.data) + str(self.previous_hash))
  
  
class BlockChain:
    def __init__(self):
        self.chain = [Block("Genesis Block", "0")]
        
    def add_block(self, data):
        self.chain.append(Block(data,self.chain[data, self.chain[-1].hash]))
        

blockChain = BlockChain()


blockChain.add_block("Block 1")
blockChain.add_block("Block 2")
blockChain.add_block("Block 3")

for block in blockChain.chain:
    print("Data : " , block.data)
    print("Hash:  ", block.hash)
    print("")