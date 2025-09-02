def person(name, *data):
    print(name)
    print(data)

person('tejas', 28, 'Mumbai', 9864532)


# keyworded variable length arguments - multiple data with keywords.
def kw_person(name, **data):
    print(name)
    print(data)
    for i, j in data.items():
        print(i, j)

kw_person('tejas', age=28, city='Mumbai', phone=9864532)