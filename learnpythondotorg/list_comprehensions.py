
# List Comprehensions is a very powerful tool, which creates a new list based on another list, in a single, readable line.
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)

# [expression for item in iterable]
squares = [x**2 for x in range(5)]
print(squares)

# [expression for item in iterable if condition]
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# [manipulation for manipulated in iterable if condition]