#%%
# Extracted from: https://plot.ly/python/scatter-plots-on-maps/

import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
import pandas as pd

def createScale(vel, maxVel):
    # Red 255, 0, 0
    # Yellow 255, 255, 0
    # Green 0, 255, 0
    L = []
    for i in range(vel, maxVel): 
        r = round((1 - i/maxVel) * 255)
        g = round((i/maxVel) * 255)
        b = 0 
        L.append([i/maxVel, 'rgb(' + str(r) + ", " + str(g) + ", " + str(b) + ")"])
    return L

path = 'C:/Users/Pedro Trabuco/Documents/Universidade/5º Ano/Tese/code/'
init_notebook_mode(connected=True)

df = pd.read_csv(path + 'tables/tableForHistograms.csv')
df.head()

scl = createScale(0, int(round(df['Velocidade real eixo 3 (km/h)'].max())))

data = [ go.Scattergeo(
        locationmode = 'country names',
        locations=['Portugal'],
        lon = df['coord_lon'].iloc[::100],
        lat = df['coord_lat'].iloc[::100],
        # text = df['text'],
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
            color = df['Velocidade real eixo 3 (km/h)'] / df['Velocidade real eixo 3 (km/h)'].max(),
            cmax = df['Velocidade real eixo 3 (km/h)'].max(),
            #colorbar=dict(
            #    title="Incoming flights<br>February 2011"
            # )
        ))]

layout = dict(
        title = 'Trains\' velocity', 
        geo = dict(
            scope='europe',
            # projection=dict( type='albers usa' ),
            center = dict(
                lat = 38.606248,
                lon = -9.093228
            ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5,
            resolution = 110       
        ),
    )

fig = go.Figure(data=data, layout=layout )
iplot(fig, filename='test' )

#%%
