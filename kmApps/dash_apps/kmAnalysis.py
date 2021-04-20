import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from django_plotly_dash import DjangoDash
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from random import randrange
from .k_means_functions import load_data_csv, cluster_distance, mode_assign
from plotly.subplots import make_subplots
from django_plotly_dash import DjangoDash
from django.conf import settings
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projectMain.settings")
from file_upload.models import Datafile


datafile = Datafile.objects.get(id=4)


file_path = os.path.join(settings.MEDIA_ROOT, datafile.csvfile.name)



df = pd.read_csv(file_path, dayfirst=True, sep=";", skiprows=[1,2])
# df = df.apply(pd.to_numeric, errors="coerce")
df = df.drop(df.columns[0], axis=1)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = DjangoDash('kmAnalysis', external_stylesheets=external_stylesheets)
app_local = dash.Dash()

tags = df.columns

app.layout = html.Div([
            html.Div([
                dcc.Dropdown(
                    id='tag-selection-dropdown',
                    options=[{'label':tag, 'value':tag} for tag in tags],
                    value=[tags[1], tags[2]],
                    multi=True
                ),
            ], id='tag-selection-container', className = 'box'),
            html.Div([
                dcc.Graph(
                    id='cluster-distance-graph',
                    config={'displayModeBar': False},
                ),
            ], id='cluster-distance-container', className='box'),
            # html.Div([
            #     dcc.Dropdown(
            #         id='n-cluster-selection',
            #         options=[{'label': str(i), 'value': str(i) } for i in range(1, 10)],
            #         value = '3'
            #     ),
            # ], id='n-cluster-selection-container', className='box'),

            # html.Div([
            #     dcc.Graph(
            #         id='timeline-graph',
            #         config={'displayModeBar': False}
            #     ),
            #     html.Div(id='mode-table', className="table"),
            # ], id='timeline-graph-container', className = 'box'),

], className='dash-container')



@app.callback(Output('cluster-distance-graph','figure'),
            [Input('tag-selection-dropdown','value'),])
def create_cluster_distance(tags): 
    print("test")
    distance = cluster_distance(df[tags])

    trace = go.Scatter(
        x = list(range(1, len(distance)+1)),
        y = distance
    ) 
    layout = go.Layout(
        xaxis_title="Number of clusters",
        yaxis_title="Sum of distances",
        font=dict(
            family="arial",
            size=16,
        ) 
    )
    fig = go.Figure(data = [trace], layout=layout)

    fig.update_layout(template='none')
    return fig



# @app.callback([Output('timeline-graph','figure'),
#             Output('mode-table', 'children')],
#             [Input('tag-selection-dropdown','value'),
#              Input('n-cluster-selection','value'),])
# def create_timeline_graph(tags, n_clusters):    
#     data = mode_assign(df[tags], int(n_clusters))
#     fig = make_subplots(specs=[[{"secondary_y": True}]])
    
#     for tag in tags:
#         fig.add_trace(go.Scatter(
#             x = data.index,
#             y = data[tag],
#             name = tag
#             ),
#             secondary_y=False,
#         )


#     fig.add_trace(go.Scatter(
#         x = data.index,
#         y = data['Mode'],
#         name = 'Mode'
#         ),
#         secondary_y=True,
#     )
   
#     fig.update_layout(
#         xaxis_title="Time",
#         yaxis_title="Value",
#         height=600,
#         font=dict(
#             family="arial",
#             size=16,
#         ) 
#     )
#     fig.update_layout(template='none')
#     table_data = pd.DataFrame()
#     for i in range(int(n_clusters)):
#         table_data[str(i)] = data[data['Mode'] == i].mean()


#     mode_percentage_list = [data['Mode'][data['Mode'] == i].count()/data.shape[0]*100 for i in range(int(n_clusters))]
#     table_data.loc[int(n_clusters)+1]=mode_percentage_list
#     table_data = table_data.rename({int(n_clusters)+1: 'Perc. of time (%)'}, axis='index')

#     table = generate_table(table_data)

#     return fig, table


# def generate_table(df, max_rows=10):
#     df = df.round(1)
#     df = df.reset_index()
#     table = html.Table(
#                 # Header
#                 [html.Tr([html.Th(col) for col in df.columns])] +
#                 # Body
#                 [html.Tr([html.Td(df.iloc[i][col]) for col in df.columns
#                 ]) for i in range(min(len(df), max_rows))]
#             )

#     return table

if __name__ == '__main__':
#    webbrowser.open('http://localhost:8050/')
    app.run_server(debug=False)
    