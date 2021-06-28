# def correct_mult(x, y):
#     res = 0

#     flag = True
#     if y < 0:
#         y = -y
#         flag = False

#     for i in range(y):
#         res += x

#     if not flag:
#         res = -res

#     return res

# m = correct_mult(-2, -3)
# print(m)

def correct_mult(x, y):
    res = 0

    if y < 0:
        y = -y
        x = -x

    for i in range(y):
        res += x

    return res

m = correct_mult(-2, -3)
print(m)