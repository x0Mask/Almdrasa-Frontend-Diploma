# For Loop - Capitalize spices
spices = [
    'salt',
    'pepper',
    'cumin',
    'tumeric',
]

for spice in spices:
    capitalizedSpice = str(spice).capitalize()
    print(capitalizedSpice)

print("Mix Ingredients")
print("Done")

print("------------------------------------------------------------------")

# For Loop - Print colors
colorList = [
    "blue",
    "red",
    "green",
    "black"
]

print(colorList[0]) #blue
print(colorList[1]) #red
print(colorList[2]) #green
print(colorList[3]) #black

for color in colorList:
    print(color)

print("------------------------------------------------------------------")

# While Loop - Counting
print("Counting to 33 by threes:")

counter = 3
while counter <= 33:
    print(counter)
    counter += 3

print("------------------------------------------------------------------")

# iterations Challenge - Print fruits
fruits = [
    'apples',
    'bananas',
    'grapes',
    'mangos',
    'nectarines',
    'pears',
    'watermelon',
]

print("List of the fruits we have in the shop")

for fruit in range(len(fruits)):
    print(fruits[fruit])

print("------------------------------------------------------------------")

target_index = 4
fruit = 0
while fruit < target_index and fruit < len(fruits):
    print(fruits[fruit])
    fruit += 1