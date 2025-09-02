def div(a, b):
    if a < b:
        a, b = b, a
    print(a / b)

def smart_div(func):
    def inner(a, b):
        if a > b:
            a, b = b, a
        return func(a, b)
    return inner



div(4, 2)
div(2, 4)

div = smart_div(div)
div(2, 4)