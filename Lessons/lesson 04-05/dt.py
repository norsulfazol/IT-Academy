def times(x, y):
    # if isinstance(y, str):
    #     return
    # if isinstance(y, str):
    #     return x*len(y)
    return x*y

print(times(3,4))
print(times(3, 4.0))
print(times(3, "test"))
print(times({}, "test"))