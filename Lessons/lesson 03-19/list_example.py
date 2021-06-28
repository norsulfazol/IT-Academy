import random

l = []
print(l, type(l))

l = [10]
print(l, id(l))

l[0] = 5
print(l, id(l))

l = [0, "test", 12.5, 2, 3, 4, 5, 6, 7, 8]
print(l[0], l[1], l[2])
print(l[-1])

print(l[0:4])
print(l[0:6:2])
print(l[6:0:-2])
print(l[::-1])
print(l)

l[0] = l[1]
print(l)

l[0:4] = [1.2, "test"]
print(l)

m = [1,2,3.5, 0]
print(l+m)

print(l*3)

print(l.index("test"))
print((l*3).index("test"))

l=l+[0]
print(l)

l.append(0)
print(l)

l.insert(0, "new elem")
print(l)

y = l.pop()
print(y)
print(l)

l2 = l*2
l2.remove("test")
print(l2)
print(l2.count("test"))

del l[0]
print(l)

# l.clear()
# print(l)

# del l
# print(l)

random.shuffle(m)
print(m)

m.sort()
print(m)


random.shuffle(m)
print(m)

print(sorted(m))
print(m)