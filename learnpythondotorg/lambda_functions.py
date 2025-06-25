# instead of defining a function, we can just make these anonymous functions
# useful, quick, throwaway functions
a = 1
b = 2
sum = lambda x,y : x + y
c = sum(a,b)
print(c)

# lambda arguments: expression

def square(x):
    return x * x

square = lambda x: x * x