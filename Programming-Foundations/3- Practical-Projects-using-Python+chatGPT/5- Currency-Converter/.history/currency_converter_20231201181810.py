import requests

API_KEY = "24a1b9c7559814993ec152285ebba64b"
URL = f'http://data.fixer.io/api/converter?access_key={API_KEY}'

response = requests.get(URL, timeout=10)


if response.status_code == "200":
    FROM = str(input("Insert the initial currency: "))
    TO = str(input("Insert the target currency: "))
    amount = int(input("Insert the amount: "))
