import json
from dataclasses import dataclass
from modules.mirageShopParser import MirageShopParser
from modules.zincMechaParser import ZincMechaParser


@dataclass
class LocalDataCraeator():
    def __init__(self, data_path: str):
        self.data_path = data_path

    def save_data(self):
        zinch_mecha_scales: list[str] = ["mg-1-00", 'hg-1-144', 'pg-1-60']
        mirage_shop_scales: list[str] = ["High-Grade-HG-1144", 'Real-Grade-RG-1144', 'Master-Grade-MG-1100',
                                         'Perfect-Grade-PG-160']

        try:
            for zinch_mecha_scale in zinch_mecha_scales:
                data = self.__get_zipped_data(zinch_mecha_scale, 'zinch')

                if data is not None:
                    for element in data:
                        print(element)
        except Exception as data_error:
            print(data_error)

    def __get_zipped_data(self, scale: str, shop: str):
        zipped_data = None

        try:
            if shop == 'zinch':
                catalogue = ZincMechaParser(scale)
                zipped_data = catalogue.parse_products()
            elif shop == 'mirage':
                catalogue = MirageShopParser(scale)
                zipped_data = catalogue.parse_products()
        except Exception as data_error:
            print(data_error)
        else:
            return zipped_data
