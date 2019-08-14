import pandas as pd
from collections import Counter

# Prints the number of occurrences for every type of error
path = "C:/Users/Pedro Trabuco/Documents/Universidade/5º Ano/Tese/code/"
vals = pd.read_csv(path + "tables/tableWithSkatingData_5_1.csv", encoding="utf_8")

print("ERRORS OCCURRENCES: ")
print("Type 1: ", vals[vals.error_type == 1].shape[0])
print("Type 2: ", vals[vals.error_type == 2].shape[0])
print("Type 3: ", vals[vals.error_type == 3].shape[0])
print("Type 4: ", vals[vals.error_type == 4].shape[0])
print("Type 5: ", vals[vals.error_type == 5].shape[0])

print(Counter(vals["error_type"]))