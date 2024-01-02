# Greet the user
name = input("What's your name? ")

# Print a greeting message
print("It's nice to meet you,", name)

# Get feedback on the course
course_feedback = input("Are you enjoying the course? (answer Yes or No) ").capitalize()

# Check the feedback and provide a response
if course_feedback == "Yes":
    print("That's good to hear!")
else:
    print("Oh no! That makes me sad!")