def check_day():
    """
    Function to check the day of the week and print a corresponding message.
    """
    today = input("Which day are we on: ").capitalize()

    if today == "Friday":
        # If it is Friday, it's the weekend
        print(today, "is my weekend")
    elif today == "Saturday":
        # If it is Saturday, it's the day to visit my mother
        print(today, "is the day I visit my mother")
    else:
        # For any other day, it's a working day
        print(today, "is a working day")

    print("Thanks!")

check_day()