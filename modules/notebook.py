import datetime as dt
import pandas as pd
import plotly.express as px
from modules.local_data_creator import LocalDataCraeator


def run():
    dataframe = __get_data('data/products.csv')

    __create_box_plot(dataframe)


def __get_data(filename: str):
    local = LocalDataCraeator(filename, False)

    try:
        __is_update_needed()

    except Exception:
        dataframe = __create_dataframe(local, filename)
    else:
        if __is_update_needed():
            local.save_data()
        else:
            dataframe = __create_dataframe(local, filename)


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


def __create_dataframe(save_data_manager, filename) -> pd.DataFrame:
    try:
        dataframe = pd.read_csv(filename)
    except Exception:
        save_data_manager.save_data()
        dataframe = pd.read_csv(filename)

    return dataframe

def __create_box_plot(dataframe):
    fig = px.box(dataframe, x='Shop', y='Price', color="Scale")

    fig.show()
