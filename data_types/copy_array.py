from numpy import *

arr = array([1, 2, 3, 4, 5], int)

arr = arr + 5

print(arr)

arr1 = array([1, 2, 3, 4, 5], int)
arr2 = array([6, 7, 8, 9, 10], int)

arr3 = arr1 + arr2

print(arr3)
print (f"sin(arr3): {sin(arr3)}")
print(f"sqrt(arr3): {sqrt(arr3)}")
print(f"cos(arr3): {cos(arr3)}")
print(f"log(arr3): {log(arr3)}")
print(f"min(arr3): {min(arr3)}")
print(f"sum(arr3): {sum(arr3)}")

print(concatenate((arr1, arr2)))

arr4 = arr2

print(arr4)
print(arr2)

print(id(arr4))
print(id(arr2))


# Shallow copy
arr5 = arr2.view() # shallow copy
print(f"arr5: {arr5}")
print(f"arr2: {arr2}")
print(f"id(arr5): {id(arr5)}")
print(f"id(arr2): {id(arr2)}")

arr5[0] = 100

print(f"arr5: {arr5}")
print(f"arr2: {arr2}")


# deep copy

arr6 = arr2.copy() # deep copy
print(f"arr6: {arr6}")
print(f"arr2: {arr2}")
print(f"id(arr6): {id(arr6)}")
print(f"id(arr2): {id(arr2)}")

arr6[0] = 200

print(f"arr6: {arr6}")
print(f"arr2: {arr2}")
