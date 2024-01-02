import requests

api_key = "24a1b9c7559814993ec152285ebba64b"
url = f'http://data.fixer.io/api/converter?access_key={api_key}'

response = requests.get(url)


if response.status_code == "200":
    print("conversion successful")