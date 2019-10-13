import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

test_size = 0.15
number_of_iterations = 5

path = "C:/Users/Pedro Trabuco/Documents/Universidade/5º Ano/Tese/code/"
df = pd.read_csv(path + "tables/tableForTraining_10.csv", encoding="utf_8")

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

    # Naive Bayes
    nb = GaussianNB()
    nb.fit(X_train, y_train)
    predictions = nb.predict(X_test)

    print("test_size = " + str(test_size) + '\n')
    print(confusion_matrix(y_test, predictions))
    print('\n')
    print(classification_report(y_test, predictions))
    print("Accuracy: ", accuracy_score(y_test, predictions))