# map(function, *iterables)

# Where func is the function on which each element in iterables (as many as they are) would be applied on.
# The number of arguments to func must be the number of ITERABLES listed.
# so, if you need a value for each parameter
# So, if the function you're passing requires two, or three, or n arguments, then you need to pass in two, 
#   three or n iterables to it.

# returns a generator
# To get the result as a list, the built-in list() function can be called on the map object. i.e. list(map(func, *iterables))

# ex, upper case all elements in the list
my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = list(map(str.upper, my_pets))
print(uppered_pets)

# round the first element to one place, the second to two, etc...
# note how we have multiple parameters here, but 
#   len(iterables) = len(params), and each iterable comes with a corresponding value
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, circle_areas, range(1, 7)))
print(result)

# if an iterable does not have enough value, it will only run as far as the shortest iterable, without error
# it will simply iterate over the elements until it can't find a second argument to the function, 
#   at which point it simply stops and returns the result.

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, circle_areas, range(1, 3)))
print(result)

# The zip() function is a function that takes a number of iterables and 
#   then creates a tuple containing each of the elements in the iterables.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]
results = list(zip(my_strings, my_numbers))
print(results)

# custom zip function!
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]
results = list(map(lambda x, y: (x, y), my_strings, my_numbers))
print(results)