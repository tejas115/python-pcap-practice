'''this program will do selection sort'''

def selection_sort(lst):
    '''sorts a list in ascending order using selection sort'''
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

lst = [21, 5, 8, 4, 6, 9, 2, 1, 3, 15, 19, 3, 14, 23, 19]
sorted_lst = selection_sort(lst)
print(sorted_lst)