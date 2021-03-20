import datetime as dt
import pandas as pd
from modules.local_data_creator import LocalDataCraeator

def run():
    __get_data('data/products.csv')

def __get_data(filename: str):
    local = LocalDataCraeator(filename, False)

    try:
        __is_update_needed()

    except Exception:
        print('No file!')
        # local.save_data()
    else:
        if __is_update_needed():
            local.save_data()
        else:
            dataframe = pd.read_csv(filename)
            display(dataframe)

def __is_update_needed() -> bool:
    now = dt.datetime.now()
    is_date_different = True

    with open('data/data_save.txt') as date_file:
        date: str = date_file.readline()

        last_save = dt.datetime.strptime(date, '%d-%m-%Y')

        if last_save.date() == now.date():
            is_date_different = False

    return is_date_different
