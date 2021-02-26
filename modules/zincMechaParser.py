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
        products_prices: list[float] = []

        response: Response = requests.get(self.url)

        soup: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')

        for summary_wrap in soup.find_all('div', class_='astra-shop-summary-wrap'):
            for product in summary_wrap:
                self.__get_product_data('h2', product, products_names)
                self.__get_product_data('span', product, products_prices)

    def __get_product_data(self, field: str, product: BeautifulSoup, data_contatiner: list[str]):
        name = product.find(field)

        if name is not None and name != -1:
            data_contatiner.append(name.get_text())
