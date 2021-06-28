import functools

g = lambda x: x+1

#the same thing
# def g(x):
#     return x + 1

def generate_lambda(parameter):
    if parameter:
        return lambda x: x+1
    else:
        return lambda x: x*x

def f(l, s):
    for el in l:
        print(s(el))

#f([1,2,3,4,5], lambda x: x+1)

#print(sorted(["Abc","abc","efg","Efg"], key=str.lower))

d = {"one":1, "two":2, "three":3}

def get_value(pair):
    return pair[1]

def check_for_3(x):
    if x==3:
        return True
    return False

#print(sorted(d.items(), key=lambda pair: pair[1]))

l = [0,1,2,3,4,5]
print(list(map(lambda x: x*10, l)))

print(list(filter(lambda x: x>3, l)))

print(functools.reduce(lambda x,y: x+y, l))

print(functools.reduce(lambda x,y: x if x>y else y, l))

t = lambda p: (lambda x: x+1) if p else (lambda y: y-1)
print(t(True))
print(t(False)(10))

l = ['1', '11', '33', '12', '22', '2', '13', '30']

sorted(filter(lambda x: int(x)*int(x) % 2 != 0, l), key=int)

list(filter(lambda x: int(x)*int(x) % 2 != 0, sorted(l, key=int)))