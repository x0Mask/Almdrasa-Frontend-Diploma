import math
import random
import keyword
import uuid

# Using the integrated modules

# Install modules from PyPI using Pip
# 1. in the terminal we type the command pip3 install packageName
# 2. then we use as usual import moduleName

# The math module provides mathematical functions and constants
# The floor() function returns the largest integer less than or equal to a given number
print(math.floor(2.7))

# The random module provides functions for generating random numbers
# The sqrt() function returns the square root of a given number
# The random() function returns a random float between 0 and 1
print(math.sqrt(random.random()) * 100)

# The sqrt() function returns the square root of a given number
print(math.sqrt(9))

# The pow() function returns the value of a number raised to the power of another number
print(math.pow(3, 3))

# The random module provides functions for generating random numbers
# The randrange() function returns a randomly selected element from a specified range
print(random.randrange(100, 654))

# The random() function returns a random float between 0 and 1
print(random.random())

# The randint() function returns a random integer between the specified range
print(random.randint(1, 13))

# The keyword module provides functions for working with Python keywords
# The iskeyword() function checks if a given string is a Python keyword
print(keyword.iskeyword("if"))
print(keyword.iskeyword("break"))

# The uuid module provides functions for generating universally unique identifiers (UUIDs)
# The uuid1() function generates a UUID from the current time and the MAC address of the computer
print(uuid.uuid1())

# The uuid3() function generates a UUID using the MD5 hash algorithm and a namespace identifier
# Uncomment the line below to use the uuid3() function
# print(uuid.uuid3(uuid.NAMESPACE_DNS, "mo"))
# print(uuid.uuid3("mo", str()))