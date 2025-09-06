names = ("John", "Jane", "Doe", "alice", "John")
comps = ("dell", "apple", "hp", "Ms", "dell")

zipped = zip(names, comps)  # returns a zip object

print(zipped) # <zip object at 0x00000123456789AB>

print(list(zipped))


set_zipped = set(zip(names, comps)) # removes duplicates and gives set - unique pairs
print(set_zipped)

dict_zipped = dict(zip(names, comps)) # converts to dictionary
print(dict_zipped)

for(a,b) in zip(names, comps):
    print(f"{a} works at {b}")