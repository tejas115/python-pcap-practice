# validate user input for a username exercise
# 1. user name is no more than 12 characters
# 2. user name must not contain any spaces
# 3. user name must not contain any digits

username = input("Enter your username: ")

if len(username) > 12:
    print("Username must be no more than 12 characters.")
elif not  username.find(" ") == -1:
    print("Username must not contain any spaces.")
elif any(char.isdigit() for char in username):
    print("Username must not contain any digits.")
else:
    print(f"Username '{username}' is valid, Welcome '{username}'.")
