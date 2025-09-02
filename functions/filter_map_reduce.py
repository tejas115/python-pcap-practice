# filter, map and reduce

from  functools import reduce

nums = [3, 2, 6, 8, 9, 11, 10, 8, 7]

# def is_even(n):
#     return n % 2 == 0

# evens = list(filter(is_even, nums))

# def add_all(a, b):
#     return a + b

# def double(a):
#     return a * 2

# above function replaced by lambda, filter
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Evens:", evens)

# doubling the even numbers using map and lambda
doubles = list(map(lambda x: x * 2, evens))
print("Doubles:", doubles)

# reducing the list to sum of all elements
sum = reduce(lambda x, y: x + y, doubles)
print("Sum:", sum)
