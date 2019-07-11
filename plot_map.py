#%%
# Extracted from: https://www.geeksforgeeks.org/python-plotting-google-map-using-gmplot-package/
# import gmplot package 
import gmplot 
import pandas as pd

path = "C:/Users/Pedro Trabuco/Documents/Universidade/5º Ano/Tese/code/"
vals = pd.read_csv(path + "tables/tableForHistograms.csv", encoding="utf-8")

# Presents 1 entry in every 20
latitude_list = vals["coord_lat"].iloc[::20]
longitude_list = vals["coord_lon"].iloc[::20]
gmap3 = gmplot.GoogleMapPlotter(38.606248, -9.093228, 11) 
  
# scatter method of map object  
# scatter points on the google map 
gmap3.scatter(latitude_list, longitude_list, "# FF0000", size = 40, marker = False ) 
  
gmap3.draw(path + "/maps/map.html") 


#%%
