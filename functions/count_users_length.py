# Take 5 names from the user and Count the number of users greater than length 5
def count_users_with_long_names(name_list):
    count = 0
    for name in name_list:
        if len(name) > 5:
            count += 1
    return count


name_list = []

for i in range(5):
    name = input("Enter name {}: ".format(i + 1))
    name_list.append(name)


print("Number of users with names greater than length 5: {}".format(count_users_with_long_names(name_list)))