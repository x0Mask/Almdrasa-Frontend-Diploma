fruits = [
    'apples',
    'bananas',
    'grapes',
    'mangos',
    'nectarines',
    'pears',
    'watermillion',
]


print("I love these fruits!")
for fruit in fruits:
    print(fruit.capitalize())

#-----------------------------------------------
counter = 0;
while fruits[counter] != "nectarines":
    print(fruits[counter])
    counter += 1


for fruit in fruits:
    if fruit != "nectarines":
        print(fruit.capitalize())

# for fruit in fruits:
#     if fruit == "nectarines":
#         break
#     print(fruit.capitalize())