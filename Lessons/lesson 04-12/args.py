# def f(y, x=0):
#     x = x + 1
#     print(x)

# x = 5
# f(x=10, y=x)
# print(x)

# def f(a, b, c, *args):
#     print(type(args))
#     print(args)
#     for i in args:
#         print(i)

# x = [1,2,3,4,5]
# f(1,2,3,4,5,6,7,8,9,"test",*x)
# print(x)

# def f(**kwargs):
#     print(type(kwargs))
#     for k,v in kwargs.items():
#         print(k,v)

# x = {"1":"test"}
# f(**x)
# f(a = 1, b = "test", **x)


def f(x, y, *args, **kwargs):
    print(x, y)

    print(args)

    print(kwargs)

#f(1,2,3,4,5,6,7,8,a=6,b=4,**{"1":1})