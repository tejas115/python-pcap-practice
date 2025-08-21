"""Array operations and manipulations"""

from array import *

vals = array('i', [1, 2, 3, 4, 5])
print(vals.buffer_info())  # Get buffer info of the array
print(vals[0])  # Access the first element
vals[1] = 10  # Modify the second element
print(vals)
vals.append(6)  # Append a new element
print(vals)
vals.insert(2, 20)  # Insert an element at index 2
print(vals)
vals.remove(10)  # Remove the first occurrence of 10
print(vals)
for index, val in enumerate(vals):
    print(index, val)


for e in vals:
    print(e, end=", ")  # Print all elements in the array
print()

# work with chars array
char_vals = array('u', ['a', 'e', 'c', 'i'])

for e in vals:
    print(e, end=", ")  # Print all elements in the integer array


newArr = array(vals.typecode, (a for a in vals))
print("\nNew Array:", newArr)  # Print the new array created from vals
for e in newArr:
    print(e, end=", ")  # Print all elements in the new array

newArr = array(vals.typecode, (a*a for a in vals))
print("\nNew Array:", newArr)  # Print the new array created from vals
for e in newArr:
    print(e, end=", ")  # Print all elements in the new array
print()

i = 0

while i < len(newArr):
    print(newArr[i], end=", ")  # Print elements using a while loop
    i += 1
print()
# End-of-file (EOF)