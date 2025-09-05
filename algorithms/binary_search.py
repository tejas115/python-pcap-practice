''' This function performs a binary search on a sorted list. '''
pos = -1

def search(lst, n):
    l = 0
    u = len(lst) - 1
    while l <= u:
        mid = (l + u) // 2
        if lst[mid] == n:
            globals()['pos'] = mid
            return True
        elif lst[mid] < n:
            l = mid + 1
        else:
            u = mid - 1
    return False

lst = [5, 8, 4, 6, 9, 2, 10001, 1003, 999, 559, 6000, 3345]
sorted_list = sorted(lst)
print(sorted_list)
n = 10001 # 2 # 999 #45

if search(sorted_list, n):
    print(f"Found {n} at position {pos+1}")
else:
    print(f"{n} not found")