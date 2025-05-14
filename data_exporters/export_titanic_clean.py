from mage_ai.io.file import FileIO
from pandas import DataFrame
import pandas as pd

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_file(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to filesystem.

    Docs: https://docs.mage.ai/design/data-loading#example-loading-data-from-a-file
    """
    filepath = 'titanic_clean.csv'
    FileIO().export(df, filepath)
    df = pd.read_csv('titanic_clean.csv')
    import os
    print(os.getcwd())
    print(df.head())
