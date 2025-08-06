import math

def is_triangle(a, b, c):
    if math.hypot(a, b) == c:
        return True
    return False

print("The program checks if three sides can form a triangle.")
inp1 = int(input("Enter the first side: "))
inp2 = int(input("Enter the second side: "))
inp3 = int(input("Enter the third side: "))

print("Is it a triangle?", is_triangle(inp1, inp2, inp3))