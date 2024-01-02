def check_temp(temp):
    """
    Check the temperature and print a message based on the temperature range.

    Args:
        temp (int): The temperature to check.

    Returns:
        None
    """
    if temp < 15:
        # Temperature is less than 15 degrees Celsius
        print('Bring a jacket')
    elif temp > 25 and temp <= 35:
        # Temperature is between 26 and 35 degrees Celsius
        print('Pack a jacket')
    elif temp > 35:
        # Temperature is greater than 35 degrees Celsius
        print('Leave the jacket at home')

# Making the Test Cases
check_temp(10)
check_temp(30)
check_temp(37)