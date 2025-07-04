# built in functions
# https://www.youtube.com/watch?v=YsOYMrBNGq8
from timeit import Timer
from numpy import random

# 1
# faster because they're written in C!
def sort(nums):
    return sorted(nums)

nums = random.randint(100, size=(10000))
print(nums)
y = Timer("sort(nums)", "from __main__ import sort, nums")
print('Sorted timer: %f', y.timeit(number = 10))

# 2
# using a yield can save a lot of time and memory while unpacking large datasets
def parse_csv(file_name):
    for row in open(file_name, 'r'):
        yield row

def test_parse_csv():
    csv_file = 'test.csv'
    row_count = 0
    for row in parse_csv(csv_file):
        row_count += 1
        # process data!
    return row_count

# 3
# concurrency!
import multiprocessing

# 4
# compile code with CPython

# 5
# use compiled frameworks, like numpy, pandas, and pillow