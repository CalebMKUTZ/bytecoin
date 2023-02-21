from jsonrpcclient import request
import requests

rpc_json = request("create_tx")

response = requests.post("http://localhost:5000", json=rpc_json)
print(response.json())