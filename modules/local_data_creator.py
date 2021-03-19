import datetime
import csv
from dataclasses import dataclass
from modules.mirageShopParser import MirageShopParser
from modules.zincMechaParser import ZincMechaParser


@dataclass
class LocalDataCraeator():
    def __init__(self, data_path: str, is_being_tested: bool):
        self.data_path = data_path
        self.records = []
        self.date = datetime.datetime.now()
        self.is_being_tested = is_being_tested

    def save_data(self):
        zinch_mecha_scales: list[str] = ["mg-1-100", 'hg-1-144', 'pg-1-60']
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
            self.records.append(self.__create_record(element, scale, shop))

    def __create_record(self, mecha_data: str, scale: str, shop):
        record: dict = {
            "Mecha": mecha_data[0],
            "Price": mecha_data[1],
            "Seen": datetime.datetime.fromtimestamp(self.date.timestamp()).strftime('%d-%m-%y'),
            "Scale": scale,
            "Shop": shop,
        }

        return record

    def __write_to_file(self):
        with open(self.data_path, mode='a', newline='') as csv_file:
            header: list[str] = list(self.records[0].keys())

            writer = csv.DictWriter(csv_file, fieldnames=header, dialect='unix')
            writer.writeheader()

            for record in self.records:
                writer.writerow(record)