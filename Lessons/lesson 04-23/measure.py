import merge
import quick

import random
import time
import sys

sys.setrecursionlimit(99999999)

arr = random.sample(range(10000000), 10000)
arr_q = arr.copy()
arr_s = arr.copy()

start = time.time()
arr.sort()
print(time.time() - start)

start = time.time()
merge.merge_sort(arr)
print(time.time() - start)

start = time.time()
quick.quick_sort(arr_q, 0, len(arr_q)-1)
print(time.time() - start)