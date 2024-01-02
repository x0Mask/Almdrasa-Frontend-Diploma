first_number = int(input("Insert your first number: "))
second_number = int(input("Insert your second number: "))
operator = input("Insert the operation (+, -, *): ")


if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
else:
    print("We don't support this operation")
    exit()

print(f"{first_number} {operator} {second_number} = {result}") # is a Python f-string that prints the values of num1, operator, num2, and result in a formatted string. 
# The f before the opening quote indicates that this is an f-string, which allows you to embed expressions inside string literals using curly braces {}
print("Thanks for using our software")