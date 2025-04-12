import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
import graphs
import pandas as pd

df = pd.read_csv('AB_NYC_2019_cleaned.csv')

price_analysis_tab = dbc.Container([
    dcc.Graph(figure=graphs.avg_price_neigh )
], fluid=True)