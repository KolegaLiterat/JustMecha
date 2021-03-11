from modules.zincMechaParser import ZincMechaParser
from modules.mirageShopParser import MirageShopParser


def test_zinch_mecha():
    zinch_mecha = ZincMechaParser('mg-1-100')
    zinch_mecha.parse_products()

def test_mirage_shop():
    mirage_shop = MirageShopParser('Perfect-Grade-PG-160')
    mirage_shop.parse_products()

