import pandas as pd

vals = pd.read_csv('exported_csv_commas.csv', encoding='utf_8', sep=';')
print(vals.head())
print(vals.iloc[0])
print(vals.info())