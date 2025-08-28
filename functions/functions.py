def greet():
    print("Hello, welcome to the program!")
    print("This program demonstrates the use of functions in Python.")

def add_sub(a, b):
    return a + b, a - b

greet()
result_add, result_sub = add_sub(5, 10)
print(f"The result of the addition is: {result_add}")
print(f"The result of the subtraction is: {result_sub}")


