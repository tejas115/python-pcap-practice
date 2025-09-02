a = 10
b = 5
c = 5
print(id(c))
def something():
    a= 15 # local variable
    global b # global variable  
    b = 8
    x = globals()['c'] # to access all global variables
    globals()['c'] = 10
    print(id(c))
    print("in fun a", a)
    print("in fun b", b) # global variable
    print("in fun x", x) # global variable
    print('in fun c', c) # global variable


something()

print("out function: a ", a)
print("out function: b ", b)
print("out function: c ", c)
