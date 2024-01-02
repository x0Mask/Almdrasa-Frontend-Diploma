# Age variable
person_age = 36  # Assigning the value 36 to the variable person_age
print(person_age)  # Printing the value of person_age
print(type(person_age))  # Printing the data type of person_age

# Email variable
email_address = "ahmed.fathy@almdrasa.com"  # Assigning the string "ahmed.fathy@almdrasa.com" to the variable email_address
print(email_address)  # Printing the value of email_address

# String variables
val1 = "ahmed"  # Assigning the string "ahmed" to the variable val1
print(val1)  # Printing the value of val1

# Casting examples
x = str(3)  # Casting the integer 3 to a string and assigning it to the variable x
y = int(3)  # Casting the integer 3 to an integer (no change) and assigning it to the variable y
z = float(3)  # Casting the integer 3 to a float and assigning it to the variable z

# Working with Numbers
print(3 + 2)  # Performing addition of 3 and 2 and printing the result
print(3 - 2)  # Performing subtraction of 2 from 3 and printing the result
print(3 * 2)  # Performing multiplication of 3 and 2 and printing the result
print(3 / 2)  # Performing division of 3 by 2 and printing the result
print(3 % 2)  # Performing modulo operation of 3 divided by 2 and printing the remainder
print(3 // 2)  # Performing integer division of 3 by 2 and printing the result
print(3 ** 2)  # Performing exponentiation of 3 raised to the power of 2 and printing the result

# Working with Strings
print("Almdarasa loves you")  # Printing the string "Almdarasa loves you"
print('He said "hello ahmed"')  # Printing the string 'He said "hello ahmed"'

# Multi-line string variables
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""  # Assigning a multi-line string to the variable a
print(a)  # Printing the value of a

b = '''my name is mohamed 
my age is 23
i am currently in the military service'''  # Assigning a multi-line string to the variable b
print(b)  # Printing the value of b

# Function example
def print_salary(salary):  # Defining a function named print_salary that takes a parameter named salary
    print(salary)  # Printing the value of the salary parameter

print_salary(8000)  # Calling the print_salary function with the argument 8000

# Variable sum
var1 = 1  # Assigning the value 1 to the variable var1
var2 = 2  # Assigning the value 2 to the variable var2
var3 = "3"  # Assigning the string "3" to the variable var3
print(var1 + var2 + int(var3))  # Converting var3 to an integer, adding var1, var2, and var3, and printing the result