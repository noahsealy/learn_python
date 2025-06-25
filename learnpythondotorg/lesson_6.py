astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))

astring = "Hello world!"
print(astring.index("o"))

# first occurence of the letter o
astring = "Hello world!"
print(astring.count("l"))

astring = "Hello world!"
print(astring[3:7])

print(astring[2:])
print(astring[:2])

# This way, -3 means "3rd character from the end".
print(astring[::-3])

print(astring[3:7:2])

# [start:stop:step]

astring = "Hello world!"
print(astring[::-1])

astring = "Hello world!"
print(astring.upper())
print(astring.lower())
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

afewwords = astring.split(" ")
print(afewwords)