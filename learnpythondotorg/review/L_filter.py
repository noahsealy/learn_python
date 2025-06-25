# filter(), first of all, requires the function to return boolean values (true or false) 
#   and then passes each element in the iterable through the function, "filtering" away those that are false

# filter(func, iterable)

# only one iterable is required
# func is required to return a boolean type. If it doesn't, filter simply returns the iterable passed to it.
# func can only take one argument (only one iterable)
# filter passes each element in the iterable through func and returns only the ones that evaluate to true

# example, filter out all ints under 75
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
def over(score):
    return score > 75
over_75 = list(filter(over, scores))
print(over_75)

# palindrome detector
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
palindromes = list(filter(lambda word: word == word[::-1], dromes))
print(palindromes)