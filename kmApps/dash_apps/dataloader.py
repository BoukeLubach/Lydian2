
import pandas as pd
import numpy as np


def load_data_csv(filenames):
    """takes csv filesnames and returns dataframe with datetime index and tagcolum names"""
    dataframe = pd.DataFrame()

    for filename in filenames:
        df = pd.read_csv(filename, sep=';', skiprows=[1,2])
        df = df.set_index(pd.to_datetime(df['Datetime'], dayfirst=True))
        df = df.drop(df.columns[0], axis=1)
        df = df[0:8760]
        if dataframe.empty: 
            dataframe = df
        else: 
            dataframe = dataframe.merge(df, left_index=True, right_index=True)

    return dataframe
