# tuple unpacking with *
def add(x, y):
    return x + y

args = (3, 5)
print(add(*args))  # Output: 8

# dict unpacking with **
def describe(name, age):
    print(f"{name} is {age} years old.")

kwargs = {'name': 'Alice', 'age': 30}
describe(**kwargs)

# or pack them back up! 
        # sidenote:
        # (using lambda (anonymous) functions)... 
        # Church used lambda to denote throwaway functions in Lambda calculus 
        # ex, λx. x + 1
pack_tuple = lambda *args:args
packed_tuple = pack_tuple('Noah', 'Sealy')
print(packed_tuple)

pack = lambda **kwargs: kwargs
packed_dict = pack(first_name = 'Noah', last_name = 'Sealy')
print(packed_dict)

args = (3, 4)
print(*args) #unpack
print(args)


# if you pass in a tuple to *, it will unpack it
# if you pass in variables to a function with *, it will pack them