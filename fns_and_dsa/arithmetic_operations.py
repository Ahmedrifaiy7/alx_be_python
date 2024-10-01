def perform_operation(num1: float, num2: float, operation: str) -> float:
    """
    Performs basic arithmetic operations based on the operation parameter.

    Args:
        num1 (float): The first numerical value.
        num2 (float): The second numerical value.
        operation (str): The operation to perform, one of 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float: The result of the arithmetic operation.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'."