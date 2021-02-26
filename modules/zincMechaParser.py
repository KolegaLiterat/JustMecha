import requests
from requests.models import Response
from bs4 import BeautifulSoup
from dataclasses import dataclass


@dataclass
class ZincMechaParser:

    def __init__(self, url: str):
        self.url = url

    def parse_products(self):
        products_names: list[str] = []

        response: Response = requests.get(self.url)

        soup: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')

        for summary_wrap in soup.find_all('div', class_='astra-shop-summary-wrap'):
            for product in summary_wrap:
                self.__get_products_names(product, products_names)

    def __get_products_names(self, product: BeautifulSoup, products_names: list[str]):
        name = product.find('h2')

        if name is not None and name != -1:
            products_names.append(name.get_text())
