from sklearn.ensemble import GradientBoostingRegressor, GradientBoostingClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.metrics import mean_squared_error
from matplotlib.legend_handler import HandlerLine2D
from sklearn.metrics import roc_curve, auc

test_size = 0.15
max_depth = 12
learning_rate = 1
n_estimators = 8
min_samples_split = 0.1
min_samples_leaf = 0.1
max_features = 34

path = "C:/Users/Pedro Trabuco/Documents/Universidade/5º Ano/Tese/code/"
df = pd.read_csv(path + "tables/tableForTraining_5.csv", encoding="utf_8")

# Data splitting
X = df.drop(df.columns[18], axis = 1)
y = df.iloc[:,18]

labelencoder_X_1 = LabelEncoder()
X.iloc[:,2] = labelencoder_X_1.fit_transform(X.iloc[:,2])
labelencoder_X_2 = LabelEncoder()
X.iloc[:,3] = labelencoder_X_2.fit_transform(X.iloc[:,3])
labelencoder_X_3 = LabelEncoder()
X.iloc[:,4] = labelencoder_X_3.fit_transform(X.iloc[:,4])
labelencoder_X_4 = LabelEncoder()
X.iloc[:,5] = labelencoder_X_4.fit_transform(X.iloc[:,5])

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = test_size)

max_features = list(range(1,df.shape[1]))
train_results = []
test_results = []

for max_feature in max_features:
    print(str(max_feature))
    model = GradientBoostingClassifier(
        learning_rate = learning_rate, 
        n_estimators = n_estimators, 
        max_depth = max_depth, 
        min_samples_split = min_samples_split, 
        max_features = max_feature,
        min_samples_leaf = min_samples_leaf
    )
    model.fit(x_train, y_train)   
    train_pred = model.predict(x_train)   
    false_positive_rate, true_positive_rate, thresholds = roc_curve(y_train, train_pred)
    roc_auc = auc(false_positive_rate, true_positive_rate)
    train_results.append(roc_auc)   
    y_pred = model.predict(x_test)  
    false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred)
    roc_auc = auc(false_positive_rate, true_positive_rate)
    test_results.append(roc_auc)

line1, = plt.plot(max_features, train_results, 'b', label="Train AUC")
line2, = plt.plot(max_features, test_results, 'r', label = "Test AUC")
plt.legend(handler_map={line1: HandlerLine2D(numpoints=2)})
plt.ylabel("AUC score")
plt.xlabel("max_feature")
plt.show()