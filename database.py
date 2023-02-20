import pickledb


db = pickledb.load("./tmp/bytecoin-store.db", False)


def get_block(hash):
    return db.get(hash)


def get_wallet(public_key):
    db.get(public_key)