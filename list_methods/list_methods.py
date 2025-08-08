numbers = ['1', '010', 3]
sum_numbers = sum(float(n) for n in numbers)  # expected outcome 14.0
print(sum_numbers)

#1 list methods - append
people = ['Alice', 'Bob', 'Charlie']
people.append('Diana')  # expected outcome ['Alice', 'Bob', 'Charlie', 'Diana']
print(people)

#2 list methods - clear
people.clear()  # expected outcome []
print(people)

#3 list methods - copy
# copy creates a shallow copy of the list.
people = ['Alice', 'Bob', 'Charlie']
copy_people : list[str] = people.copy()  # expected outcome ['Alice', 'Bob', 'Charlie']
print(copy_people)

copy_people.remove('Alice')  # expected outcome ['Bob', 'Charlie']
print(f"people: {people}")
print(f"copy_people: {copy_people}")  # to show that copy_people is a shallow copy of people


#4 list methods - count
numbers = [1, 2, 3, 2, 4, 2]
count_of_twos = numbers.count(2)  # expected outcome 3
print(f"Count of 2s: {count_of_twos}")  

people = ['Alice', 'Bob', 'Charlie', 'Alice']
count_of_alices = people.count('Alice')  # expected outcome 2
print(f"Count of Alice: {count_of_alices}")

#5 list methods - extend
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)  # expected outcome [1, 2, 3, 4, 5, 6]
print(list1)

people = ['Alice', 'Bob']
more_people = ['Charlie', 'Diana']  
people.extend(more_people)  # expected outcome ['Alice', 'Bob', 'Charlie', 'Diana']
print(people)   
people.extend([more_people])  # extending with a list of lists
print(people)  # expected outcome ['Alice', 'Bob', 'Charlie', 'Diana', ['Charlie', 'Diana']]

#6 list methods - index
numbers = [1, 2, 3, 4, 5]
index_of_three = numbers.index(3)  # expected outcome 2
print(f"Index of 3: {index_of_three}")
people = ['Alice', 'Bob', 'Charlie']
index_of_bob = people.index('Bob')  # expected outcome 1
print(f"Index of Bob: {index_of_bob}")

#7 list methods - insert
people = ['Alice', 'Charlie']
people.insert(1, 'Bob')  # expected outcome ['Alice', 'Bob', 'Charlie']
print(people)

# 8 list methods - pop
people = ['Alice', 'Bob', 'Charlie']
popped_person = people.pop()  # expected outcome 'Charlie'
print(f"Popped person: {popped_person}")
print(f"People after pop: {people}")

#9 list methods - remove
people = ['Alice', 'Bob', 'Charlie']
people.remove('Bob')  # expected outcome ['Alice', 'Charlie']
print(f"People after remove: {people}")

#10 list methods - reverse
people = ['Alice', 'Charlie']
people.reverse()  # expected outcome ['Charlie', 'Alice']
print(f"People after reverse: {people}")

#11 list methods - sort
numbers = [3, 1, 4, 2]
numbers.sort()  # expected outcome [1, 2, 3, 4]
print(f"Sorted numbers: {numbers}")

people = ['Charlie', 'Alice', 'Bob']
people.sort()  # expected outcome ['Alice', 'Bob', 'Charlie']
print(f"Sorted people: {people}")

#12 list methods - sort with key
people = ['Charlie', 'Alice', 'Bob', 'luigi']
people.sort(key=len)  # expected outcome ['Bob', 'Alice', 'Charlie', 'luigi']
print(f"Sorted people by length: {people}")

people.sort(key=lambda name: len(name), reverse=True)  # expected outcome ['Charlie', 'Alice', 'Bob', 'luigi']
print(f"Sorted people by length in reverse: {people}")

people.sort(key=lambda name: len(name), reverse=False)  # expected outcome ['Bob', 'Alice', 'Charlie', 'luigi']
print(f"Sorted people by length in ascending order: {people}")

people.sort(key=lambda name: name.lower())  # expected outcome ['Alice', 'Bob', 'Charlie', 'luigi']
print(f"Sorted people by name (case-insensitive): {people}")


