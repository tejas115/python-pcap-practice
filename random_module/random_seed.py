# Add necessary imports here
import random

# Write the function random_seed
def random_seed(s):
  random.seed(s)
  return random.random() 

s = float(input("Enter a value: "))
print(random_seed(s))
