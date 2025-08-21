""" loop problems showcasing for else""" 

numbers = [12, 16, 18, 21, 26]

for number in numbers:

    if number % 5 == 0:
        print(f"Found multiple of 5: {number}")
        break
else:
    print("No multiple of 5 found.")


# End-of-file (EOF)
