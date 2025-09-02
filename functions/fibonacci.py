# fibonnaci series
def fibonacci(n):
    a, b = 0, 1
    if n < 1:
        print("you entered a negative number")
        return
    elif n == 1:
        print(a, end=" ")
    else:
        print(a, b, end=" ")
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c, end=" ")

n = int(input("Enter a number: "))
fibonacci(n)
print()

