integer_var = 10
float_var = 10.0
string_var = "Hello, World!"
# double quotes allos for apostrophes
# double quotes allow for backslashes and unicode characters
# they also allow for interpolation of variables
# and multiline strings
# and carriage returns

# Example of a string with a carriage return
string_with_cr = "First line\rSecond line"
print("String with carriage return:", string_with_cr)

# Example of a multiline string with regular newlines
multiline_string = """Line 1
Line 2
Line 3"""
print("\nMultiline string:")
print(multiline_string)

boolean_var = True

print(integer_var)
print(float_var)
print(string_var)
print(boolean_var)

print(type(integer_var))

# simultaneous assignment
a, b = 3, 4
print(a, b)
a, b = b, a
print(a, b)

# augmented assignment
a += 1
print(a)

# augmented assignment with multiplication
a *= 2
print(a)

# you cannot add a string and a number

# https://stackoverflow.com/questions/16409901/simultaneous-assignment-semantics-in-python