while True:
    try:
        num1 = float(input("Please enter number one: "))
        num2 = float(input("Please enter number two: "))

        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is  {result}")

    except ZeroDivisionError:
        print("Error: division  by  zero  is not possible.")

    except ValueError as e:
        print(e)
        print("Error: please enter  valid numbers.")
        continue

    continue_choice = input("Do  you  want to  continue? (yes/no): ").strip().lower()
    if continue_choice == 'no':
        print("Exiting the program.")
        break