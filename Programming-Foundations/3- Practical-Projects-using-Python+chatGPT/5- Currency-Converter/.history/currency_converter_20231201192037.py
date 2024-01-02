import requests

API_KEY = "24a1b9c7559814993ec152285ebba64b"
FROM = str(input("Insert the initial currency: "))
TO = str(input("Insert the target currency: "))
URL = f'http://data.fixer.io/api/converter?access_key={API_KEY}&from={FROM}&to={TO}&amount={AMOUNT}'
response = requests.get(URL, timeout=10)


