# Prompt the user to input the first number
first_number = int(input("Please insert your first number: "))

# Prompt the user to input the second number
second_number = int(input("Please insert your second number: "))

# Prompt the user to input the operation they want to perform
operation = input("Please insert the operation you want to perform: ")

# Perform the operation based on the user's input
if operation == "+":
    # If the operation is addition, add the two numbers
    result = first_number + second_number
elif operation == "-":
    # If the operation is subtraction, subtract the second number from the first number
    result = first_number - second_number
elif operation == "*":
    # If the operation is multiplication, multiply the two numbers
    result = first_number * second_number
else:
    # If the operation is not supported, set the result to None and print an error message
    result = None
    print("This operation is not supported. Supported operations are: + - * / ")

# If the result is not None, print the result
if result is not None:
    print("The Result is:", + result)

# Print a thank you message to the user
print("Thanks for using our software")