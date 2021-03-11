import json
from dataclasses import dataclass
from modules.mirageShopParser import MirageShopParser
from modules.zincMechaParser import ZincMechaParser


@dataclass
class LocalDataCraeator():
    def __init__(self, data_path: str):
        self.data_path = data_path

    def save_data(self):
        pass