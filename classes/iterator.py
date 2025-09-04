# Iterables = An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop.

# numbers = [7,8,9, 5]
# print(numbers[0])  # Output: 7

# for number in numbers:
#     print(number, end=", ")  # Output: 7, 8, 9, 5

# it = iter(numbers)
# print(it)
# print(it.__next__())  # Output: 7
# print(it.__next__())  # Output: 8

# print(next(it))  # Output: 9


class TopTen:
    
    def __init__(self):
        self.num = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num > 10:
            raise StopIteration
        val = self.num
        self.num += 1
        
        return val
    
values = TopTen()
print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))

# will only print 1 once because of iteration
for i in values:
    print(i)