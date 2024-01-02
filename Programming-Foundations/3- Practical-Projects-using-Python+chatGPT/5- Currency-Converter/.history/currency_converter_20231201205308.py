import requests

API_KEY = "78b94eac90aa85c7805bc8d7dacf2a61"
FROM = str(input("Insert the initial currency: "))
TO = str(input("Insert the target currency: "))
AMOUNT = float(input("Insert the amount: "))

URL = f'http://data.fixer.io/api/convert?access_key={API_KEY}&from={FROM}&to={TO}&amount={AMOUNT}'
response = requests.get(URL, timeout=10)

if response.status_code == 200:
    result = response.json()
    converted_amount = result["result"]
    print(f"{AMOUNT} {FROM} is approximately = {converted_amount} {TO}")
else:
    print("Failed to fetch data. Check your API key or try again later.")
