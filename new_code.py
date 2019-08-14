import pandas as pd
import numpy as np
import math
from shapely.geometry import Polygon, Point

def eliminatesBasedOnCoordinates(file, columnLat, columnLon, columnVel, latList, lonList):
    L = []
    workshop = Polygon(zip(lonList, latList))

    for _, row in file.iterrows():
        if (not workshop.contains(Point(row[columnLon], row[columnLat]))):
        # if not (row[columnLat] >= minLat and row[columnLat] <= maxLat and \
        #  row[columnLon] >= minLon and row[columnLon] <= maxLon):
            L.append(row)
    newTable = pd.DataFrame(L)
    return newTable
    

path = "C:/Users/Pedro Trabuco/Documents/Universidade/5º Ano/Tese/code/tables/"

# Reads the data from the .csv file and drops unwanted/useless columns
vals = pd.read_csv(path + "tableForHistograms.csv", encoding="utf_8")
print(vals.head())
print("Number of entries on original table: {}".format(len(vals.index)))

# tableForNewMaps = eliminatesBasedOnCoordinates(vals, 1, 2, 10, [38.595816, 38.591677, 38.593568, 38.595730], \
#                                                 [-9.072765, -9.063601, -9.065429, -9.070423])
tableForNewMaps = eliminatesBasedOnCoordinates(vals, 1, 2, 10, \
    [38.5980443, 38.5957342, 38.5951599, 38.5943465, 38.5926735, 38.5921327, 38.5916463, 38.5911851, 38.5907029, 38.5902039, 38.5897091, 38.5892102, 38.5887028, 38.5931933, 38.5955077, 38.5980401, 38.5980443], \
    [-9.0778613, -9.0729153, -9.0716332, -9.0697879, -9.0661454, -9.0649277, -9.0638334, -9.0628356, -9.0618539, -9.0609795, -9.0601212, -9.0592575, -9.0584046, -9.0630341, -9.0675402, -9.0778559, -9.0778613])

print(tableForNewMaps.head())
print(tableForNewMaps.tail())
tableForNewMaps.to_csv(path + "tableForNewMaps2.csv", encoding="utf-8", index=False)

print("DONE!")