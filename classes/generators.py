
def topten():
    n = 1
    while n <= 10:
        yield n
        n += 1

values = topten()

for value in values:
    print(value)
