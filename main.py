from core.block import ByteBlock
from database import get_block
from core.chain import Chain
from database import db
from core.wallet import Wallet


caleb = Wallet("Caleb Kutz")
jane = Wallet("Jane Doe")

caleb.send(caleb, jane, 10)

tx = db.get(caleb.public_k)
print(tx)