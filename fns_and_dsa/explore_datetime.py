from datetime import datetime, timedelta


def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Display the current date and time
    print(f"Current date and time: {formatted_date}")


def calculate_future_date():
    # Prompt the user to enter a number of days
    try:
        days = int(input("Enter the number of days to add: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    # Get the current date
    current_date = datetime.now()
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days)
    # Format the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    # Display the future date
    print(f"The date after {days} days will be: {formatted_future_date}")


def main():
    display_current_datetime()
    calculate_future_date()


if __name__ == "__main__":
    main()
