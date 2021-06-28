import measurement as m
import phone_book as pb

# x = "not test"

# print(m.y)
# print(m.x)
# print(m.__name__)

# m.start()

# for i in range(100000000):
#     i+1

# result = m.finish()
# print(result)


first, last, phone = input("First name:\n"), input("Last name:\n"), input("Phone:\n")
pb.add(first, last, phone)
print(pb.get_book())
print(pb.find("test"))
print(pb.find("890"))
pb.delete(first, last, phone)
print(pb.get_book())
