import pandas as pd
import datetime as dt
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
        filtered_data: pd.DataFrame = dataframe[dataframe['Mecha'].str.contains(mecha_name, case=False)]

        mechas: pd.DataFrame = filtered_data.drop_duplicates(keep='last').sort_values('Seen', ascending=True)

        return mechas.reset_index(drop=True)

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
