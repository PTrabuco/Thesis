import pandas as pd
import numpy as np
import math


# Cleans all the entries with binary strings on file "file" and 
# column "columnWithBinaries"
def cleanBinaries(file, columnWithBinaries):
    L = []
    for _, row in file.iterrows():
        if (not row[columnWithBinaries][0].isdigit()) or (row[columnWithBinaries][0] != '0' and \
        row[columnWithBinaries][0] != '1' and row[columnWithBinaries][1] != '0' and row[columnWithBinaries][1] != '1'):
            L.append(row)
    newTable = pd.DataFrame(L)
    return newTable

# Creates columns from column "column" from file "file", where the columns have 
# the names "names"
def createColumnsWithValues(file, column, names):
    L = [names]
    for _, row in file.iterrows():
        if row[column][0].isdigit():
            L.append(row[column].replace('\"', '').split(';'))
        else:
            L.append([np.NaN] * len(names))
    LToDataframe = pd.DataFrame(L[1:], columns=L[0])
    newTable = pd.concat([file.reset_index(drop=True), LToDataframe.reset_index(drop=True)], axis=1, sort=False)
    return newTable

# Creates columns from column "column" from file "file", where the columns have 
# the names "names", where the value in the row of the new column will be 0 if the 
# corresponding value on column "column" is equal to "valueCondition", otherwise 1
def createColumnsWithValuesCondition(file, column, valueCondition, names):
    L = [names]
    for _, row in file.iterrows():
        if row[column] == valueCondition:
            L.append(0)
        else:
            L.append(1)
    LToDataframe = pd.DataFrame(L[1:], columns=L[0])
    newTable = pd.concat([file.reset_index(drop=True), LToDataframe.reset_index(drop=True)], axis=1, sort=False)
    return newTable

# Creates a table from file "file", where column "column" has to be a digit
def createTableForHistograms(file, column):
    error = 0
    L = []
    for _, row in file.iterrows():
        if (not math.isnan(row[column])):
            if(error == 0):
                L.append(row)
            else:
                row["error_type"] = error
                error = 0
                L.append(row)
        else:
            error = row["error_type"]
    newTable = pd.DataFrame(L)
    return newTable


# Changes the types of data in the columns
def changeTypeOfData(file):
    newTable = file
    newTable["coord_lat"] = newTable["coord_lat"].str.replace(',', '.').astype(float)
    newTable["coord_lon"] = newTable["coord_lon"].str.replace(',', '.').astype(float)
    newTable["carriage_reader"] = newTable["carriage_reader"].astype(str)
    newTable["carriage_source"] = newTable["carriage_source"].astype(str)
    newTable["event_type"] = newTable["event_type"].astype(str)
    newTable["error_type"] = newTable["error_type"].str.replace('\\N', '-1', regex=False).astype(int)
    tableWithValues["Corrente eléctrica moderável (mA)"] = tableWithValues["Corrente eléctrica moderável (mA)"].astype(float)
    tableWithValues["Velocidade de referência (km/h)"] = tableWithValues["Velocidade de referência (km/h)"].astype(float)
    tableWithValues["Velocidade real eixo 3 (km/h)"] = tableWithValues["Velocidade real eixo 3 (km/h)"].astype(float)
    tableWithValues["Velocidade real eixo 4 (km/h)"] = tableWithValues["Velocidade real eixo 4 (km/h)"].astype(float)
    tableWithValues["Velocidade real eixo 1 (km/h)"] = tableWithValues["Velocidade real eixo 1 (km/h)"].astype(float)
    tableWithValues["Velocidade real eixo 2 (km/h)"] = tableWithValues["Velocidade real eixo 2 (km/h)"].astype(float)
    tableWithValues["Comando esforço (kN)"] = tableWithValues["Comando esforço (kN)"].astype(float)
    tableWithValues["Esforço (real) (kN)"] = tableWithValues["Esforço (real) (kN)"].astype(float)
    tableWithValues["Corrente Conversor 4Q (Aeff)"] = tableWithValues["Corrente Conversor 4Q (Aeff)"].astype(float)
    tableWithValues["Tensão Catenária (Veff)"] = tableWithValues["Tensão Catenária (Veff)"].astype(float)
    return newTable

# Eliminates all the entries where coord_lat and coord_lon are not within the
# specified limits, passed as lists
def eliminatesBasedOnCoordinates(file, columnLat, columnLon, latList, lonList):
    minLat = min(latList)
    maxLat = max(latList)
    minLon = min(lonList)
    maxLon = max(lonList)
    L = []

    for _, row in file.iterrows():
        if row[columnLat] >= minLat and row[columnLat] <= maxLat and \
           row[columnLon] >= minLon and row[columnLon] <= maxLon:
            L.append(row)
    newTable = pd.DataFrame(L)
    return newTable

