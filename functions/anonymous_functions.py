# Anonymous function (lambda)

# regular function
def square(x):
    return x * x

result = square(5)
print("The square of 5 is:", result)

lambda_square = lambda x: x * x
print("The square of 5 is:", lambda_square(5))

lambda_sum = lambda a, b: a + b
print("The sum of 5 and 10 is:", lambda_sum(5, 10))
