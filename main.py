from modules.mirageShopParser import MirageShopParser
from modules.zincMechaParser import ZincMechaParser


def main():
    zinc_mecha_mg = ZincMechaParser('mg-1-100')
    # zinc_mecha_hg = ZincMechaParser('rg-1-144')
    mh_shop = MirageShopParser('Perfect-Grade-PG-160')

    try:
        zinc_mecha_products_mg = zinc_mecha_mg.parse_products()
    except Exception as parser_error:
        print(parser_error)
    else:
        for element in zinc_mecha_products_mg:
            print(element)


    # zinc_mecha_products_hg = zinc_mecha_hg.parse_products()

    # test = mh_shop.parse_products()
    #
    # dataframe = pd.DataFrame(test)
if __name__ == '__main__':
    main()
