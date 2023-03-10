import json

from private_key import PrivateKey
from transaction import Transaction
from database import db


class Wallet:
    def __init__(self, name):
        self.name = name
        self.private_k = PrivateKey()
        self.public_k = self.private_k.get_public_key()
        self.balance = 100  # TODO: implement the balance
        db.set(self.public_k, str(self.balance))

    def send(self, sender, recipient, amount):
        t = Transaction(sender, recipient, amount)
        t.add_input(t.get_output(recipient, amount))
        recipient.private_k.sign(bytes(f"{sender} sent {recipient} {amount} BYC".encode()))
        t.sign(recipient.private_k)
        t.create_tx_block()
        t_json = t.to_json()
        print("transaction complete ✓")
        print(t_json)

    def to_json(self):
        wallet_object = {
            "name": self.name,
            "public_key": self.public_k,
            "balance": self.balance
        }
        wallet_json = json.dumps(wallet_object, indent=2)
        return wallet_json
