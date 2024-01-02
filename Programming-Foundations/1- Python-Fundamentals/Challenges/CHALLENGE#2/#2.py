# Prompt the user to insert the first number and store it in the variable first_number
first_number = int(input("Insert your first number: "))

# Prompt the user to insert the second number and store it in the variable second_number
second_number = int(input("Insert your second number: "))

# Prompt the user to insert the operation (+, -, *) and store it in the variable operator
operator = input("Insert the operation (+, -, *): ")

# Check if the operator is '+'
if operator == "+":
    # Perform addition of first_number and second_number and store the result in the variable result
    result = first_number + second_number

# Check if the operator is '-'
elif operator == "-":
    # Perform subtraction of second_number from first_number and store the result in the variable result
    result = first_number - second_number

# Check if the operator is '*'
elif operator == "*":
    # Perform multiplication of first_number and second_number and store the result in the variable result
    result = first_number * second_number

# If none of the above conditions are met, print an error message and exit the program
else:
    print("We don't support this operation")
    exit()

# Print the equation and the result using f-string formatting
print(f"{first_number} {operator} {second_number} = {result}")

# Print a thank you message
print("Thanks for using our software")