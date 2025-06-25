from functools import partial

def polynomial(u, v, w, x):
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function

first_deg_input = partial(polynomial, 4, 4, 4)
y = first_deg_input(4)
print(y)