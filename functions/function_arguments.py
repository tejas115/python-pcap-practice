def update(x):
    print(f"id(x) before update: {id(x)}")
    x = 8
    print(f"x: {x}")
    print(f"id(x) after update: {id(x)}")

def update_list(lst):
    print(f"id(lst) before update: {id(lst)}")
    lst[0] = 100
    print(f"lst: {lst}")
    print(f"id(lst) after update: {id(lst)}")

a = 10
print(f"id(a) before update: {id(a)}")
update(a)
print(f"a: {a}")
print(f"id(a) after update: {id(a)}")

# list is mutable, id stays the same after update
lst = [1, 2, 3, 4, 5]
print(f"id(lst) before update: {id(lst)}")
update_list(lst)
print(f"lst: {lst}")
print(f"id(lst) after update: {id(lst)}")
