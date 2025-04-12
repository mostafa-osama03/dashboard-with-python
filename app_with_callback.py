
from dash import Dash, dcc, html, callback, Input, Output
import plotly.express as px
import pandas as pd


app = Dash(__name__)

df = pd.read_csv('AB_NYC_2019_cleaned.csv')

fig = px.scatter(df, x="latitude", y="longitude", color="neighbourhood_group", size="price",
                 hover_name="neighbourhood",  title="Airbnb Listings in NYC",)
fig.update_layout(
    xaxis=dict(showgrid=False),  # Disable gridlines for x-axis
    yaxis=dict(showgrid=False)   # Disable gridlines for y-axis
)

fig2 = px.pie(df, names='neighbourhood_group', title='Neighbourhood Group Distribution')
fig2.update_traces(textposition='inside', textinfo='percent+label')
fig2.update_layout(showlegend=False)  # Hide legend

fig3 = px.pie(df, names='room_type', title='Room Type Distribution')
fig3.update_traces(textposition='inside', textinfo='percent+label')
fig3.update_layout(showlegend=False)  # Hide legend



app.layout = html.Div([     html.H1(children='Airbnb Listings in NYC'),
                            html.Hr(),
                            html.Div(children=[
                            dcc.Graph(figure=fig ),
                            dcc.RadioItems(
                                            id='radio',
                                            options=[
                                                {'label': 'Neighbourhood Group', 'value': 'neighbourhood_group'},
                                                {'label': 'Room Type', 'value': 'room_type'}
                                            ],
                                            value='neighbourhood_group',
                                            
                                        ),  
                            dcc.Graph(figure={}, id='graph2'),
                        
                            ]),
                        ])


@callback(
    Output('graph2', 'figure'),
    Input('radio', 'value')
)
def update_graph(value):
    if value == 'neighbourhood_group':
        return fig2
    else:
        return fig3
    
        
if __name__ == '__main__':
    app.run(debug=True)
