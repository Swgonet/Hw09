import requests
from bs4 import BeautifulSoup


def pars(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('span', class_='text')
    for quote in quotes:
        return quote.text


url = 'https://quotes.toscrape.com/page/1/'

for i in range(1, 10):
    url = f"{url}{i}/"
    print(f"Извлечение цитат с {url}:")
    pars(url)
    print("\n")
