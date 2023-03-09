import dash
from dash import dcc
from dash import html
from dash import dash_table
from dash.dash_table.Format import Group 
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

# Define the data that we want to display on the map and table
data = pd.DataFrame({
    'City': ['San Francisco', 'New York', 'Los Angeles'],
    'Lat': [37.7749, 40.7128, 34.0522],
    'Lon': [-122.4194, -74.0060, -118.2437],
    'Population': [884363, 8336817, 3977683]
})

# Define the layout of the app
app.layout = html.Div([
    dcc.Graph(
        id='my-map',
        figure={
            'data': [{
                'type': 'scattermapbox',
                'lat': data['Lat'],
                'lon': data['Lon'],
                'mode': 'markers',
                'marker': {
                    'size': 14
                },
                'text': data['City']
            }],
            'layout': {
                'mapbox': {
                    'accesstoken': 'pk.eyJ1IjoiY3lnbnVzMjYiLCJhIjoiY2s5Z2MzeWVvMGx3NTNtbzRnbGtsOXl6biJ9.8SLdJuFQzuN-s4OlHbwzLg',
                    'center': {'lat': 37.7749, 'lon': -122.4194},
                    'zoom': 4
                },
                'margin': {'l': 0, 'r': 0, 't': 0, 'b': 0},
                'height': 500
            }
        }
    ),
    """"dash_table.DataTable(
        id='my-table',
        columns=[{"name": i, "id": i} for i in data.columns],
        data=data.to_dict('records')
    )"""
])

# Define the callbacks that update the table based on user interactions with the map
@app.callback(
    dash.dependencies.Output('my-table', 'data'),
    [dash.dependencies.Input('my-map', 'clickData')])
def update_table(clickData):
    if clickData is not None:
        city = clickData['points'][0]['text']
        filtered_data = data[data['City'] == city]
        return filtered_data.to_dict('records')
    else:
        return data.to_dict('records')

if __name__ == '__main__':
    app.run(debug=False)
