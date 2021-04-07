import pandas as pd
import os
import pprint as pprint
import click
from modules.dataframeManager import DataframeManager


@click.command()
@click.option('--mecha_name', help='Write a name of mecha model, that you\'re looking for')
@click.argument('mecha_name')
@click.option('--mecha_scale', help='Specify a mecha scale (ALL, HG, RG, MG, PG)')
@click.argument('mecha_scale')
def main(mecha_name, mecha_scale):
    df_manager = DataframeManager(data_path='data/products.csv', is_being_tested=False)

    dataframe = df_manager.get_data()

    if mecha_scale == 'ALL':
        mechas = df_manager.get_mechas_without_scale(dataframe, mecha_name)

        if len(mechas) == 0:
            click.echo(click.style('Mecha not found!', fg='red'))
        else:
            click.echo(mechas)
    else:
        mechas = df_manager.get_mechas_with_scale(dataframe, mecha_name, mecha_scale)

        if len(mechas) == 0:
            click.echo(click.style('Mecha not found!', fg='red'))
        else:
            click.echo(mechas)


if __name__ == '__main__':
    main()
