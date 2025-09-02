def fact(n):
    if n < 0:
        return "Invalid input"
    
    elif n == 0:
        return 1
    else:
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f

x = int(input("Enter a number to calculate its factorial: "))
print("Factorial of", x, "is", fact(x))
