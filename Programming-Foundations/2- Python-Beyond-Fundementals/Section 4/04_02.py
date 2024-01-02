# Initialize variables
firstName = "abu Bakr"
lastName = "Al-Siddiq"
title = "The Caliph of Muslims"
title = "The, Caliph, of, Muslims"

# Print capitalized first name
print(firstName.capitalize())

# Print last name in lowercase
print(lastName.lower())

# Find the index of the word "Muslims" in the title
print(title.find("Muslims"))

# Replace the word "Muslims" with "Islam" in the title
print(title.replace("Muslims", "Islam"))

# Print a substring of the title starting from index 4
print(title[4:])

# Split the title by commas and iterate over the parts
parts = title.split(",")
for part in parts:
    # Strip leading/trailing whitespace and capitalize each part
    print(part.strip().capitalize())