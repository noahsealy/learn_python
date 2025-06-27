# A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.

# Firstly, a Nested Function is a function defined inside another function

# It's very important to note that the nested functions can access the variables of the enclosing scope. 
# However, at least in python, they are only readonly
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)

    data_transmitter()

print(transmit_to_space("Test message"))
# output: Text message

# However, one can use the "nonlocal" keyword explicitly with these variables in order to modify them.
def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)

print_msg(9)
# the output is 3 3. BUT without the nonlocal, it would be 3 9

# you can return the function object rather than calling the nested function within
def transmit_to_space(message):
  "This is the enclosing function"
  def data_transmitter():
      "The nested function"
      print(message)
  return data_transmitter

fun2 = transmit_to_space("Burn the Sun!")
fun2()

# Even though the execution of the "transmit_to_space()" was completed, the message was rather preserved. 
# This technique by which the data is attached to some code even after end of those other original functions 
#   is called as closures in python

# Advantage: Closures can avoid use of global variables and provides some form of data hiding.

# example, can generalize to have functions of multiply_with_x
def multiplier_of(_with):
    def multiplier(number):
        return number*_with
    return multiplier

multiply_with_5 = multiplier_of(5)
print(multiply_with_5(9))

