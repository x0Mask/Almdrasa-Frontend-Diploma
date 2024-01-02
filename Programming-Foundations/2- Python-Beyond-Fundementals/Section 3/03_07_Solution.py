from personal_modules import calculate
import math
import random2

firstNumber = input("Insert your first number ")
secondNumber = input("Insert your second number ")
operation = input("Insert your operation ")

firstNumber = int(firstNumber)
secondNumber = int(secondNumber)

result = 0
if operation == "+":
    result = calculate.sum(firstNumber, secondNumber)
elif operation == "-":
    result = calculate.sub(firstNumber, secondNumber)
elif operation == "*":
    result = calculate.multi(firstNumber, secondNumber)
elif operation == "/":
    result = calculate.divide(firstNumber, secondNumber)
elif operation == "pow":
    result = math.pow(firstNumber, secondNumber)
elif operation == "sqrt":
    result = math.sqrt(firstNumber)
elif operation == "random":
    result = random2.randint(firstNumber, secondNumber)

print(f"result: {result}")