# Prompt the user for their first name, last name, age, and job
firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
age = input("How old are you? ")
job = input("What's your job? ")

# String Interpolation
result = f"Your name is {firstName} {lastName}. Your age is {age}. and your job is a {job}"
print(result)

# Concatenation
result = "Your name is " + firstName +" " + lastName+ ". Your age is " + age + ". and your job is a " + job
print(result)

# String Functions

fname = "abu bakr"
lname = "al-siddiq"
title = "the caliph of muslims"

# capitalize the first letter of the first name
print(fname.capitalize())
# capitalize the first letter of the last name
print(lname.capitalize())
# find the index of the word "muslims" in the title
print(title.find("muslims"))
# capitalize the first letter of the title and replace "muslims" with "Islam"
print(title.capitalize().replace("muslims", "Islam"))
# capitalize the first letter of the title starting from the 14th character
print(title[14:].capitalize())
# replace spaces with commas in the title
print(title.replace(" ", ", "))

# split the title into parts using commas as separators
parts = title.replace(" ", ", ").split(",")
for part in parts:
    # remove leading and trailing spaces and capitalize each part
    print(part.strip().capitalize())

# Creating Regular Expression

import re;

phrase = "I love my family. I have 2 sisters and 2 brothers."
# search for a phrase that starts with "I" and ends with any character
print(re.search("^I.*.$", phrase))
# search for a whitespace character in the phrase
print(re.search("\s", phrase))
# find all occurrences of "love" or "2" in the phrase
print(re.findall("love | 2", phrase))
# split the phrase into a list of words using whitespace as the separator, limit to 7 splits
print(re.split("\s", phrase, 7))
# replace whitespace with dashes in the phrase, limit to 3 replacements
print(re.sub("\s", "-", phrase, 3))

# split the phrase into words using whitespace as the separator
split = re.split("\s", phrase)
for s in split:
    # remove leading and trailing spaces from each word
    print(s.strip())

# search for the first word boundary followed by one or more word characters in the phrase
x = re.search(r"\b\w+", phrase)
# print the start and end index of the match
print(x.span())