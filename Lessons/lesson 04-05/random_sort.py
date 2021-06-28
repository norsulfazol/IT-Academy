import random

def is_sorted(l):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            return False
    
    return True
    # if l == sorted(l):
    #     return True
    # return False

def swap(l, x, y):
    l[x], l[y] = l[y], l[x]

def get_rand_index(x):
    return random.randint(0,x-1)

    

l = [3,1,2,8]


counter = 0

while True:
    if is_sorted(l):
        print(l)
        print(counter)
        break

    x = get_rand_index(len(l))
    y = get_rand_index(len(l))
    while x == y:
        y = get_rand_index(len(l))

    swap(l, x, y)
    counter += 1