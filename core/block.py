import hashlib
from datetime import datetime
import sys
import json
from database import db
from utils.screen import CLEAR, CLEAR_RETURN
import time


class ByteBlock:
    def __init__(self, previous_hash, transactions):
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.n_transactions = len(self.transactions)
        self.time = datetime.now()
        self.hash = hashlib.sha256()
        self.height = 0
        self.nonce = 0
        self.merkle_root = self.generate_merkle(self.transactions)
        self.size = sys.getsizeof(self)
        self.difficulty = 5
        self.difficulty_target = 2 ** (256 - self.difficulty)
        self.max_nonce = 2 ** 32
        self.increment_difficulty_over_time()

    def run_proof(self):
        print(CLEAR)
        for _ in range(self.max_nonce):
            if int(self.hash.hexdigest(), 16) <= self.difficulty_target:
                db.set(self.hash.hexdigest(), self.to_json())
                db.dump()
                break
            else:
                self.nonce += 1
                time.sleep(0.01)
                self.hash = self.calc_sha256()
                print(CLEAR_RETURN)
                print(self.hash.hexdigest())

        self.height += 1
    
    def generate_merkle(self, transactions):
        if len(transactions) == 0:
            return hashlib.sha256(b"").hexdigest()
        
        if len(transactions) == 1:
            return hashlib.sha256(hashlib.sha256(transactions[0].encode()).hexdigest().encode()).hexdigest()
        
        left = self.generate_merkle(transactions[:len(transactions) // 2])
        right = self.generate_merkle(transactions[len(transactions) // 2])
        
        return hashlib.sha256(hashlib.sha256(left.encode() + right.encode()).hexdigest().encode()).hexdigest()
    
    def calc_sha256(self):
        block_data = {
            "time": str(self.time),
            "height": self.height,
            "nonce": self.nonce,
            "transactions": self.n_transactions,
            "previous": self.previous_hash,
            "hash": self.hash.hexdigest(),
            "merkle_root": self.merkle_root,
            "size": self.size,
            "difficulty_target": self.difficulty_target,
            "difficulty": self.difficulty,
            "max_nonce": self.max_nonce
        }
        block_string = json.dumps(block_data, indent=2)
        self.hash.update(block_string.encode())
        return self.hash
        
    def to_json(self):
        block_data = {
            "time": str(self.time),
            "height": self.height,
            "nonce": self.nonce,
            "transactions": self.n_transactions,
            "previous": self.previous_hash,
            "hash": self.hash.hexdigest(),
            "merkle_root": self.merkle_root,
            "size": self.size,
            "difficulty_target": self.difficulty_target,
            "difficulty": self.difficulty,
            "max_nonce": self.max_nonce
        }
        block_string = json.dumps(block_data, indent=2)
        return block_string

    def increment_difficulty_over_time(self):
        n_seconds = 0.0001
        block_time = self.max_nonce / n_seconds
        time_diff = (self.time - datetime.now()).total_seconds()

        if time_diff >= block_time:
            # Increment the difficulty if the block time is too long
            self.difficulty += 1
        elif self.difficulty > 1 and time_diff <= block_time / 2:
            # Decrease the difficulty if the block time is too short
            self.difficulty -= 1
    
    