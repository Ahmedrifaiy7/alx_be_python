def draw_pattern():
    try:
        # Prompt the user to enter a positive integer for the pattern size
        size = int(input("Enter the size of the pattern: "))

        if size <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return

    # Initialize the row counter
    row = 0

    # Use a while loop to iterate through each row
    while row < size:
        # Use a for loop to print asterisks for each row
        for col in range(size):
            print("*", end="")  # Print asterisk without advancing to a new line
        print()  # Move to the next line after completing a row
        row += 1  # Increment the row counter


# Run the pattern drawing function
if __name__ == "__main__":
    draw_pattern()
