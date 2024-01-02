# Prompt the user to enter their name and store it in the variable user_name
user_name = input("Hi, what is your name? ")

# Prompt the user to enter their age and convert the input to an integer, then store it in the variable user_age
user_age = int(input("How old are you? "))

# Check if the user's age is less than 13
if user_age < 13:
    # If the user's age is less than 13, print a message indicating that they are too young to register, followed by their name
    print("You are too young to register, ", user_name)
else:
    # If the user's age is 13 or greater, print a message indicating that they are free to join, followed by their name
    print("Feel free to join, ", user_name)