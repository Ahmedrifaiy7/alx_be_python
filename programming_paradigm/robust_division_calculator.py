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
        return "Error: Division by zero is not allowed."

    except ValueError:
        return "Error: Non-numeric input detected. Please provide valid numbers."

