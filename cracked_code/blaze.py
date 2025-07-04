from timeit import Timer
from numpy import random

# built in functions
def sort(nums):
    return sorted(nums)

nums = random.randint(100, size=(10000))
print(nums)
y = Timer("sort(nums)", "from __main__ import sort, nums")
print('Sorted timer: %f', y.timeit(number = 10))