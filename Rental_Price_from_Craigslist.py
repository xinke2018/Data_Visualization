# import libraries
import numpy as np
import pandas as pd import plotly
import plotly.plotly as py# import dataraw_data = pd.read_csv('data.csv') raw_data.head() raw_data.describe() raw_data.isnull().sum()# deal with mis-recorded datadata = raw_data[raw_data['price']>100]data_plot = data[['latitude','longitude', 'price', 'bedrooms','bathrooms']].copy()df = data_plot.dropna()# Get the interactive plot with can show each roome's price, number of bedroom and number of bathroomdf['text'] = df['bedrooms'].astype(str) + 'bed, ' + df['bathrooms'].astype(str) + \
             'bath, '+ 'price:'+ df['price'].astype(str)

scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
      [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]

data = [ dict(
        type = 'scattergeo',
        locationmode = 'ISO-3',
        lon = df['longitude'],
        lat = df['latitude'],
        text = df['text'],
        mode = 'markers',
        marker = dict(
            size = 8,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = scl,
            cmin = 0,
            color = df['price'],
            cmax = 3500,
            colorbar=dict(
                title="Price"
            )
        ))]


layout = dict(
        title = 'Room Rental Price from Craigslist',
        colorbar = True,
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ),
    )

fig = dict( data=data, layout=layout )
plotly.offline.plot( fig, validate=False, filename='d3-houseprice' )
