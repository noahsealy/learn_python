# map(function, *iterables)

# Where func is the function on which each element in iterables (as many as they are) would be applied on.
# The number of arguments to func must be the number of iterables listed.

# returns a generator
# To get the result as a list, the built-in list() function can be called on the map object. i.e. list(map(func, *iterables))

# ex, upper case all elements in the list
my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)