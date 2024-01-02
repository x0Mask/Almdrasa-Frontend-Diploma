import requests

class CurrencyService:
    def __init__(self, api_key):
        self.api_key = api_key

    def list_available_currencies(self):
        response = requests.get(f"http://api.currencylayer.com/list?access_key={self.api_key}")
        data = response.json()
        if data['success']:
            currencies = data['currencies']
            return currencies
        else:
            return None

    def convert_currency(self, from_currency, to_currency, amount):
        response = requests.get(f"http://api.currencylayer.com/convert?access_key={self.api_key}&from={from_currency}&to={to_currency}&amount={amount}")
        data = response.json()
        if data['success']:
            converted_amount = data['result']
            return converted_amount
        else:
            return None
