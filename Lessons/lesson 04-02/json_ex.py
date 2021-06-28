import json

x = {"test": (22,33,44)}
obj = {"key": [1,2.3, True, "test", x]}
# json_obj = json.dumps(obj)
# print(type(json_obj))
# print(json_obj)

# new_obj = json.loads(json_obj)
# print(type(new_obj))
# print(new_obj)

with open("test.json", "w") as f:
    json.dump(obj, f)

with open("test.json", "r") as f:
    print(json.load(f))