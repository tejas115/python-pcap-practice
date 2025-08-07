# Do any necessary imports here
import math

# Complete the function
def circle_area(r):
    return math.pi * r ** 2


inp = float(input("Enter the radius of a circle:"))
print("Area of circle =", circle_area(inp))
