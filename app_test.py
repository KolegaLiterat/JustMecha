import csv
from modules.zincMechaParser import ZincMechaParser
from modules.mirageShopParser import MirageShopParser
from modules.localDataCreator import LocalDataCraeator


def test_zinch_mecha():
    zinch_mecha = ZincMechaParser('mg-1-100')
    zinch_mecha.parse_products()


def test_mirage_shop():
    mirage_shop = MirageShopParser('Perfect-Grade-PG-160')
    mirage_shop.parse_products()


def test_json_file():
    with open('data/products.csv', mode='r') as file:
        reader = csv.reader(file)


def test_data_creation():
    local_data_creator = LocalDataCraeator('data/products.csv', True)
    data = local_data_creator.save_data()

    assert data > 0
