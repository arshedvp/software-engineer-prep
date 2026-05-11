import json

employee={
    "name":"Arshed",
    "role":"ASE",
    "skills":["Python","Linux","Git"]
}

json_data=json.dumps(employee)

print(json_data)
print(type(json_data))

dictio=json.loads(json_data)
print(dictio)
print(type(dictio))