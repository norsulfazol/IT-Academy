# f = open("text_file.txt", "w")
# f.close()

x = "test"

# with open("text_file.txt", "w") as f:
    #f.write(f"some {x} new line\nanother new line")
    # f.write("another new line\n")
    # f.writelines(["some new line\n", "another new line\n"])

# with open("text_file.txt", "r") as f:
#     for l in f:
#         print(l)
    #x = f.readlines()
    #print(f.readline())
    #x = f.read(5)
    #f.seek(0)
    #x = f.read(5)

# print(x)
# for line in x:
#     print(line)

# with open("text_file.txt", "a") as f:
#     f.write("\nthis line was appended")

#with open("text_file.txt", "r+") as f:
    #f.write("not a test")
    # print(f.read())
    # f.write("\ntest")
    # f.seek(0)
    # for l in f:
    #     print(l)

# with open("text_file.txt", "a+") as f:
#     f.seek(0)
#     print(f.read())
#     f.write("\nthis line was appended")
#     f.seek(0)
#     print(f.read())

with open("text_file.txt", "w+") as f:
    f.write("completely new line")
    f.seek(0)
    print(f.read())