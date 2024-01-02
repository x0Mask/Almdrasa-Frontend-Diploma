def calculate(first_number, second_number, operator):
    """
    Calculates the result of the given mathematical operation.

    Args:
        first_number (int): The first number.
        second_number (int): The second number.
        operator (str): The mathematical operator ('+', '-', or '*').

    Returns:
        None
    """
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    else:
        result = "This operation is not supported. Supported operations are: + - *"
    print("Result is:", result)

# Perform calculations
calculate(5, 6, "+")
calculate(6, 45, "-")
calculate(6, 11, "*")
calculate(15, 54, "+")