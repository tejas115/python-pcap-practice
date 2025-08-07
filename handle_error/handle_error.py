def division():
    global number1, number2
    number1 = input("Enter a number: ")
    number2 = input("Enter another number: ")


#rewrite the code so that all if/elif/else statements are replaced by a try/except code block. Use two named exceptions and one unnamed.
    try:
        print(float(number1) / float(number2))
        return
    except ZeroDivisionError as zde:
        print("Zero division error, please try again.", zde)
        division() # retry
    except ValueError as ve:
        print("Invalid input. Please enter numeric values.", ve )
        division() # retry
    except Exception as e:
        print("something went wrong, try again:", e)
        division()  # retry



division()
