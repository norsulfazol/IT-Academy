t = ()
print(t)
print(type(t))

t = (1, "test", 2.5)
print(t)

print(t[0], t[1], t[2])

l = [1]
t = (1)
print(t)
print(type(t))

t = (1,)
print(t)
print(type(t))

t=(1, 2, "test", 42.42)
print(t[0:2])

print((1,) + ("test",))
print((1,) * 1)

#t[0] = 5 => error

t = list(t)
t[0] = 5
print(t)

t = tuple(t)
print(t)