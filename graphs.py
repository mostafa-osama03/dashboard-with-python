import plotly.express as px
import pandas as pd


df = pd.read_csv('AB_NYC_2019_cleaned.csv')

# Scatter plot for Longitude vs Latitude
geograph_scatter = px.scatter(df, x="latitude", y="longitude", color="neighbourhood_group", size="price",
                 hover_name="neighbourhood",  title="Airbnb Listings in NYC",
                 template="presentation")
geograph_scatter.update_layout(
    xaxis=dict(showgrid=False),  # Disable gridlines for x-axis
    yaxis=dict(showgrid=False)   # Disable gridlines for y-axis
)

# Pie charts for Neighbourhood Group 
neigh_pie = px.pie(df, names='neighbourhood_group', title='Neighbourhood Group Distribution', template="presentation", hole=0.3)
neigh_pie.update_traces(textposition='inside', textinfo='percent+label')
neigh_pie.update_layout(showlegend=False)  # Hide legend

# Pie charts for Room Type
room_pie = px.pie(df, names='room_type', title='Room Type Distribution',
                  template="presentation", hole=0.3)
room_pie.update_traces(textposition='inside', textinfo='percent+label')
room_pie.update_layout(showlegend=False)  # Hide legend


# Avg Price by Neighbourhood Group
avg_price_neigh = px.bar(df, x="neighbourhood_group", y="price", color="neighbourhood_group", title="Average Price by Neighbourhood Group", template="presentation")
avg_price_neigh.update_layout(xaxis_title="Neighbourhood Group", yaxis_title="Average Price", showlegend=False)