import requests
from requests.models import Response
from bs4 import BeautifulSoup
from dataclasses import dataclass
from modules.validator import Validator



@dataclass
class MirageShopParser:

    def __init__(self, mecha_scale: str):
        self.page = 1
        self.mecha_scale = mecha_scale

    def parse_products(self):
        validator = Validator()

        products_names: list[str] = []
        products_prices: list[str] = []

        url: str = self.__build_url()
        response: Response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')
        self.__get_products_names(soup, products_names)
        self.__get_products_prices(soup, products_prices)

        self.__convert_prices_from_str(products_prices)

        if not validator.list_validation(products_names, products_prices):
            raise Exception(f'Check product parser for Zinch Mecha!!')
        else:
            return zip(products_names, products_prices)

    def __build_url(self) -> str:
        url: str = 'empty'

        shop_urls: list[str] = [
            f'https://www.mhshop.pl/pl/c/High-Grade-HG-1144/249/1/default/1/f_availability_2/{self.page}',
            f'https://www.mhshop.pl/pl/c/Master-Grade-MG-1100/17/1/default/1/f_availability_2/{self.page}',
            f'https://www.mhshop.pl/pl/c/Perfect-Grade-PG-160/18/1/default/1/f_availability_2/{self.page}'
        ]

        for link in shop_urls:
            if link.find(self.mecha_scale) != -1:
                url: str = link
                break

        return url

    def __get_products_names(self, soup, data_container: list[str]):
        for product_row in soup.find_all('a', class_='prodname f-row'):
            data_container.append(product_row.get('title'))

    def __get_products_prices(self, soup, data_container: list[str]):
        for price_row in soup.find_all('div', class_='price f-row'):
            data_container.append(price_row.find('em').get_text())

    def __convert_prices_from_str(self, products_prices: list[str]):
        for i in range(len(products_prices)):
            products_prices[i] = products_prices[i].replace(u'\xa0', '')[:-2]
            products_prices[i] = float(products_prices[i].replace(',', '.'))
