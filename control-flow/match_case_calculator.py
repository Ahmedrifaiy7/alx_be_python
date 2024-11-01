def calculator():
    try:
        # Prompt the user to enter two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        return

    # Ask the user to choose the operation
    operation = input("Choose the operation (+, -, *, /): ")

    # Perform the calculation using match case
    match operation:
        case '+':
            result = num1 + num2
            print(f"The result is {result}")
        case '-':
            result = num1 - num2
            print(f"The result is {result}")
        case '*':
            result = num1 * num2
            print(f"The result is {result}")
        case '/':
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result is {result}")
        case _:
            print("Invalid operation! Please choose a valid operator (+, -, *, /).")

# Run the calculator
if __name__ == "__main__":
    calculator()
