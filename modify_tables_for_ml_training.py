import pandas as pd

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
tableForTraining = pd.read_csv(path + "tableForTraining.csv", encoding="utf_8")
# Creates table for training
# tableForTraining = createColumnsWithValuesCondition(vals, 8, -1, ["Error"])
print(tableForTraining.head())
print(tableForTraining.tail())
# tableForTraining.to_csv(path + "tableForTraining.csv", encoding="utf-8", index=False)

table = pd.read_csv(path + "carriages.csv", encoding="utf_8")
tableForTraining2 = replaceNamesWithNumbers(tableForTraining, ["carriage_reader", "carriage_source"], table, "name", "code")
print(tableForTraining2.head())
print(tableForTraining2.tail())
tableForTraining2.to_csv(path + "tableForTraining2.csv", encoding="utf-8", index=False)


print("DONE!")