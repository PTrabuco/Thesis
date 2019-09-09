#%%
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

path = "C:/Users/Pedro Trabuco/Documents/Universidade/5º Ano/Tese/code/"
table = "tableForNewMaps2.csv"
vals = pd.read_csv(path + "tables/" + table, encoding="utf-8")
column = "Tensão Catenária (Veff)"
title = "Map showing the catenary's tension in each location_final".replace(" ", "_")
# title = "Map showing where skating happened " + table.replace(".csv", "").split('_', 1)[-1]
labelText = "Voltage (VRMS)"

# 0. Extract the data that's going to be used
lat = vals["coord_lat"].iloc[::1].values
lon = vals["coord_lon"].iloc[::1].values
vel = vals[column].iloc[::1].values
print(vals[column].max())

# 1. Draw the map background
fig = plt.figure(figsize=(8, 8))
m = Basemap(resolution='f', llcrnrlon=-9.206494,
            llcrnrlat=38.500353, urcrnrlon=-8.857752,
            urcrnrlat=38.757190, epsg=4326)
# Close up coordinates bellow
# m = Basemap(resolution='f', llcrnrlon=-9.091603, 
#            llcrnrlat=38.580480, urcrnrlon=-9.045267, 
#            urcrnrlat=38.607951, epsg=4326)
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
plt.clim(0, 26440)
cb = plt.colorbar(shrink=0.595)
cb.set_label(label=labelText)
# plt.clim(0, 255)
# cb.update_ticks()
cb.minorticks_off()
cb.update_ticks()

# For title
# csfont = {"fontname":"Times New Roman"}
# plt.title(title,**csfont)

# 4. Save figure
name = path + "maps/" + title
plt.savefig(name, bbox_inches="tight", dpi=300, transparent=True)