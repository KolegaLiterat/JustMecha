import json
from dataclasses import dataclass
import pprint as please
from modules.mirageShopParser import MirageShopParser
from modules.zincMechaParser import ZincMechaParser


@dataclass
class LocalDataCraeator():
    def __init__(self, data_path: str):
        self.data_path = data_path

    def save_data(self):
        zinch_mecha_scales: list[str] = ["mg-1-100", 'hg-1-144', 'pg-1-60']
        mirage_shop_scales: list[str] = ["High-Grade-HG-1144", 'Real-Grade-RG-1144', 'Master-Grade-MG-1100',
                                         'Perfect-Grade-PG-160']

        try:
            for zinch_mecha_scale in zinch_mecha_scales:
                data = self.__get_zipped_data(zinch_mecha_scale, 'zinch')

                if data is not None:
                    self.__iterate_over_data(data, zinch_mecha_scale, 'zinch')

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
            print(f'{data_error} <==> {scale}')
        else:
            return zipped_data

    def __iterate_over_data(self, parsed_data, scale: str, shop: str):
        for element in parsed_data:
            record = self.__create_record(element, scale, shop)
            self.__append_to_file(record)

    def __create_record(self, mecha_data: str, scale: str, shop):
        record: dict = {
            "Mecha": mecha_data[0],
            "Price": mecha_data[1],
            "Scale": scale,
            "Shop": shop,
        }

        return record

    def __append_to_file(self, data):
        with open(self.data_path, mode='a') as json_file:
            json.dump(data, json_file)
