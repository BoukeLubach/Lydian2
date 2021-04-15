from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
from .dash_apps.dataloader import load_data_csv
from .dash_apps.customgraphscripts import createxy, simpleScatter, timeseries
import plotly.offline as opy
import plotly.graph_objs as go
from os import path
from file_upload.models import Tagmodel
from django.conf import settings
import pandas as pd

def introPageView(request):
    file_path = path.join(path.dirname(__file__), 'dash_apps/data/distillationcolumn_okt.csv')
    df = load_data_csv([file_path])
    

    graph_height = "350px"
 

    
    tagnames = ['Feed flow', 'Reflux flow', 'Reflux temperature', 
            'Hot oil return temperature', 'Reboiler temperature', 
            'Column bottom temperature', 'Hot oil supply temperature', 'Hot oil flow']



    #multiscatterplot
    xygraph = createxy('Feed flow', 'Reflux flow', df)
    graph = xygraph.to_html(full_html=False, config=dict(displayModeBar=False), default_height=graph_height, default_width='100%')

    xygraph = createxy('Feed flow', 'Hot oil flow', df)
    graph2 = xygraph.to_html(full_html=False, config=dict(displayModeBar=False), default_height=graph_height, default_width='100%')

    xygraph = createxy('Feed flow', 'Reflux temperature', df)
    graph3 = xygraph.to_html(full_html=False, config=dict(displayModeBar=False), default_height=graph_height, default_width='100%')

    xygraph = createxy('Reflux flow', 'Hot oil flow', df)
    graph4= xygraph.to_html(full_html=False, config=dict(displayModeBar=False), default_height=graph_height, default_width='100%')
    
    xygraph = createxy('Reflux flow', 'Reflux temperature', df)
    graph5 = xygraph.to_html(full_html=False, config=dict(displayModeBar=False), default_height=graph_height, default_width='100%')

    xygraph = createxy('Hot oil flow', 'Reflux temperature', df)
    graph6 = xygraph.to_html(full_html=False, config=dict(displayModeBar=False), default_height=graph_height, default_width='100%')


    #create simplescatter graph object
    ssgraph = simpleScatter().to_html(full_html=False, config=dict(displayModeBar=False), default_height='400px', default_width='100%')


    #create timeseries graph object
    tsgraph = timeseries().to_html(full_html=False, config=dict(displayModeBar=False), default_height='450px', default_width='100%')

    context = {
        'graph': graph,
        'graph2': graph2,
        'graph3': graph3,
        'graph4': graph4,
        'graph5': graph5,
        'graph6': graph6,
        'tsgraph': tsgraph, 
        'ssgraph': ssgraph,
        
    }

    return render(request, 'kmApps/intro_page.html', context=context)




def kmeans_analysis_view(request):

    available_tags = Tagmodel.objects.all()
    
    context = {
        'available_tags': available_tags,
    }

    if request.method =="POST":

        selected_tagname = request.POST.get('tagselector')
        context['input_field_data'] = selected_tagname
        
        tag = Tagmodel.objects.filter(name=selected_tagname).first()
        file_name = tag.batch.datafile.csvfile.name
        print(file_name)
        file_path = path.join(settings.MEDIA_ROOT, file_name)

        df = pd.read_csv(file_path, sep=';')

        trace1 = go.Scatter(
            x=df.index, 
            y=df[selected_tagname], 
            marker={'color': '#000518', 'size': 6, 'opacity': 0.7},
            mode="markers",  
            name='1st Trace'
        )

        data=go.Data([trace1])
        layout=go.Layout(
            # title="Meine Daten", 
            xaxis={'title': 'xaxis'}, 
            yaxis={'title': 'yaxis'},
            margin=dict(
                t=10,
                l=50,
                b=50,
                r=10
            ))


        fig = go.Figure(data = data, layout=layout)

        tsgraph = fig.to_html(full_html=False, config=dict(displayModeBar=False), default_height='450px', default_width='100%')
        context['tsgraph'] = tsgraph
    
    return render(request, 'kmApps/kmeans_analysis.html', context = context)