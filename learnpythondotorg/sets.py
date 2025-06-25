# Sets are lists with no duplicate entries.
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.intersection(b))
print(b.intersection(a))

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

print(a.difference(b))
print(b.difference(a))

print(a.union(b))

# list all participants that containing everyone in A who did not attend B
a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

print(set(a).intersection(set(a).symmetric_difference(set(b))))

# OR

print(set(a).difference(set(b)))