import plotly.graph_objs as go
from os import path
from .dataloader import load_data_csv



def timeseries():				
    file_path = path.join(path.dirname(__file__), 'data/distillationcolumn_okt.csv')
    df = load_data_csv([file_path])

    layout=go.Layout(
        xaxis={'title': 'Time'}, 
        yaxis={'title': ''},
    )

    fig = go.Figure(layout=layout)

    y1_tags = ['Feed flow', 'Reflux flow', 'Hot oil flow']
    y2_tags = ['Reflux temperature', 'Hot oil return temperature', 'Reboiler temperature', 
            'Column bottom temperature', 'Hot oil supply temperature', ]


    for tag in y1_tags:
        fig.add_trace(go.Scatter(
            x=df.index,
            y=df[tag], 
            mode="lines",  
            name=tag
        ))

    for tag in y2_tags:
        fig.add_trace(go.Scatter(
            x=df.index,
            y=df[tag], 
            mode="lines",  
            name=tag,
            yaxis="y2"
        ))

    fig.update_layout(
            yaxis=dict(
                title="Flow (kg/h)",
                titlefont=dict(
                    color="#000518"
                ),
                tickfont=dict(
                    color="#000518"
                )
            ),
            yaxis2=dict(
                title="Temperature (°C)",
                titlefont=dict(
                    color="#ED553B"
                ),
                tickfont=dict(
                    color="#ED553B"
                ),
                anchor="free",
                overlaying="y",
                side="right",
                position=1
            ),
                legend=dict(
                y=1,
                # xanchor="right",
                x=1.2
            ))

 
    return fig



def simpleScatter():

    file_path = path.join(path.dirname(__file__), 'data/distillationcolumn_okt.csv')
    df = load_data_csv([file_path])

    trace1 = go.Scatter(
        x=df['Feed flow'], 
        y=df['Reflux flow'], 
        marker={'color': '#000518', 'size': 6, 'opacity': 0.7},
        mode="markers",  
        name='1st Trace'
    )

    data=go.Data([trace1])
    layout=go.Layout(
        # title="Meine Daten", 
         xaxis={'title': 'Feed flow'}, 
         yaxis={'title': 'Reflux'},
         margin=dict(
             t=10,
             l=50,
             b=50,
             r=10
         ))


    fig = go.Figure(data = data, layout=layout)

    return fig


def createxy(x, y, df):

    trace1 = go.Scatter(
        x=df[x], 
        y=df[y], 
        marker={'color': '#000518', 'size': 6, 'opacity':0.7},
        mode="markers",  
        name='1st Trace'
    )

    data=go.Data([trace1])
    layout=go.Layout(
        # title="Meine Daten", 
         xaxis={'title': f'{x}'}, 
         yaxis={'title': f'{y}'},
         margin=dict(
             t=10,
             l=50,
             b=50,
             r=10
         ))


    fig = go.Figure(data = data, layout=layout)

    return fig

