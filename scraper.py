import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

file = open("data/updated_books.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(file)

writer.writerow(["Title", "Price", "Rating","Link","Image Link","Availability"])

for page in range(1, 51):

    print(f"Scraping page {page}")

    url = BASE_URL.format(page)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.find("p", class_="star-rating")["class"][1]
        link=book.h3.a["href"]
        image_link=book.find("img")["src"]
        availability=book.find("p", class_="availability").text.strip()

        writer.writerow([title, price, rating, link, image_link, availability])

file.close()

print("Scraping finished. Data saved.")
