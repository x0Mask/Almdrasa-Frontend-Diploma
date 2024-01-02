"""Description: This script scrapes information from a website."""

import requests
from bs4 import BeautifulSoup


# URL of the website to scrape
URL = "https://books.toscrape.com/index.html"

# Sending a GET request to the URL
response = requests.get(URL, timeout=10)

# Checking if the request was successful (status code 200)
if response.status_code == 200:
    # Parsing the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Finding all 'article' elements which contain book information
    books = soup.find_all("article")

    # Iterating through each book
    for book in books:
        # Extracting the title of the book
        title = book.h3.a["title"]

        # Extracting the rating of the book
        ratings = book.p["class"][1]

        # Extracting the product price of the book
        # Using 'select_one' method to target the <p> tag with class 'price_color'
        # Extracting the text content using '.text' or using '.get_text()'
        product_price = book.select_one('p.price_color').text

        # Printing the information of each book
        print(f"Book titled: '{title}' has a rating of: '{ratings}' stars and it costs '{product_price}'.")
else:
    print("Failed to retrieve data. Status code:", response.status_code)