# From: https://towardsdatascience.com/machine-learning-part-18-boosting-algorithms-gradient-boosting-in-python-ef5ae6965be4
# Tuning from: https://medium.com/all-things-ai/in-depth-parameter-tuning-for-gradient-boosting-3363992e9bae

from sklearn.ensemble import GradientBoostingRegressor, GradientBoostingClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.metrics import mean_squared_error

test_size = 0.15
number_of_iterations = 5
max_depth = 12
learning_rate = 1
n_estimators = 8
min_samples_split = 0.1
min_samples_leaf = 2
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

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size)

for i in range(0, number_of_iterations):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size)

    # Gradient Boosting Tree
    best_regressor = GradientBoostingClassifier(
        max_depth = max_depth,
        n_estimators = n_estimators,
        learning_rate = learning_rate,
        min_samples_split = min_samples_split,
        max_features = max_features,
        min_samples_leaf = min_samples_leaf
    )

    best_regressor.fit(X_train, y_train)
    predictions = best_regressor.predict(X_test)
    predictions = (predictions > 0.5)

    print("max_depth = " + str(max_depth)) 
    print("learning_rate = " + str(learning_rate))
    print("n_estimators = " + str(n_estimators))
    print("min_samples_split = " + str(min_samples_split))
    print("min_samples_leaf = " + str(min_samples_leaf))
    print("max_features = " + str(max_features))
    print(confusion_matrix(y_test, predictions))
    print('\n')
    print(classification_report(y_test, predictions))
    print("Accuracy: ", accuracy_score(y_test, predictions))