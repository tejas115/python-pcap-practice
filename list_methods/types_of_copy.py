# reference copy. original is a list with a nested list, reference is a reference to original.
# Modifying reference will also modify original.
original = [1, [2, 3], 4]
reference = original
reference[0] = 'changed'
print(original)  # ['changed', [2, 3], 4] - original is modified!

# shallow copy. # original is a list with a nested list, shallow_copy is a new list that contains references to the same objects.
# Modifying shallow_copy will not modify original, but modifying nested objects will.
import copy
original = [1, [2, 3], 4]
shallow_copy = copy.copy(original)
shallow_copy[0] = 'changed'
shallow_copy[1][0] = 'also changed'
print(original)  # [1, ['also changed', 3], 4] - original is partially modified!


# deep copy. # original is a list with a nested list, deep_copy is a new list that contains copies of the objects.
# Modifying deep_copy will not modify original, even for nested objects.
import copy
original = [1, [2, 3], 4]
deep_copy = copy.deepcopy(original)
deep_copy[0] = 'changed'
deep_copy[1][0] = 'also changed'
print(original)  # [1, [2, 3], 4] - original is not modified!
print(deep_copy)  # ['changed', ['also changed', 3], 4] - deep copy is modified independently