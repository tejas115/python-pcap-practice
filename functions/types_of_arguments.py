def person(name, age=18):
    print(name, age)

def sum(*b):
    c = 0
    for i in b:
        c += i
    print(c)

person(age= 28, name='tejas')

person(name='john')

sum(5, 10)

sum(5, 6, 34, 78)
