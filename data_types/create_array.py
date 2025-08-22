from numpy import *

# arr = array([1, 2, 3, 4, 5], int) - int array example
# arr = array([1, 2, 3, 4, 5], float) - float array example
# arr = array([1, 2, 3, 4, 5]) - implicit type (int)

arr = array([1, 2, 3, 4, 5], float) # float array - one way to create array
print(arr)
print(arr.dtype)


# linspace - to create array.

arr1 = linspace(0,16, 10) # float array - one way to create array. generate 10 evenly spaced values between 0 and 16
print(f"arr1: {arr1}")

arr2 = linspace(0, 10) # float array - one way to create array. generate 50 evenly spaced values between 0 and 10
print(f"arr2: {arr2}")

# Generate 5 evenly spaced numbers between 0 and 10 (inclusive)
arr3 = linspace(0, 10, 5)
print(f"Array 3: {arr3}")

# Generate 5 evenly spaced numbers between 0 and 10 (exclusive of 10)
arr4 = linspace(0, 10, 5, endpoint=False)
print(f"Array 4: {arr4}")

# Generate 5 evenly spaced numbers and return the step size
arr5, step = linspace(0, 10, 5, retstep=True)
print(f"Array 5: {arr5}, Step: {step}")


# using arange
arr6 = arange(0, 10, 2)  # float array - one way to create array. generate values from 0 to 10 with step of 2
print(f"Array 6: {arr6}")

# using logspace
arr7 = logspace(0, 3, 4)  # float array - one way to create array. generate 4 values spaced evenly on a log scale from 10^0 to 10^3
print(f"Array 7: {arr7}")

# using zeros
arr8 = zeros(5)  # float array - one way to create array. generate an array of 5 zeros
print(f"Array 8: {arr8}")

# using ones
arr9 = ones(5)  # float array - one way to create array. generate an array of 5 ones
print(f"Array 9: {arr9}")

arr10 = ones((5, int(2)))  # float array - one way to create array. generate a 5x2 array of ones
print(f"Array 10: {arr10}")