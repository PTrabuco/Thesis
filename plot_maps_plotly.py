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
        L.append([i/maxVel, "rgb(" + str(r) + ", " + str(g) + ", " + str(b) + ")"])
    return L


init_notebook_mode(connected=True)

path = "C:/Users/Pedro Trabuco/Documents/Universidade/5º Ano/Tese/code/"
df = pd.read_csv(path + "tables/tableForHistograms.csv", encoding="utf-8")

scl = createScale(0, int(round(df["Velocidade real eixo 3 (km/h)"].max())) + 1)

data = [ go.Scattergeo(
        # locationmode = "country names",
        # locations=["Portugal"],
        lon = df["coord_lon"].iloc[::100],
        lat = df["coord_lat"].iloc[::100],
        text = df["Velocidade real eixo 3 (km/h)"].iloc[::100].astype(str) + " km/h",
        mode = "markers",
        marker = dict( 
            color = df["Velocidade real eixo 3 (km/h)"].iloc[::100] / df["Velocidade real eixo 3 (km/h)"].max(),
            colorscale = scl,
            cmin = 0,
            cmax = df["Velocidade real eixo 3 (km/h)"].max(),
            reversescale = True,
            opacity = 0.8,
            size = 3, 
            # autocolorscale = False,
            # symbol = "circle",
            # line = dict(
            #     width=1,
            #     color="rgba(102, 102, 102)"
            # ),
            # colorbar = dict(
            #    thickness = 10,
            #    titleside = "right",
            #    outlinecolor = "rgba(68, 68, 68, 0)",
            #    ticks = "outside",
            #    ticklen = 3,
            #    showticksuffix = "last",
            #    ticksuffix = " inches",
            #    dtick = 0.1
            # )
        )
    )
]

layout = dict(
        geo = dict(
            scope="europe",
            showland=True,
            landcolor = "rgb(212, 212, 212)",
            subunitcolor = "rgb(255, 255, 255)",
            countrycolor = "rgb(255, 255, 255)",
            resolution = 50,  
            projection=dict( type="natural earth"),
            center = dict(
                lat = 38.606248,
                lon = -9.093228
            ),
            # countrywidth = 0.5,
            # subunitwidth = 0.5
        ),
        title = "Trains\' velocity"
    )

fig = go.Figure(data=data, layout=layout)
iplot(fig, filename="test2")

#%%
