from modules.zincMechaParser import ZincMechaParser


def main():
    zinc_mecha = ZincMechaParser('https://www.zincmecha.com/product-category/gunpla/mg-1-100/?swoof=1&stock=instock'
                                 '&really_curr_tax=44-product_cat')
    zinc_mecha.parse_products()

if __name__ == '__main__':
    main()


