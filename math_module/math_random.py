import math
import random
# from random import random, randint, randrange, seed, choice, sample

print("printing the math module")
print(dir(math))
print("printing functions from random module")
print(dir(random))

print("printing the random float")
print(random.random())

for i in range (3):
    print("printing random integer between 1 and 10")
    print(random.randint(1, 10))

for i in range(5):
    print("printing random float with no seed set")
    random.seed()
    print(random.random())

# if the same seed is set, the random numbers generated will be the same.
# This is useful for debugging or testing purposes.
for i in range(5):
    print("printing random float with seed 10")
    random.seed(10)
    print(random.random())



for i in range(5):
    print("printing random integer between 0 and 10")
    print (random.randrange(0,10))

for i in range(5):
    print("printing random integer between 0 and 20")   
    print (random. randrange(20))

for i in range(5):
    print("printing random integer between 0 and 10 with step 3")
    print (random.randrange(0,10,3))

students = ['John', 'Jane', 'Jim', 'Jill']
print("Randomly selected student:", random.choice(students))
print(random.choice(students))

print(" sample of 2 students from the list") # length of the sample list is equal to the second argument.
print(random.sample(students, 2))




