# factorial using recursion
def fact(n):
    if n < 0:
        print("Invalid input")
        return
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
result = fact(int(input("Enter a number to calculate its factorial: ")))
print("The factorial is:", result)

