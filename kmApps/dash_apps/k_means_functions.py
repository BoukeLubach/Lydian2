
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler


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

def cluster_distance(df):
    """takes dataframe with tagvalues and returns sum of cluster distance for 1-9 clusters"""

    #cutoff datetime column and normalize data
    X = df.iloc[:,1:].values
    scaler = MinMaxScaler()
    x = scaler.fit_transform(X)

    #determine total distance for kmeans clusters
    sse = []
    list_k = list(range(1, 10))
    for k in list_k:
        km = KMeans(n_clusters=k)
        km.fit(x)
        sse.append(km.inertia_)
    return sse


def mode_assign(df, n_modes):
    """Takes dataframe and number of modes, assigns mode for each row in dataframe (assumed timepoint)
    returns dataframe with assigned mode to every row in a new column 'mode'   """
    X = df.iloc[:,1:].values
    scaler = MinMaxScaler()
    x = scaler.fit_transform(X)

    km_model = KMeans(n_clusters=n_modes)
    km_model.fit(x)
    km_model.cluster_centers_
    Y = []
    
    for k in range(x.shape[0]):
        sample_test=np.array(x[k,:])
        reshaped_test=sample_test.reshape(1, -1)
        value = km_model.predict(reshaped_test)[0]
        Y.append(value)
        

    df_modes = pd.DataFrame(Y, columns=['Mode'])
    df_modes = df_modes.set_index(df.index)
    
    df = pd.concat([df,df_modes], axis=1)

    return df
