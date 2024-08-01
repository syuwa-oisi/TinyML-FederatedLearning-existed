import json


file_path = "/Users/odayuki/Documents/TinyML-FederatedLearning-existed/datasets/colors/blau.2im6rk8r.ingestion-65c5587588-dvjvm.json"

with open(file_path, "r") as file:
    content = json.load(file)
    print(content)
    tmp = content['payload']["values"]
    print(max(tmp),min(tmp))