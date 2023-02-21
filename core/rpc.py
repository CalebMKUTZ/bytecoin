import http.client

from jsonrpcserver import method, Success, dispatch, serve
from transaction import Transaction
from wallet import Wallet
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
from chain import Chain

# TODO: create a gui that allows users to create wallets, for now leave it hard-coded
ex_sender = Wallet("Caleb")
ex_recipient = Wallet("Jane")
amount = 100

c = Chain()


@method
def create_tx():
    tx = Transaction(ex_sender, ex_recipient, amount)
    block = tx.create_tx_block()
    tx.sign(ex_recipient.private_k)
    tx_json = tx.to_json()
    c.add_block(block)
    c.save()
    return Success(tx_json)


@method
def read_chain():
    return Success(c.to_json())


try:
    print("[RPC] rpc server listening on localhost:5000")
    serve()
except http.client.error as e:
    print(e)
