from modules.local_data_creator import LocalDataCraeator


def main():
    local = LocalDataCraeator('data/products.json')

    local.save_data()


if __name__ == '__main__':
    main()
