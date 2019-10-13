import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

test_size = 0.15
# batch_size = 500 
# batch_size = [50, 100, 200, 500, 1000]
# batch_size = [1000]
batch_size = [100]
# nb_epoch = 20 
# nb_epoch = [20, 50, 100, 200, 400]
nb_epoch = [400]

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

onehotencoder = OneHotEncoder(categorical_features = [2, 3, 4, 5])
X = onehotencoder.fit_transform(X).toarray()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size)

for batch in batch_size:
    for epoch in nb_epoch:
        for i in range(0, 5):
            sc = StandardScaler()
            X_train = sc.fit_transform(X_train)
            X_test = sc.transform(X_test)

            classifier = Sequential()

            # Adding the input layer and the first hidden layer
            # Ignore the errors on Dense()
            classifier.add(Dense(output_dim = round(X_train.shape[1]/2), init = 'uniform', activation = 'relu', input_dim = X_train.shape[1]))
            # Adding the second hidden layer
            classifier.add(Dense(output_dim = round(X_train.shape[1]/4), init = 'uniform', activation = 'relu'))
            # Adding the third hidden layer
            # classifier.add(Dense(output_dim = 16, init = 'uniform', activation = 'relu'))
            # Adding the output layer
            classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))

            # Compiling Neural Network
            classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

            # Fitting our model 
            classifier.fit(X_train, y_train, batch_size = batch, nb_epoch = epoch, verbose = 0)

            # Predicting the Test set results
            predictions = classifier.predict(X_test)
            predictions = (predictions > 0.5)

            # Creating the Confusion Matrix
            print("nb_epoch = " + str(epoch) + '\n' + "batch_size = " + str(batch) + 
            '\n' + "test_size = " + str(test_size) + '\n')
            print(confusion_matrix(y_test, predictions))
            # print('\n')
            # print(classification_report(y_test, predictions))
            print('\n' + "Accuracy: ", accuracy_score(y_test, predictions))     