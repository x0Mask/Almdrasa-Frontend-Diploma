def laptop_discount(discount_percent, laptop_price):
    """
    Calculate the discount amount based on the given discount percentage and laptop price.
    """
    return laptop_price * (discount_percent / 100)


discount = laptop_discount(30, 15000)

if discount <= 15000:
    print("The laptop is a good deal")
else:
    print("The laptop isn't a good deal")

# ..................

def multiply_by_five(x):
    """
    Multiply the given number by five.
    """
    return 5 * x

print(multiply_by_five(5))
print(multiply_by_five(6))