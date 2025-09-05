'''program that performs bubble sort'''
def bubble_sort(n):
    '''sorts a list in ascending order using bubble sort'''
    for i in range(len(n)-1, 0, -1):
        for j in range(i):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n



n = [21, 5, 8, 4, 6, 9, 2, 1, 3, 15, 19]
sorted_n = bubble_sort(n)
print(sorted_n)
