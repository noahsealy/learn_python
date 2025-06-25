# start, stop, step
for x in range(3, 8, 2):
    print(x, end=" ")
print('')
for x in range(3, 8):
    print(x, end=" ")

# Prints out 0,1,2,3,4
count = 0
while True:
    print(count, end=" ")
    count += 1
    if count >= 5:
        break
print('')
# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x, end=" ")