import pandas as pd
import os
import pprint as pprint
import click
from modules.dataframeManager import DataframeManager


@click.command()
@click.option('--mecha_name', help='Write a name of mecha model, that you\'re looking for')
@click.argument('mecha_name')
# @click.option('--mecha_scale', default='ALL', help='Specify a mecha scale (ALL, HG, RG, MG, PG)')
# @click.argument('mecha_scale')
def main(mecha_name):
    df_manager = DataframeManager()

    pprint.pprint(f'{mecha_name}')


if __name__ == '__main__':
    main()
