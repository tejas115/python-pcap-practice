name = input("Enter your name: ")
# result = len(name)  # expected outcome is the length of the name entered
#occurence = name.find("e")

# occurence = name.rfind("q")

# name = name.capitalize()
# name = name.capitalize() #capitalize only the first character
# name = name.upper() # convert the entire string to uppercase
name = name.lower() # convert the entire string to lowercase

phone_number = input("Enter your phone number: ")
phone_number = phone_number.replace("-", "")  # remove dashes
result = phone_number.count("-")



# result = name.isdigit()  # checks if the string contains only digits
# result = name.isalpha()  # checks if the string contains only alphabets
# result = name.isspace()  # checks if the string contains only whitespace characters
print(name)
print(phone_number)
print(result)
print(help(str)) #  displays all the methods available for string objects
# print(occurence)
