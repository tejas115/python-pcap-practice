''' This function performs a linear search on a list. '''
# search the list for a value using for loop.
def linear_search(search_list, given_value):
    ''' function searching for a value in a list '''
    for i, v in enumerate(search_list):
        if v == given_value:
            return True, i
    return False, -1

lst = [5, 8, 4, 6, 9, 2]

value = input("Enter a value to search for: ")
found, pos = linear_search(lst, int(value))
if found:
    print(f"Found {value} at position {pos+1}")
else:
    print(f"{value} not found in the list.")
# End-of-file (EOF)
