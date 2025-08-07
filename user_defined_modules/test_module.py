import main


new_list = [i+1 for i in range(3)]
print(main.counter(new_list))
print("Counter function works correctly:", main.counter(new_list) == main.count)
