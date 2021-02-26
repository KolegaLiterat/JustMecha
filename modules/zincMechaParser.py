import requests
from requests.models import Response
from bs4 import BeautifulSoup
from dataclasses import dataclass



@dataclass
class ZincMechaParser:

    def __init__(self, url: str):
        self.url = url

    def parse_products(self):
        response: Response = requests.get(self.url)

        soup: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')

        for product in soup.find_all('div', class_='astra-shop-summary-wrap'):
            for element in product:
                title = element.find('h2')

                if title != None and title != -1:
                    print(title.get_text())