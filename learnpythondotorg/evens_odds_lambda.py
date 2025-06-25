l = [2,4,7,3,14,19]
odds_evens = lambda x: x % 2 == 0
for i in l:
    odd_even = odds_evens(i)
    print(f'{i} is even?: {odd_even}')