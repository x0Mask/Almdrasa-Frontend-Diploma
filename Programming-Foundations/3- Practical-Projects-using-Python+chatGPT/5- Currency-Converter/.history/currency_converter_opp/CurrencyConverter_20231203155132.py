from CurrencyService import CurrencyService

class CurrencyConverter:
    def __init__(self, api_key):
        self.currency_service = CurrencyService(api_key)

    def get_available_currencies(self):
        currencies = self.currency_service.list_available_currencies()
        if currencies:
            return currencies
        else:
            return None

    def validate_currency(self, currency, currencies):
        while currency not in currencies:
            print("Invalid currency code. Please choose from the available currencies.")
            currency = input("Enter currency code: ").upper()
        return currency

    def convert_currency(self, from_currency, to_currency, amount):
        converted_amount = self.currency_service.convert_currency(from_currency, to_currency, amount)
        return converted_amount
