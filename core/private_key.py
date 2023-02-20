import hashlib
import base64
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256


class PrivateKey:
    def __init__(self):
        self._key = RSA.generate(2048)

    def sign(self, message):
        message_hash = SHA256.new()
        message_hash.update(message)
        signer = pkcs1_15.new(self._key)
        signature = signer.sign(message_hash)
        return base64.b64encode(signature).decode('utf-8')

    def get_public_key(self):
        return self._key.publickey().export_key().decode('utf-8')