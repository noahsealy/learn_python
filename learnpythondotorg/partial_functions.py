# Partial functions allow one to derive a function with x parameters to 
# a function with fewer parameters and fixed values set for the more limited function.

from functools import partial

def multiply(x, y):
        return x * y

# wrap the multiply function, so that x is always 2
# the default values will start replacing variables from the left
# so, x will be 2 and y will be the (now only) input of double
double = partial(multiply, 2)
# y = 4
print(double(4))