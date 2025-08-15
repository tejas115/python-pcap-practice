# finally block executes after each attempt, whether successful or not, and there's no recursive call stack confusion.

def division():
    while True:
        try:
            print("resource open")
            number1 = input("Enter a number: ")
            number2 = input("Enter another number: ")
            result = float(number1) / float(number2)
            print(result)
            break  # Exit the loop on success
        except ZeroDivisionError as zde:
            print("Zero division error, please try again.", zde)
        except ValueError as ve:
            print("Invalid input. Please enter numeric values.", ve)
        except Exception as e:
            print("something went wrong, try again:", e)
        finally:
            print("resource closed")

division()