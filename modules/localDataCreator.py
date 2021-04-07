import datetime as dt
import csv
from dataclasses import dataclass
from modules.mirageShopParser import MirageShopParser
from modules.zincMechaParser import ZincMechaParser


@dataclass
class LocalDataCraeator:
    def __init__(self, data_path: str, is_being_tested: bool):
        self.data_path = data_path
        self.records: list[dict] = []
        self.date: dt = dt.datetime.fromtimestamp(dt.datetime.now().timestamp()).strftime('%d-%m-%Y')
        self.is_being_tested = is_being_tested

    def save_data(self) -> int:
        zinch_mecha_scales: list[str] = ["mg-1-100", 'hg-1-144', 'pg-1-60', 'rg-1-144']
        mirage_shop_scales: list[str] = ["High-Grade-HG-1144", 'Real-Grade-RG-1144', 'Master-Grade-MG-1100',
                                         'Perfect-Grade-PG-160']

        try:
            for zinch_mecha_scale in zinch_mecha_scales:
                data = self.__get_zipped_data(zinch_mecha_scale, 'zinch')

                if data is not None:
                    self.__iterate_over_data(data, zinch_mecha_scale, 'zinch')

            for mirage_shop_scale in mirage_shop_scales:
                data = self.__get_zipped_data(mirage_shop_scale, 'mirage')

                if data is not None:
                    self.__iterate_over_data(data, mirage_shop_scale, 'mirage')

        except Exception as data_error:
            print(data_error)
        else:
            if not self.is_being_tested:
                self.__write_to_file()

            return len(self.records)

    def __get_zipped_data(self, scale: str, shop: str) -> object:
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

    def __get_scale_id(self, mecha_scale) -> str:
        scale_ids = ['MG', 'RG', 'HG', 'PG']
        selected_scale = 'Empty'

        for scale in scale_ids:
            if mecha_scale.find(scale) != -1 or mecha_scale.find(scale.lower()) != -1:
                selected_scale = scale
                break

        return selected_scale

    def __iterate_over_data(self, parsed_data, scale: str, shop: str):
        scale_id = self.__get_scale_id(scale)

        for element in parsed_data:
            self.records.append(self.__create_record(element, scale_id, shop))

    def __create_record(self, mecha_data: str, scale: str, shop) -> dict:
        record: dict = {
            "Mecha": mecha_data[0],
            "Price": mecha_data[1],
            "Seen": self.date,
            "Scale": scale,
            "Shop": shop,
        }

        return record

    def __write_to_file(self):
        with open(self.data_path, mode='a', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=list(self.records[0].keys()), dialect='unix')

            for record in self.records:
                writer.writerow(record)

        self.__save_last_data_parse()

    def __save_last_data_parse(self):
        with open('data/data_save.txt', mode='w') as date_file:
            date_file.write(self.date)
