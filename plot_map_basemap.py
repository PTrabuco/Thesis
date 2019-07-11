#%%
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

path = "C:/Users/Pedro Trabuco/Documents/Universidade/5º Ano/Tese/code/"
vals = pd.read_csv(path + "tables/tableForHistograms.csv", encoding="utf-8")

# 0. Extract the data that's going to be used
lat = vals["coord_lat"].iloc[::1].values
lon = vals["coord_lon"].iloc[::1].values
vel = vals["Velocidade real eixo 3 (km/h)"].iloc[::1].values

# 1. Draw the map background
fig = plt.figure(figsize=(8, 8))
m = Basemap(resolution='f', llcrnrlon=-9.206494, 
            llcrnrlat=38.500353, urcrnrlon=-8.857752, 
            urcrnrlat=38.757190, epsg=4326)
#http://server.arcgisonline.com/arcgis/rest/services
m.arcgisimage(service="World_Street_Map", xpixels = 3500, verbose=False)

# 2. Scatter velocity data, with color reflecting velocity
m.scatter(lon, lat, latlon=True, c=vel,
          cmap="RdYlGn", alpha=0.5, edgecolors=None)

# 3. Create colorbar, legend and customisation
COLOR = "black"
plt.rcParams["text.color"] = COLOR
plt.rcParams["axes.labelcolor"] = COLOR
plt.rcParams["xtick.color"] =  COLOR
plt.rcParams["ytick.color"] = COLOR
plt.rcParams["font.family"] = "Times New Roman"
cb = plt.colorbar(shrink=0.595)
cb.set_label(label="Velocity (km/h)")
plt.clim(0, 145)
cb.update_ticks()

# 4. Save figure
name = path + "maps/" + \
    "Map showing the velocity of the train in each location"
plt.savefig(name, bbox_inches="tight", dpi=300, transparent=True)