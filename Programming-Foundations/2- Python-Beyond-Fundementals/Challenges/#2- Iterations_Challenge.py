# iterations Challange

fruit_list = [
    'apples',
    'bananas',
    'grapes',
    'mangos',
    'nectarines',
    'pears',
    'watermillion',
]

print("List of the fruits we have in the market:")

for fruit in range(len(fruit_list)):
    print(fruit_list[fruit].upper())

print("\n---------------------") 

target_limit = 4
fruit = 0
while fruit <= target_limit and fruit < len(fruit_list):
    print(fruit_list[fruit].capitalize())
    fruit += 1