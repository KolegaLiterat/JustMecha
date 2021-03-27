import pandas as pd
import os
import pprint as pprint
import click
from modules.localDataCreator import LocalDataCraeator


@click.command()
@click.option('--mecha_name', help='Write a name of mecha model, that you\'re looking for')
@click.argument('mecha_name')
@click.option('--mecha_scale', default='ALL', help='Specify a mecha scale (ALL, HG, RG, MG, PG)')
@click.argument('mecha_scale')
def main(mecha_name, mecha_scale):
    pprint.pprint(f'{mecha_name} {mecha_scale}')


if __name__ == '__main__':
    main()