# Replaces all entries from file file at columns columns with the values present
# at table table
def replaceNamesWithNumbers(file, columns, table, columnName, columnCode):
    L = []
    setTable = table.drop("type", axis = 1).set_index(columnName).T.to_dict('list')
    for _, row in file.iterrows():
        L.append(row)
        for c in columns:
            L[-1][c] = setTable.get(row[c])[0]
    newTable = pd.DataFrame(L)
    return newTable


path = "C:/Users/Pedro Trabuco/Documents/Universidade/5º Ano/Tese/code/tables/"

# Reads the data from the .csv file and drops unwanted/useless columns
vals = pd.read_csv("exported_csv_commas_full_data.csv", encoding="utf_8", sep=';')
print(vals.head())
print("Number of entries on original table: {}".format(len(vals.index)))

# Creates copy of the table "vals" without the entries with binary numbers in 
# the "value" column
tableWithoutBinaries = cleanBinaries(vals, "value")
print(tableWithoutBinaries.head())
print("Number of entries on cleaned table: {}".format(len(tableWithoutBinaries.index)))
tableWithoutBinaries.to_csv(path + "withoutBinaries.csv", encoding="utf-8", index=False)

# Creates columns with values from column "value", with the given names
names = ["Corrente eléctrica moderável (mA)", "Velocidade de referência (km/h)", "Velocidade real eixo 3 (km/h)", \
    "Velocidade real eixo 4 (km/h)", "Velocidade real eixo 1 (km/h)", "Velocidade real eixo 2 (km/h)", \
    "Comando esforço (kN)", "Esforço (real) (kN)", "Corrente Conversor 4Q (Aeff)", "Tensão Catenária (Veff)"]
tableWithValues = createColumnsWithValues(tableWithoutBinaries, 0, names)
print(tableWithValues.head())
print(tableWithValues.tail())
print("Number of entries on table with values: {}".format(len(tableWithValues.index)))
tableWithValues.to_csv(path + "tableWithValues.csv", encoding="utf-8", index=False)

# Changes the types of data and drops irrelevant columns
print(tableWithValues.dtypes)
tableWithValuesAndTypes = changeTypeOfData(tableWithValues)
print(tableWithValuesAndTypes.head())
print(tableWithValuesAndTypes.tail())
print(tableWithValuesAndTypes.dtypes)
tableWithValuesAndTypes.to_csv(path + "tableWithValuesAndTypes.csv", encoding="utf-8", index=False)

# Creates table without rows without values in the most right columns
tableForHistograms = createTableForHistograms(tableWithValuesAndTypes, 13)
tableForHistograms = tableForHistograms.drop(["value"], axis=1)
tableForHistograms = tableForHistograms.drop(["error_sub_type"], axis=1)
tableForHistograms = tableForHistograms.drop(["date_train"], axis=1)
tableForHistograms = tableForHistograms.drop(["event_type"], axis=1)
print(tableForHistograms.head())
print(tableForHistograms.tail())
tableForHistograms.to_csv(path + "tableForHistograms.csv", encoding="utf-8", index=False)

# Creates a column where every row has 0 if there isn't an error, 1 otherwise
tableWithErrorColumn = createColumnsWithValuesCondition(tableWithValuesAndTypes, 11, -1, ["Error"])
print(tableWithErrorColumn.head())
print(tableWithErrorColumn.tail())
tableWithErrorColumn.to_csv(path + "tableWithErrorColumn.csv", encoding="utf-8", index=False)

# Creates a new table by erasing the entries that have coordinates between a
# specific set of values
tableForNewMaps = eliminatesBasedOnCoordinates(vals, 1, 2, [38.596012, 38.595026, 38.593483, 38.591350], \
                                                [-9.073478, -9.070251, -9.065484, -9.063185])
print(tableForNewMaps.head())
print(tableForNewMaps.tail())
tableForNewMaps.to_csv(path + "tableForNewMaps.csv", encoding="utf-8", index=False)

# Creates table for training
tableForTraining = createColumnsWithValuesCondition(vals, 8, -1, ["Error"])
print(tableForTraining.head())
print(tableForTraining.tail())
tableForTraining.to_csv(path + "tableForTraining.csv", encoding="utf-8", index=False)

# Creates second table for training
table = pd.read_csv(path + "carriages.csv", encoding="utf_8")
tableForTraining2 = replaceNamesWithNumbers(tableForTraining, ["carriage_reader", "carriage_source"], table, "name", "code")
print(tableForTraining2.head())
print(tableForTraining2.tail())
tableForTraining2.to_csv(path + "tableForTraining2.csv", encoding="utf-8", index=False)


print("DONE!")
#%%