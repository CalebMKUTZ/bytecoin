import hashlib
import json
from .block import ByteBlock


class Chain:
    def __init__(self):
        self.chain = [self.genesis()]

    def add_block(self, block):
        self.chain.append(block)
    
    def to_json(self):
        chain_object = {
            "chain": str(self.chain[len(self.chain) - 1].to_json())
        }
        chain_json = json.dumps(chain_object, indent=2)
        return chain_json
    
    def genesis(self):
        genesis = ByteBlock("GENESIS", ["xxxxxxx"])
        return genesis