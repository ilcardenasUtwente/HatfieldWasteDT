from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import geopandas as gpd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = gpd.read_file('../../../../SHP/230313_Containers.shp')


fig = px.bar(df, x="Type", y="Quantity", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hatfield Waste'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=False)