d = {0: "zero", "one":1, 2:"two"}
print(d)

print(d[0], d["one"], d[2])

print(d.items())
print(type(d.items()))
print(d.keys())
print(type(d.keys()))
print(d.values())
print(type(d.values()))

x = d.pop(0)
print(x)
print(d)

y = d.popitem()
print(y)
print(d)

d[(1,3,"test")] = 5
print(d)