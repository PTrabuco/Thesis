import pandas as pd

minValue = 1
percentage = 0.05

def comparePercentage(row, percentage, columns):
    length = len(columns)

    for i in range(0, length):
        for i2 in range(i + 1, length):
            if row[columns[i]] > 0 and row[columns[i2]] > 0:
                if row[columns[i]] >= row[columns[i2]] and (row[columns[i]] / row[columns[i2]] - 1) >= percentage:
                    return True
                elif (row[columns[i2]] / row[columns[i]] - 1) >= percentage:
                    return True
    return False


def getData(dataFrame, percentage, minValue, columns):
    L = []
    for _, row in dataFrame.iterrows():
        if (row[columns[0]] == 0 or row[columns[1]] == 0 or row[columns[2]] == 0 or 
            row[columns[3]] == 0) and (row[columns[0]] >= minValue or row[columns[1]] >= minValue or 
            row[columns[2]] >= minValue or row[columns[3]] >= minValue):
            L.append(row)
        elif comparePercentage(row, percentage, columns):
            L.append(row)

    newTable = pd.DataFrame(L)
    return newTable


path = "C:/Users/Pedro Trabuco/Documents/Universidade/5º Ano/Tese/code/tables/"
vals = pd.read_csv(path + "tableForNewMaps2.csv", encoding="utf-8")

tableWithSkatingData = getData(vals, percentage, minValue, [11, 12, 13, 14])
print(tableWithSkatingData.head())
print(tableWithSkatingData.tail())
tableWithSkatingData.to_csv(path + "tableWithSkatingData_" + str(minValue) + "_" + \
    str(percentage).split('.', 1)[-1] + ".csv", encoding="utf-8", index=False)