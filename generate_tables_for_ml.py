import pandas as pd
import numpy as np

numEntries = 5

def createTimedTable(file, fileTrimmed, numPastEntries):
    L = []
    length = len(file.index)
    for i in range(numPastEntries, length):
        aux = file.iloc[i]
        for n in range(1, numPastEntries):
            aux = np.concatenate([aux, fileTrimmed.iloc[i - n]])
        L.append(aux)
    newTable = pd.DataFrame(L)
    return newTable

def getErrorsFromFuture(file, numFutureEntries, errorColumn):
    length = len(file.index)
    L = []
    for i in range(0, length - numFutureEntries):
        L.append(file.iloc[i])
        for n in range(1, numFutureEntries):
            if file.iloc[i + n][errorColumn] == 1:
                L[-1][errorColumn] = 1
                break
    for i in range(length - numFutureEntries, length):
        L.append(file.iloc[i])
        for n in range(1, numFutureEntries - i - (length - numFutureEntries)):
            if file.iloc[i + n][errorColumn] == 1:
                L[-1][errorColumn] = 1
                break

    newTable = pd.DataFrame(L)
    return newTable


path = "C:/Users/Pedro Trabuco/Documents/Universidade/5º Ano/Tese/code/tables/"
tableForTraining2 = pd.read_csv(path + "tableForTraining2.csv", encoding="utf_8")
tableForTraining2 = tableForTraining2.drop(columns = ["date_sys"])
tableForTraining2_trimmed = tableForTraining2.drop(columns = ["carriage_reader",
                            "monitor_reader", "carriage_source", "device_source",
                            "mission", "error_type", "Error"])

tableForTraining3 = createTimedTable(tableForTraining2, tableForTraining2_trimmed, numEntries)
tableForTraining3 = getErrorsFromFuture(tableForTraining3, numEntries, 18)
print(tableForTraining3.head())
print(tableForTraining3.tail())
tableForTraining3.to_csv(path + "tableForTraining_" + str(numEntries) + ".csv", 
                         encoding="utf-8", index=False)

print("DONE!")