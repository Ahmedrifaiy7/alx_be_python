# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert inputs to float
        numerator = float(numerator)
        denominator = float(denominator)

        # Try performing the division
        result = numerator / denominator
        return f"Result: {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero.."

    except ValueError:
        return "Error: Non-numeric input detected. Please provide valid numbers."

