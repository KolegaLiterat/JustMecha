from modules.zincMechaParser import ZincMechaParser


def main():
    zinc_mecha_mg = ZincMechaParser('mg-1-100')
    zinc_mecha_hg = ZincMechaParser('hg-1-144')

    zinc_mecha_products_mg = zinc_mecha_mg.parse_products()
    zinc_mecha_products_hg = zinc_mecha_hg.parse_products()

    for mecha_mg in zinc_mecha_products_mg:
        print(mecha_mg)

    for mecha_hg in zinc_mecha_products_hg:
        print(mecha_hg)

if __name__ == '__main__':
    main()


