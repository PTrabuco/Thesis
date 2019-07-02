import pandas as pd
import numpy as np

# Cleans all the entries with binary strings on file 'file' and 
# column 'columnWithBinaries'
def cleanBinaries(file, columnWithBinaries):
    L = []
    for index, row in file.iterrows():
        if (not row[columnWithBinaries][0].isdigit()) or (row[columnWithBinaries][0] != '0' and \
        row[columnWithBinaries][0] != '1' and row[columnWithBinaries][1] != '0' and row[columnWithBinaries][1] != '1'):
            L.append(row)
    newTable = pd.DataFrame(L)
    return newTable

# Creates columns from column 'column' that belong to array 'arrayOfNumbers' 
# from file 'file', where the columns have the names 'names'
def createColumnsWithValues(file, column, arrayOfNumbers, names):
    L = [names]
    for index, row in file.iterrows():
        if row[column][0].isdigit():
            L.append(row[column].replace('\"', '').split(';'))
        else:
            L.append([np.NaN] * len(names))
    LToDataframe = pd.DataFrame(L[1:], columns=L[0])
    newTable = pd.concat([file.reset_index(drop=True), LToDataframe.reset_index(drop=True)], axis=1, sort=False)
    return newTable


# Reads the data from the .csv file
vals = pd.read_csv('exported_csv_commas_full_data.csv', encoding='utf_8', sep=';')
print(vals.head(10))
print("Number of entries on original table: {}".format(len(vals.index)))

# Creates copy of the table 'vals' without the entries with binary numbers in 
# the 'value' column
tableWithoutBinaries = cleanBinaries(vals, 'value')
print(tableWithoutBinaries.head(5))
print("Number of entries on cleaned table: {}".format(len(tableWithoutBinaries.index)))
tableWithoutBinaries.to_csv("withoutBinaries.csv", encoding='utf-8', index=False)

# Creates columns with values from column 'value'
names = ["Corrente eléctrica moderável (mA)", "Velocidade de referência (km/h)", "Velocidade real eixo 3 (km/h)", \
    "Velocidade real eixo 4 (km/h)", "Velocidade real eixo 1 (km/h)", "Velocidade real eixo 2 (km/h)", \
    "Comando esforço (kN)", "Esforço (real) (kN)", "Corrente Conversor 4Q (Aeff)", "Tensão Catenária (Veff)"]
tableWithValues = createColumnsWithValues(tableWithoutBinaries, 0, list(range(0,10)), names)
print(tableWithValues.head(5))
print(tableWithValues.tail(5))
print("Number of entries on table with values: {}".format(len(tableWithValues.index)))
tableWithValues.to_csv("tableWithValues.csv", encoding='utf-8', index=False)