# while True:
#     print("I'm working...")

# counter = 0
# while counter<5:
#     if counter == 2:
#         break
#     print(counter)
#     print("I'm working...")
#     counter += 1
# else:
#     print("else is here")

# counter = 0
# while True:
#     counter += 1
#     if counter == 2:
#         print("it's 2")
#         continue
#     print(counter)
#     print("I'm working...")
#     if counter == 11:
#         break

l = [8,4,9,0.1]
# for test in l:
#     if test == 3:
#         continue
#     test += 2
#     print(test)
# else:
#     print("else is here")

# x = 0
# while x<len(l):
#     print(l[x])
#     x += 1

# for i, elem in enumerate(l):
#     print(elem, i)

# for i in range(1, 11, 2):
#     print(i)

d = { 1: "one", 2: "two"}
for k in d.items():
    print(k)