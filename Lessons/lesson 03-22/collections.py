x = [[1,2,3], [4,5,6], [7,8,9]]
print(x)
print(x[0])
print(x[1])
print(x[2])

print(x[1][1])

x = [[1,2,3], [4,5], [7,8,9]]
print(x[0])
print(x[1])
print(x[2])

t = (x, 55)
print(t)
t[0][0][0] = 0
print(t)
x[2][2] = 10
print(t)
print(x)
#t[0] = "test" - error

d = {(3, 6): "test"}
print(d)
#d[t] = 0 - error

print({(3, 6): "test"} == {(3, 6): "test1"})