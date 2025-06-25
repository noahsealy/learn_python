# Decorators allow you to make simple modifications to callable objects like functions, methods, or classes
# a function that extends the behaviour of another function, without modifying the base function
# you simply pass the base function as an argument to the decorator function

# ex, you have get_ice_cream, but some people might want sprinkles
# not everyone will want sprinkles tho, so we can use a decorator to accomodate for just those who want sprinkles
# @add_sprinkles
# get_ice_cream('vanilla')

# adding something to a base function, without changing that function

def decorator(function):
    def wrapper(*args, **kwargs):
        print('In the decorator, before the base function call.')
        function(*args, **kwargs)
        print('In the decorate, after the base function call.')
    return wrapper

def second_decorator(function):
    # need this function, so decorator doesn't get automatically called as soon as we declare it
    # the wrapper should take in *args and **kwards, to accept any number or type of parameter
    # otherwise, it errors out if the base function takes in any variables
    def wrapper(*args, **kwargs):
        print('In the second decorator, before the base function call.')
        # then we unpack the args and kwargs into the base function call
        function(*args, **kwargs)
        print('In the second decorator, after the base function call.')
    return wrapper

@decorator
@second_decorator
def base(parameter):
    print(parameter)
    print('In the base function.')

base('parameter')

# the decorator ONLY gets executed, when we call the base function