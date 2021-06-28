"""this is my program"""

x = "test"
y = 'test'
z = """test"""
print(id(x) == id(y) == id(z))

my_str = "my very long string!"
print(my_str[0])
print(type(my_str[0]))

print(my_str[int(len(my_str)/2)])

print(my_str[3:-3])

spl = my_str.split()
print(" ".join(spl))

print(my_str.upper())

print("my" in my_str)

print(my_str.find("y"))