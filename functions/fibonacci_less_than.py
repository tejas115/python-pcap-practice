# fibonnaci series
def fibonacci(n):
    if n < 1:
        print("you entered a negative number")
        return
    elif n == 1:
        print(a, end=" ")
    else:
        a, b = 0, 1
        print(a, b, end=" ")
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            if (c < n):
                print(c, end=" ")
            else:
                break

n = int(input("Enter the number till you want to see the fibonacci series: "))
fibonacci(n)
print()
