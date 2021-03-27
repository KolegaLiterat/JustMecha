import datetime as dt
import pandas as pd
import plotly.express as px
from modules.localDataCreator import LocalDataCraeator

local = LocalDataCraeator('data/products.csv', False)


def run():
    dataframe = __get_data()

    __create_box_plot(dataframe)


def __get_data():
    try:
        __is_update_needed()

    except Exception:
        dataframe = __create_dataframe()
    else:
        if __is_update_needed():
            local.save_data()
        else:
            dataframe = __create_dataframe()

    return dataframe


def __is_update_needed() -> bool:
    now = dt.datetime.now()
    is_date_different = True

    with open('data/data_save.txt') as date_file:
        date: str = date_file.readline()

        last_save = dt.datetime.strptime(date, '%d-%m-%Y')

        if last_save.date() == now.date():
            is_date_different = False

    return is_date_different


def __create_dataframe() -> pd.DataFrame:
    header = ['Mecha', 'Price', 'Seen', 'Scale', 'Shop']

    try:
        dataframe = pd.read_csv('data/products.csv', names=header)
    except Exception:
        local.save_data()
        dataframe = pd.read_csv('data/products.csv', names=header)

    return dataframe


def __create_box_plot(dataframe):
    fig = px.box(dataframe, x='Shop', y='Price', color="Scale",
                 title='Shop prices', )

    fig.show()
