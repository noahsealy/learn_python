def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))

# The "therest" variable is a list of variables, 
# which receives all arguments which were given to the "foo" function after the first 3 arguments. 
foo(1, 2, 3, 4, 5)

# It is also possible to send functions arguments by keyword, 
# so that the order of the argument does not matter, using the following syntax.
def bar(first, second, third, **options):
    print('Result')
    print(options)
    # .get('action') is the same as options['actions'], 
    # BUT it does not throw an error if action does not exist
    # it just returns None
    # it's best to use that in cases like this, where there are optional parameters
    # and we just want to check them
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))

# more on .get() in dictionaries
# you can use setdefault to set the variable, if it is absent in the options
d = {'a': 1, 'b': 2}
val = d.setdefault('a', 100)
print(val)  # Output: 1
print(d)    # {'a': 1, 'b': 2}

# absent
d = {'b': 2}
val = d.setdefault('a', 100)
print(val)  # Output: 1
print(d)    # {'a': 100, 'b': 2}