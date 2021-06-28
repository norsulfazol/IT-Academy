import random

x = 1010
y = 101
print(x, 1)

def func():
    #print(1)
    #global x, y
    y = 8
    x = random.randint(0,10)
    print(x, "func")
    def inner_func():
        #global x
        nonlocal x
        print(x, "inner_func")
        x = "test"
        print(x, "inner_func")
        def inner_inner_func():
            nonlocal x
            print(x, "inner_inner_func")
        inner_inner_func()
    inner_func()
    print(x, "func")

# def func2():
#     x = 3.0
#     print(x, "func2")

print(x, 2)

func()

print(x, 3)