
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd


app = Dash(__name__)
server=app.server
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



app.layout = html.Div([     html.H1(children='Airbnb Listings in NYC', className='title'),
                            html.Hr(),
                            html.Div(children=[
                            dcc.Graph(figure=fig ),
                            dcc.Graph(figure=fig2 ),
                            dcc.Graph(figure=fig3 )
                            ], className='div'),
                        ])

if __name__ == '__main__':
    app.run(port=8080)
