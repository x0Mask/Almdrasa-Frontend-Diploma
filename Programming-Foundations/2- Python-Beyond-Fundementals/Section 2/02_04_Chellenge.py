fruits = [
    'apples',
    'bananas',
    'grapes',
    'mangos',
    'nectarines',
    'pears',
    'watermillion',
]

# Print any sentence of your choice.   اطبع أي جملة من اختيارك
# Make for loop, and print each name individually.  واطبع كل اسم حدة for loop قم بعمل 
# After that, Use while loop to print all fruits until you reach nectarines, don't print it. لا تقوم بطباعته nectarines لطباعة كل الفواكة الي ان تصل الي while loop بعد ذالك استخدم 

for fruit in fruits:
    print(fruit)

print("\n*****************")

for fruit in fruits:
    if fruit != "nectarines":
        print(fruit.capitalize())

for fruit in fruits:
    if fruit == "nectarines":
        break 
    print(fruit.upper())


print("\n*****************")
counter = 0;
while fruits[counter] != "nectarines":
    print(fruits[counter])
    counter += 1

print("\n*************")
fruit1 = 0
targetIndex = 4
while fruit1 < targetIndex and fruit1 < len(fruits):
    print(fruits[fruit1])
    fruit1 += 1