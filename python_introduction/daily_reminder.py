def daily_reminder():
    # Prompt the user to input task details
    task = input("Enter your task: ")
    priority = input("priority (high, medium, low): ").lower()
    time_bound = input("Is it time-bound? (yes or no): ").lower()

    # Process the task based on priority using match case
    match priority:
        case 'high':
            reminder = f"Reminder: '{task}' is a high-priority task that requires immediate attention today!."
        case 'medium':
            reminder = f"The task '{task}' is a medium-priority task."
        case 'low':
            reminder = f"Note: '{task}' is a low-priority task. Consider completing it when you have free time."
        case _:
            print("Invalid priority level! Please enter high, medium, or low.")
            return

    # Modify the reminder if the task is time-sensitive
    if time_bound == 'yes':
        reminder += " This task requires immediate attention today!"

    # Provide the final reminder
    print(reminder)

# Run the daily reminder function
if __name__ == "__main__":
    daily_reminder()
