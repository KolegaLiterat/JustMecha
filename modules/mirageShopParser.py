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
        url: str = self.__build_url()

        print(url)

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
