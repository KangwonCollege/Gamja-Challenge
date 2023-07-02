import requests
import datetime
import json


with open("test\q.graphql", "r") as f:
    q = f.read()

header = { "Authorization" : "Bearer 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"}
with open("test\data.json", "r") as f:
    variable = json.load(f)

result = requests.post("https://api.github.com/graphql", headers=header , json={"query" : q, "variables" : variable})

print(result.json())