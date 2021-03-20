import pandas as pd
import csv
from modules.local_data_creator import LocalDataCraeator

def run():
    __get_data('data/products.csv')

def __get_data(filename: str):
    local = LocalDataCraeator(filename, False)

    try:
        dataframe = pd.read_csv('data/products.csv')

    except Exception:
        print('No file!')
        local.save_data()
    else:
        print('File exist!')