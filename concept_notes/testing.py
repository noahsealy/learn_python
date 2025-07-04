import copy
a = [1, 2, 3]
b = a
c = [1, 2, 3]
d = copy.copy(a)
print(a is b) # True
print(a is c) # False
print(a is d) # False

a = 1
b = 1
print(a is b) # True

a = 1000000000
b = 1000000000
print(a is b) # True ???