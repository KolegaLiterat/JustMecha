from modules.zincMechaParser import ZincMechaParser
from modules.mirageShopParser import MirageShopParser


def main():
    # zinc_mecha_mg = ZincMechaParser('mg-1-100')
    # zinc_mecha_hg = ZincMechaParser('rg-1-144')
    mh_shop = MirageShopParser('Perfect-Grade-PG-160')

    # zinc_mecha_products_mg = zinc_mecha_mg.parse_products()
    # zinc_mecha_products_hg = zinc_mecha_hg.parse_products()

    mh_shop.parse_products()


if __name__ == '__main__':
    main()
