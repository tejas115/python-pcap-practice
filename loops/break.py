available_candy = 5

candy_requested = int(input("Enter number of candies to dispense: "))
i = 0
while i < candy_requested:
    if available_candy <= 0:
        print("out of candy")
        break

    print("Dispensing candy")
    i += 1
    available_candy -= 1

print("Thank you, please come again!")