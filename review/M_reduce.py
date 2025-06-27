# reduce applies a function of two arguments cumulatively to the elements of an iterable, 
#   optionally starting with an initial argument.

# reduce(func, iterable[, initial])

# Where func is the function on which each element in the iterable gets cumulatively applied to, 
#   and initial is the optional value that gets placed before the elements of the iterable in the calculation,

from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)
print(result)

# there is an optional third parameter
# The result is 78 because reduce, initially, uses 10 as the first argument to custom_sum.
from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers, 10)
print(result)