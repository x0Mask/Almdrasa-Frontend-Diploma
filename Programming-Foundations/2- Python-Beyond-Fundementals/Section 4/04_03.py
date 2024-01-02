import re

# Define a string containing the phrase
phrase = "ahmed 281 years old and mohamed 30 years old and sara is 1 years old"

# Use the re.sub() function to replace the first occurrence of "ahmed" or "mohamed" followed by a space and any number of digits (\d*)
# with just "ahmed". The fourth argument, 1, limits the substitution to the first match.
result = re.sub("(ahmed|mohamed) \d*", "ahmed", phrase, 1)

# Print the modified phrase
print(result)