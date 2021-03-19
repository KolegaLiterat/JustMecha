import pandas as pd
import os
import pprint as please
from modules.local_data_creator import LocalDataCraeator


def main():
    local = LocalDataCraeator('data/products.csv', False)
    local.save_data()

    dataframe = pd.read_csv('data/products.csv')

    please.pprint(dataframe)


if __name__ == '__main__':
    main()
