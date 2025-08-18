mix_list = [1, "python", 0.5, "Apple", 3.0, "\n"]
#create the numbers list using the lambda function
numbers = list(filter(lambda n: isinstance(n, (int, float)) or isinstance(n, int), mix_list))

print(numbers)  # Output: [1, 0.5, 3.0] 
