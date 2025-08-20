numbers = (1, 3, 5, 7, 9)

def filter_nums(num):
    nums = (0, 5, 17, 3)
    if num in nums:
        return True
    else:
        return False


filtered = filter(filter_nums, numbers)
for num in filtered:
    print(num, end=" ")