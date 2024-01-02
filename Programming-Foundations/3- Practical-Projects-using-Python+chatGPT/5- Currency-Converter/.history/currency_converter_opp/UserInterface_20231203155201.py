from CurrencyConverter import CurrencyConverter

class UserInterface:
    def __init__(self, api_key):
        self.currency_converter = CurrencyConverter(api_key)

    def display_available_currencies(self):
        currencies = self.currency_converter.get_available_currencies()
        if currencies:
            print("Available currencies:")
            for code, name in currencies.items():
                print(f"{code}: {name}")
            return currencies
        else:
            print("Failed to fetch currencies. Please try again.")
            return None

    # Other user input validation methods and interaction can be added here
