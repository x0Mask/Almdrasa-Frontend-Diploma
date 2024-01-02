import requests

api_key = '0648ac95f5d20ffb71046eb6be87a99f'

# Function to fetch and display available currencies
def list_available_currencies():
    response = requests.get(f"http://api.currencylayer.com/list?access_key={api_key}")
    data = response.json()
    if data['success']:
        currencies = data['currencies']
        print("Available currencies:")
        for code, name in currencies.items():
            print(f"{code}: {name}")
        return currencies
    else:
        print("Failed to fetch currencies. Please try again.")
        return None

# Function to validate the entered currency code
def validate_currency(currency, currencies):
    while currency not in currencies:
        print("Invalid currency code. Please choose from the available currencies.")
        currency = input("Enter currency code: ").upper()
    return currency

# Function to perform currency conversion
def convert_currency(from_currency, to_currency, amount):
    response = requests.get(f"http://api.currencylayer.com/convert?access_key={api_key}&from={from_currency}&to={to_currency}&amount={amount}")
    data = response.json()
    if data['success']:
        converted_amount = data['result']
        print(f"{amount} {from_currency} equals {converted_amount} {to_currency}")
    else:
        print("Failed to perform currency conversion. Please try again.")

# Main function
def main():
    currencies = list_available_currencies()
    if currencies:
        from_currency = input("Enter the FROM currency code: ").upper()
        from_currency = validate_currency(from_currency, currencies)

        to_currency = input("Enter the TO currency code: ").upper()
        to_currency = validate_currency(to_currency, currencies)

        amount = 0
        while amount <= 0:
            try:
                amount = float(input("Enter the amount to convert: "))
                if amount <= 0:
                    print("Amount should be greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

        convert_currency(from_currency, to_currency, amount)

if __name__ == "__main__":
    main()
