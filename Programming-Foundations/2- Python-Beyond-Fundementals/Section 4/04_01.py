# Prompt the user for their name
name = input("What's your name? ")

# Prompt the user for their age
age = input("How old are you? ")

# Prompt the user for their country
country = input("Where do you live? ")

# Prompt the user for their job
job = input("What's your job? ")

# Build the result string using concatenation
result = "Welcome " + name
result += ". Your age is " + age 
result += ". You live at " + country
result += ". You work as " + job

# Print the result string
print(result)

# Build the result string using f-string formatting
result = f"Welcome {name}. Your age is {age}. You live at {country}. You work as {job}"

# Print the result string
print(result)