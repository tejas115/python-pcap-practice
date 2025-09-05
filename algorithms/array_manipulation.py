'''This module we will manipulate the array'''
# Given an array a, your task is to output an array b of the same length by applying the following transformation: 
# – For each i from 0 to a.length - 1 inclusive, b[i] = a[i - 1] + a[i] + a[i + 1]
# – If an element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, use 0 in its place
# – For instance, b[0] = 0 + a[0] + a[1]
''''''
from array import *

def arr_manipulation(arr):
    '''this function manipulates the array'''
    new_arr = array(arr.typecode,[])
    for i in range(len(arr)):
        if i - 1 < 0 :
            temp = 0 + arr[i] + arr[i + 1] 
        elif i + 1 >= len(arr):
            temp = arr[i - 1] + arr[i] + 0
        else:
            temp = arr[i - 1] + arr[i] + arr[i + 1]
        new_arr.append(temp)
    return new_arr

arr = array('i', [4, 0, 1, -2, 3])
print(f"Original Array: {arr} and it's length: {len(arr)}")
b = arr_manipulation(arr)
print(f"New Array: {b} and it's length: {len(b)}")  