import pandas as pd

def create_column(numberInLine, column, file, name = 'None'):
    L = []
    for index, row in file.iterrows():
        if row[column][0].isdigit() and row[column].find(';') != -1:
            L.append(row['value'].replace('\"', '').split(';')[numberInLine])
            print(L[-1])
    newColumn = pd.DataFrame(L, columns = [name])
    return newColumn


vals = pd.read_csv('exported_csv_commas.csv', encoding='utf_8', sep=';')
print(vals.head(10))
newColumn = create_column(9, 'value', vals, 'Test')
print(newColumn.head(5))
vals.append(newColumn)
print(vals.head(10))