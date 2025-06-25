import copy

name = 'John'

if name in ['John', 'Rick']:
    print('Your name is either John or Rick.')

age = 24
if age > 18:
    print("You are an adult")
elif age > 12:
    print("You are a teenager")
else:
    print("You are a child")

x = [1, 2, 3]
y = [1, 2, 3]

# unlike the == operator, the is operator checks whether both variables point to the same object, not just have the same value.
print(x == y)
# check if the objects are the same, not just the values
print(x is y) # False
print(x is x) # True
print(y is not y) # True

z = x
print(z is x) # True

w = copy.deepcopy(x)
print(w is x) # False