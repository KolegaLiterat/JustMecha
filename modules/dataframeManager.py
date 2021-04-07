import pandas as pd
import datetime as dt
import pprint as pprint
from dataclasses import dataclass
from modules.localDataCreator import LocalDataCraeator


@dataclass
class DataframeManager(LocalDataCraeator):

    def __init__(self, data_path: str, is_being_tested: bool):
        super().__init__(data_path, is_being_tested)

    def get_data(self):
        try:
            self.__is_update_needed()

        except Exception:
            dataframe = self.__create_dataframe()
        else:
            if self.__is_update_needed():
                self.save_data()
            else:
                dataframe = self.__create_dataframe()

        return dataframe

    def get_mechas_without_scale(self, dataframe: pd.DataFrame, mecha_name: str) -> pd.DataFrame:
        mechas: pd.DataFrame = self.__filter_data_by_mecha_name(dataframe, mecha_name)

        return mechas.reset_index(drop=True)

    def get_mechas_with_scale(self, dataframe: pd.DataFrame, mecha_name: str, mecha_scale: str) -> pd.DataFrame:
        filtered_data_by_scale = dataframe.loc[dataframe['Scale'] == mecha_scale]

        mechas = self.__filter_data_by_mecha_name(filtered_data_by_scale, mecha_name)

        return mechas.reset_index(drop=True)

    def get_lowest_price(self, dataframe):
        lowest_price: int = dataframe['Price'].min()

        filtered_by_price: pd.DataFrame = dataframe.loc[dataframe['Price'] == lowest_price]
        vendor = pd.unique(filtered_by_price['Shop'])
        scale = pd.unique(filtered_by_price['Scale'])

        pprint.pprint(f"Lowest price is {lowest_price}. Scale: {scale}. Can be found in {vendor}")

    def __is_update_needed(self) -> bool:
        now = dt.datetime.now()
        is_date_different = True

        with open('data/data_save.txt') as date_file:
            date: str = date_file.readline()

            last_save = dt.datetime.strptime(date, '%d-%m-%Y')

            if last_save.date() == now.date():
                is_date_different = False

        return is_date_different

    def __create_dataframe(self) -> pd.DataFrame:
        header = ['Mecha', 'Price', 'Seen', 'Scale', 'Shop']

        try:
            dataframe = pd.read_csv(self.data_path, names=header)
        except Exception:
            self.save_data()
            dataframe = pd.read_csv(self.data_path, names=header)

        return dataframe

    def __filter_data_by_mecha_name(self, dataframe: pd.DataFrame, mecha_name: str):
        filtered_data: pd.DataFrame = dataframe[dataframe['Mecha'].str.contains(mecha_name, case=False)]

        return filtered_data.drop_duplicates(subset='Mecha', keep='last').sort_values('Seen', ascending=True)