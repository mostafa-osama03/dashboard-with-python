
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import overview, price_analysis


theme = dbc.themes.MINTY
app = Dash(__name__, external_stylesheets=[theme])

df = pd.read_csv('AB_NYC_2019_cleaned.csv')


app.layout = dbc.Container([    dbc.Row(html.H1(children='Airbnb Listings in NYC' ), className='text-center my-4'),
                                html.Hr(),

                                dbc.Tabs([
                                    dbc.Tab(label='Overview', children=[overview.overview_tab], active_label_style={'color': 'darkblue'}),
                                    
                                    dbc.Tab(label='Price Analysis', children=[price_analysis.price_analysis_tab], active_label_style={'color': 'darkblue'}),

                                ]),
                                
                        ], fluid=True)

if __name__ == '__main__':
    app.run(debug=True)
