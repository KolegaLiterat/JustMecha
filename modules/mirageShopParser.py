import requests
from requests.models import Response
from bs4 import BeautifulSoup
from dataclasses import dataclass


@dataclass
class MirageShopParser:

    def __init__(self, mecha_scale: str):
        self.page = 1
        self.mecha_scale = mecha_scale

    def parse_products(self):
        products_names: list[str] = []

        url: str = self.__build_url()
        response: Response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')
        self.__get_products_names(soup, products_names)

        print(products_names)

    def __build_url(self) -> str:
        url: str = 'empty'

        shop_urls: list[str] = [
            f'https://www.mhshop.pl/pl/c/High-Grade-HG-1144/249/1/default/1/f_availability_2/{self.page}',
            f'https://www.mhshop.pl/pl/c/Master-Grade-MG-1100/17/1/default/1/f_availability_2/{self.page}'
        ]

        for link in shop_urls:
            if link.find(self.mecha_scale) != -1:
                url: str = link
                break

        return url

    def __get_products_names(self, soup, data_container: list[str]):
        for product_row in soup.find_all('a', class_='prodname f-row'):
            data_container.append(product_row.get('title'))