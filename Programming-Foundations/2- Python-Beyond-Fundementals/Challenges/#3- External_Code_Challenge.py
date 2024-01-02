from personal_modules import calculate

# Get user input
first_number = int(input("Please, enter your first number: "))
second_number = int(input("Please, enter your second number: "))
operation = input("Please, Insert the operation (*, /, -, +, pow, sqrt, random): ")

# Perform the operation based on user input
if operation == "*":
    result = calculate.multible(first_number, second_number)
elif operation == "/":
    result = calculate.division(first_number, second_number)
elif operation == "-":
    result = calculate.subtraction(first_number, second_number)
elif operation == "+":
    result = calculate.addition(first_number, second_number)
elif operation == "pow":
    result = second_number ** first_number
elif operation == "sqrt":
    result = math.sqrt(first_number)
elif operation == "random":
    result = random2.randrange(first_number, second_number)

# Print the result
print(f"The result is: {result}")