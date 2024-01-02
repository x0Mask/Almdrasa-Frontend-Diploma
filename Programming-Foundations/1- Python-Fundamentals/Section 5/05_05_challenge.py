def calculate(operand1, operand2, multiplier):
    """
    Calculate the result by adding the two operands and multiplying the sum by the multiplier.

    Args:
        operand1 (int): The first operand.
        operand2 (int): The second operand.
        multiplier (int): The multiplier.

    Returns:
        int: The calculated result.
    """
    result = (operand1 + operand2) * multiplier
    return result

# Calculate and print the results
print(calculate(5, 4, 5))  # (5 + 4) * 5 = 45
print(calculate(8, 11, 7)) # (8 + 11) * 7 = 133
print(calculate(15, 99, 10)) # (15 + 99) * 10 = 1140