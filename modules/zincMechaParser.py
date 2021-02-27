import requests
from requests.models import Response
from bs4 import BeautifulSoup
from dataclasses import dataclass
from modules.validator import Validator


@dataclass
class ZincMechaParser:

    def __init__(self, mecha_scale: str):
        self.page = 1
        self.mecha_scale = mecha_scale

    def parse_products(self):
        validator = Validator()

        products_names: list[str] = []
        products_prices: list[str] = []

        url: str = self.__build_url()
        response: Response = requests.get(url)

        while response.status_code == 200:
            soup: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')

            for summary_wrap in soup.find_all('div', class_='astra-shop-summary-wrap'):
                for product in summary_wrap:
                    self.__get_product_data('h2', product, products_names)
                    self.__get_product_data('span', product, products_prices)

            self.page = self.page + 1

            url = self.__build_url()
            response: Response = requests.get(url)

        self.__convert_prices_form_str(products_prices)

        list_validation: list[bool] = [
            validator.zip_check(products_names),
            validator.zip_check(products_prices)
        ]

        if not all(list_validation):
            raise Exception(f'Check product parser!\nProducts: {list_validation[0]}\nPrices: {list_validation[1]}')
        else:
            return zip(products_names, products_prices)

    def __build_url(self) -> str:
        url: str = f'https://www.zincmecha.com/product-category/gunpla/{self.mecha_scale}/page/{self.page}/?swoof=1&stock=instock&really_curr_tax=42-product_cat'

        return url

    def __get_product_data(self, field: str, product: BeautifulSoup, data_contatiner: list[str]):
        name = product.find(field)

        if name is not None and name != -1:
            data_contatiner.append(name.get_text())

    def __convert_prices_form_str(self, product_prices):
        for i in range(len(product_prices)):
            if product_prices[i].find(',') == 1:
                product_prices[i] = product_prices[i].replace(',', '')

            product_prices[i] = float(product_prices[i][:-2])
