# let's learn string slicing and methods
# This code is part of a practice module for string methods in Python

mystring = "Learning Python is fun!"
mystring_sliced = mystring[9:15:1]  # slicing the string to get 'Python' 
print(mystring_sliced)  # Output: Python

# No stop index specified, so it goes to the end of the string
mystring_sliced_end = mystring[9:]  # slicing the string to get 'Python is fun!'
print(mystring_sliced_end)  # Output: Python is fun!


# No start index specified, so it starts from the beginning
mystring_sliced_start = mystring[:8]  # slicing the string to get 'Learning'
print(mystring_sliced_start)  # Output: Learning

#no start or stop index specified, so it takes the whole string
mystring_sliced_full = mystring[:]  # slicing the string to get 'Learning Python is fun!'
mystring_step_size_only = mystring[::2]  # slicing the string with a step size of 2
print(mystring_step_size_only)  # Output: Lann yhn sfn!
print(mystring_sliced_full)  # Output: Learning Python is fun!  

# no start  or stop or step size specified, so it takes the whole string
mystring_no_step = mystring[::]  # slicing the string with no step size
print(mystring_no_step)  # Output: Learning Python is fun!

# single character as a substring
mystring_single_char = mystring[0]  # slicing the string to get 'L'
print(mystring_single_char)  # Output: L    

mystring_single_char_next = mystring[8:9]  # slicing the string to get 'P'
print(mystring_single_char_next)  # Output: P   