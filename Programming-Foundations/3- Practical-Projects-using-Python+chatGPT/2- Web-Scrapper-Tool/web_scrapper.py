"""Description: This script scrapes information from a website."""

import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/index.html"

response = requests.get(URL, timeout=10)
print(response.status_code)

if (response.status_code == 200):
    soup = BeautifulSoup(response.content, "html.parser")

    books = soup.find_all("article")

    for book in books:
        title = book.h3.a["title"]
        ratings = book.p["class"][1]
        # To get the text content for the <p> tag, we can use '.text' method or '.get_text()'
        product_price = book.select_one('p.price_color').text
        print(f"Book titled: '{title}' has a rating of: '{ratings}' stars and it costs '{product_price}'.")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
