"""array generated from user input"""
from array import *

arr = array('i', [])

# Get user input for array elements
n = int(input("Enter the number of elements in the array: "))
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

print("Array elements:", arr)

# Check if user input is in the array
search_element = int(input("Enter an element to search for: "))

for e in arr:
    if e == search_element:
        print(f"{search_element} found in the array at index {arr.index(search_element)}.")
        break
else:
    print(f"{search_element} not found in the array.")

if search_element in arr:
    print(f"{search_element} found in the array.")
else:
    print(f"{search_element} not found in the array.")