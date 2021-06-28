x = {1, "test", False, "jhgdchgkjdkjfjf"}
print(x)
print(type(x))

x = set([False,1,1,2,3,4])
print(x)

#set([1,2,[3,4]]) - error

x.add("test")
print(x)

x.add(0)
print(x)

x.update([2,3,4.5], {6, 8.8})
print(x)

# x = set()
# print(type(x))

# print(x.pop())
# print(x)

# print(x.pop())
# print(x)

x.remove(1)
print(x)

x.discard(False)
print(x)

x.discard(False)

x = {1, 3, "test"}
y = {"test", 5.5, 8}

print(x)
print(y)
z = x.union(y)
print(x)
print(y)
print(z)
#print(x.union(y))
print(x.intersection(y))
print(x.symmetric_difference(y))

x = {1}
y = {1,3}
print(x.issubset(y))
print(y.issuperset(x))

s = "aaasssdddrr"
x = set(s)
print(str(x))