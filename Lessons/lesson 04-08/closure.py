def maker(n):
    def action(x):
        #print(n)
        return x**n
    return action

def func():
    print("test")

# f = maker(2)
# print(f(3))
# print(maker(2)(4))

# t = func
# t()

# func = "new test"
# print(func)
# t()

def get_value_or_default(t):
    def get_value(l, i):
        if i > len(l)-1:
            return t
        else:
            return l[i]
    return get_value

num = get_value_or_default(0)
string = get_value_or_default("_")

n_l = [1,2,3]
s_l = ["a", "b", "c"]
print(num(n_l, 1))
print(num(n_l, 101))

print(string(s_l, 1))
print(string(s_l, 101))