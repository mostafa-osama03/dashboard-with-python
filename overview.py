import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
import graphs
import pandas as pd

df = pd.read_csv('AB_NYC_2019_cleaned.csv')

overview_tab = dbc.Container([
    dbc.Row([
                                    dbc.Col(dbc.Card(
                                    dbc.CardBody(children=[
                                        html.H3(children='Total Listings', className='text-center'),
                                        html.H4(children=f'{df.shape[0]:,}', className='text-center')
                                    ])),),
                                    dbc.Col(dbc.Card(
                                    dbc.CardBody(children=[
                                        html.H3(children='Total Neighbourhoods', className='text-center'),
                                        html.H4(children=df.neighbourhood.nunique(), className='text-center')
                                    ])),),
                                    dbc.Col(dbc.Card(
                                    dbc.CardBody(children=[
                                        html.H3(children='Room Types', className='text-center'),
                                        html.H4(children=df.room_type.nunique(), className='text-center')
                                    ])),),
                                  
                                ]),
                                
                            
                        
                        
                                html.Div(children=[
                                            dcc.Graph(figure=graphs.geograph_scatter ),
                                            dbc.Row([
                                                dbc.Col(dcc.Graph(figure=graphs.neigh_pie )),
                                                dbc.Col(dcc.Graph(figure=graphs.room_pie ))
                                                    ])
                                        
                                            ]),

], fluid=True)