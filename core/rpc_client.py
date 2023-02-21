from jsonrpcclient import request
import requests

rpc_create_json = request("create_tx")
rpc_read_json = request("read_chain")

rpc_c_response = requests.post("http://localhost:5000", json=rpc_create_json)
rpc_r_response = requests.post("http://localhost:5000", json=rpc_read_json)

print(rpc_c_response.json())
print(rpc_r_response.json())