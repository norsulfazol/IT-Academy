x = int(input("Input your value: \n"))

# if x>0:
#     print("positive")
# elif x==0:
#     print("zero")
# else:
#     print("negative")

# if x>=0:
#     if x==0:
#         print("zero")
#     else:
#         print("positive")
# else:
#     print("negative")

# y = True if x>0 else False
# print(y)

print("positive") if x>0 else print("zero") if x==0 else print("negative")