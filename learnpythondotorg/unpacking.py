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
pack_tuple = lambda *args:args
packed_tuple = pack_tuple('Noah', 'Sealy')
print(packed_tuple)

pack = lambda **kwargs: kwargs
packed_dict = pack(first_name = 'Noah', last_name = 'Sealy')
print(packed_dict)
