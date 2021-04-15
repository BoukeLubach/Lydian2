
import pandas as pd
from .models import Tagmodel, Datafile



def handle_uploaded_file(uploaded_file):
    if uploaded_file.name.endswith('.csv'):

        file_instance = Datafile(status= "file stored", csvfile=uploaded_file)
        
        try:
            create_tagmodels_from_csvfile(uploaded_file, skiprows, dayfirst)
            file_instance.status = "tags processed"
            file_instance.save()

        except:
            file_instance.status = "tags could not be processed"
            file_instance.save()



def process_dataframe(file_pk, skiprows):

    file_object = Datafile.objects.get(id=file_pk)
    df = pd.read_csv(file_object.csvfile.path, encoding='UTF-8', sep=';', skiprows=skiprows)


    for tagname in df.columns:
        # n_datapoints, n_timepoints = check_datacompleteness(df[tagname])
        # average, median, total = get_tagdata_statistics(df[tagname])
        tag_instance = Tagmodel(name=tagname, 
                                csv_filename = file_object.csvfile, 
    #                             # time_points = n_timepoints,
    #                             # data_points = n_datapoints,
    #                             # average = average,
    #                             # median = median, 
    #                             # total = total
                                )
        tag_instance.save()



def create_tagmodels_from_csvfile(csv_file):

    df = pd.read_csv(csv_file, encoding='UTF-8', sep=';', skiprows=skiprows)
    
    df = df.set_index(pd.to_datetime(df['DateTime'], dayfirst=dayfirst))
    df = df.drop(columns = 'DateTime')

    
    for tagname in df.columns:
        
        # n_datapoints, n_timepoints = check_datacompleteness(df[tagname])
        # average, median, total = get_tagdata_statistics(df[tagname])
        tag_instance = Tagmodel(name=tagname, 
                                csv_filename = csv_file, 
    #                             # time_points = n_timepoints,
    #                             # data_points = n_datapoints,
    #                             # average = average,
    #                             # median = median, 
    #                             # total = total
                                )
        tag_instance.save()



def check_datacompleteness(df_serie):
    n_datapoints = df_serie.count()
    n_timepoints = df_serie.index.shape[0]

    return n_datapoints, n_timepoints


def get_tagdata_statistics(df_serie):
    df_serie = pd.to_numeric(df_serie, errors='coerce')
    average = df_serie.mean()
    median = df_serie.median()
    total = df_serie.sum()
    return average, median, total
