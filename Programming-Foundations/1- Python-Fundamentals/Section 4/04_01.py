# Prompt the user for their name and greet them
name = input("What's your name? ")
print("It's nice to meet you, " + name)

# Prompt the user for their feedback on the course
course_feedback = input("Are you enjoying the course? ")

# Check the user's feedback and provide a response
if course_feedback == "Yes":
    print("That's good to hear!")
else: 
    print("I am very sorry.")

# Print a final statement
print("Final statement")