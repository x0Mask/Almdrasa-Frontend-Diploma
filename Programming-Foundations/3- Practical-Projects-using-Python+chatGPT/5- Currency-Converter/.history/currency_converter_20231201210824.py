import requests

API_KEY = "0648ac95f5d20ffb71046eb6be87a99f"
FROM = str(input("Insert the initial currency: ")).upper()
TO = str(input("Insert the target currency: ")).upper()
AMOUNT = float(input("Insert the amount: "))

URL = f'http://data.fixer.io/api/convert?access_key={API_KEY}&from={FROM}&to={TO}&amount={AMOUNT}'
response = requests.get(URL, timeout=10)

if response.status_code == 200:
    result = response.json()
    if result['success']:
        converted_amount = result['result']
        print(f"{AMOUNT} {FROM} is approximately: {converted_amount} {TO}")
    else:
        print(f"Conversion failed: {result['error']['info']}")
else:
    print("Failed to fetch data. Check your API key or try again later.")
