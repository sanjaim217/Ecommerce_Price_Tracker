import requests
from bs4 import BeautifulSoup
import re

def get_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    price_tag = soup.find("p", class_="price_color")

    if price_tag is None:
        return 0.0

    price_text = price_tag.get_text()

    # Extract only numbers and decimal point
    price_numbers = re.findall(r"\d+\.\d+", price_text)

    if not price_numbers:
        return 0.0

    return float(price_numbers[0])
