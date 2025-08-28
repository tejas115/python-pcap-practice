from numpy import *

arr1 = array([[1, 2, 3, 6, 2, 9], [4, 5, 6, 8, 10, 12]], int)
print(f"Array 1: {arr1}")
print(f"Array 1 dtype: {arr1.dtype}")

print(f"Array 1 shape: {arr1.shape}")
print(f"Array 1 ndim: {arr1.ndim}")
print(f"Array 1 size: {arr1.size}")

arr2 = arr1.flatten()
print(f"Array 2: {arr2}")
print(f"Array 2 dtype: {arr2.dtype}")

print(f"Array 2 shape: {arr2.shape}")
print(f"Array 2 ndim: {arr2.ndim}")
print(f"Array 2 size: {arr2.size}")


arr3 = arr1.reshape(3, 4)
print(f"Array 3: {arr3}")

arr4 = arr1.reshape(2, 2, 3)
print(f"Array 4: {arr4}")

m  = matrix(arr1)
print(f"Matrix: {m}")

m1 = matrix('1 2 3; 4 5 6')
print(f"Matrix 1: {m1}")

m2 = matrix('1 2; 3 4; 4 5; 6 7', int)
print(f"Matrix 2: {m2}")
print(f"Diagonal: {m2.diagonal()}")


m3 = matrix('1 2 3; 4 5 6; 7 8 9')
print(f"Matrix 3: {m3}")
print(f"Diagonal: {m3.diagonal()}")
print(f"max: {m3.max()}")
print(f"min: {m3.min()}")

m4 = matrix('1 2 3; 6 8 7; 8 8 9')
print(f"Matrix 4: {m4}")

m5 = m3 + m4
print(f"Matrix 5: {m5}")

m6 = m3 * m4
print(f"Matrix 6: {m6}")