def r(x, g, i=0):
    print(g(x[i]))
    if (i == len(x)-1):
        return
    i += 1
    r(x, g, i)

def my_func(x):
    print(f"my current value is {x}")

def factor(x):
    if x==1:
        return 1
    return x*factor(x-1)

x = [1,2,3,4,5]
r(x, factor)