def multiplication_table():
    try:
        # Prompt the user to input a number
        number = float(input("Enter a number to see its multiplication table: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    # Use a for loop to iterate through numbers 1 to 10
    for i in range(1, 11):
        product = number * i
        # Print each line of the multiplication table
        print(f"{number} * {i} = {product}")

# Run the multiplication table function
if __name__ == "__main__":
    multiplication_table()