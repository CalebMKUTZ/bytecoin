import hashlib
from datetime import datetime
import json
from .block import ByteBlock
from .chain import Chain


chain = Chain()


class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.inputs = []
        self.outputs = []
        self.timestamp = datetime.now()
        self.signature = None
    
    def add_input(self, tx_output):
        self.inputs.append(tx_output)

    def add_output(self, recipient, amount):
        self.outputs.append({"recipient": recipient.name, "amount": amount})

    def get_output(self, recipient, amount):
        return {"recipient": recipient.name, "amount": amount}

    def to_json(self):
        tx_object = {
            'sender': self.sender.name,
            'recipient': self.recipient.name,
            'amount': self.amount,
            'inputs': self.inputs,
            'outputs': self.outputs,
            'timestamp': str(self.timestamp),
            'signature': self.signature
        }
        return json.dumps(tx_object, indent=2)
    
    def tx_hash(self):
        return hashlib.sha256(self.to_json().encode()).hexdigest()
    
    def sign(self, private_key):
        message = self.to_json().encode()
        self.signature = private_key.sign(message)

    # def is_valid(self):
    #     input_total = sum(input_transaction["amount"] for input_transaction in self.inputs)
    #     output_total = sum(output['amount'] for output in self.outputs)
    #     return input_total == output_total

    def create_tx_block(self):
        previous = chain.chain[-1]
        new = ByteBlock(previous.hash.hexdigest(), [self.to_json()])
        new_json = new.to_json()
        new.run_proof()
        print(new_json)