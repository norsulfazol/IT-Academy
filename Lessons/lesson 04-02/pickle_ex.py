import pickle

x = {"test": (22,33,44)}
obj = {"key": [1,2.3, True, "test", x]}
# pickle_obj = pickle.dumps(obj)
# print(type(pickle_obj))
# print(pickle_obj)

# new_obj = pickle.loads(pickle_obj)
# print(type(new_obj))
# print(new_obj)

with open("pickle_file.txt", "wb") as f:
    pickle.dump(obj, f)

with open("pickle_file.txt", "rb") as f:
    print(pickle.load(f))