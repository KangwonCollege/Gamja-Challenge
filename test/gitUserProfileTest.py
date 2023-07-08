import requests
import datetime
import json
import dataclasses

with open(r"config\token.txt", "r") as f:
    token = f.read()

with open("test\q.graphql", "r") as f:
    q = f.read()
    

header = { "Authorization" : f"Bearer {token}"}
with open("test\data.json", "r") as f:
    variable = json.load(f)
    

result = requests.post("https://api.github.com/graphql", headers=header , json = {"query" : q, "variables" : variable})

print(result.json())