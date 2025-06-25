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

### COPIED FROM foo_bar_multiple_args.py ###
# * (1 star) means the arguments are collected into a tuple
# ** (2 star) (keyword arguments) (**kwargs) are collected into a dictionary
def foo(a, b, c, *args):
    return len(args)

def bar(a, b, c, **kwargs):
    # no null check, as if we use .get, it won't error, we will just get None
    return kwargs.get('magicnumber') == 7

if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")



# PRACTICE
args_packer = lambda *args: args
packed = args_packer('Noah', 'Sealy', 'software')
print(packed)

kwargs_packer = lambda **kwargs: kwargs
packed = kwargs_packer(first_name= 'Noah', last_name= 'Sealy')
print(packed)