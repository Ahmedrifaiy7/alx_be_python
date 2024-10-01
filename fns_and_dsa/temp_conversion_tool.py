FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)  # Ensure the input is numeric
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    celsius = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    try:
        celsius = float(celsius)  # Ensure the input is numeric
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
    return fahrenheit


def main():
    try:
        temp = input("Enter the temperature: ")
        unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp:.2f}°C.")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp:.2f}°F.")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(e)


# Run the program
if __name__ == "__main__":
    main()
