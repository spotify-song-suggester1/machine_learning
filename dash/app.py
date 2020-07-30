# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import requests

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
prediction_URL = 'http://spotikay.herokuapp.com/compare'

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# TODO figure out how to get JSON data from spotikay

r = requests.get(prediction_URL).json()
df = pd.read_json(r)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
aa = np.array([df['danceability']]) # danceability
bb = np.array([df['instrumentalness']]) # instrumentalness
cc = np.array([df['loudness']]) # loudness
dd = np.array([df['valence']]) # valence
ee = np.array([df['danceability']]) # danceability again (to "close" graph)

categories = ['danceability', 'instrumentalness', 'loudness', 'valence']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
        r=[aa[0], bb[0], cc[0], dd[0], ee[0]],
        theta=categories,
        fill='toself'
))

fig.update_layout(
    polar=dict(
    radialaxis=dict(
        visible=True,
        range=[0, 1]
    )),
        showlegend=False
)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)