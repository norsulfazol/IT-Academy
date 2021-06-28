# l = [10]
# try:
#     if len(l) == 0:
#         raise IndexError
#     l[0]
#     x = open("")
#     # try:
#     #     l[0]
#     # except IndexError:
#     #     print("raise new IndexError")
#     #     raise Exception
# except IndexError:
#     l.append(0)
#     print("index was out of range, but show must go on, so it was added")
# except Exception:
#     print("something went wrong")
#     l = []
# finally:
#     x.close()
#     print("hello from finally")
# print(l)

# try:
#     f = open("text.txt", "w")
#     x + 1
# finally:
#     x + 1
#     f.close()
#     print("heh")

assert False, "something went wrong"

if not True:
    raise AssertionError("something went wrong")