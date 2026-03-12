
# Book Scraper 📚

This project is a Python web scraper that collects book data from the website:
https://books.toscrape.com

The scraper extracts data from all 50 pages of the website and saves it into a CSV file.

## Data Collected

The scraper collects the following information for each book:

- Title
- Price
- Rating

The results are stored in:

data/books.csv

## Technologies Used

- Python
- Requests
- BeautifulSoup
- CSV

## Project Structure

book_scraper/

scraper.py → main scraping script  
requirements.txt → project dependencies  
data/books.csv → scraped data output  

## How to Run the Project

1 Install the dependencies
pip install -r requirements.txt


2 Run the scraper
python scraper.py


3 The scraped data will be saved in:
data/books.csv


## Learning Purpose

This project was created to practice:

- web scraping
- HTML parsing
- Python scripting
- data extraction
- GitHub project management








