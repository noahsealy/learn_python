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