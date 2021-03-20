import datetime
import pandas as pd
from modules.local_data_creator import LocalDataCraeator

def run():
    __get_data('data/products.csv')

def __get_data(filename: str):
    local = LocalDataCraeator(filename, False)

    try:
        __get_last_save_date()

    except Exception:
        print('No file!')
        # local.save_data()
    else:
        print('File exist!')

def __get_last_save_date():
    last_save = "EMPTY"

    with open('data/data_save.txt') as date_file:
        date: str = date_file.readline()

        print(date)